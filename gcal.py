from __future__ import print_function

import datetime
import os.path
import pytz

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# If modifying these scopes, delete the file token.json.
SCOPES = ['https://www.googleapis.com/auth/calendar.readonly']
pst = pytz.timezone('America/Los_Angeles')

def get_day_events():
    """Returns relevant info of the events on the user's calendar for the day.
    """
    creds = None
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.json', 'w') as token:
            token.write(creds.to_json())

    try:
        service = build('calendar', 'v3', credentials=creds)

        # Get the current date and time in PST
        current_datetime_pst = datetime.datetime.now(pst)

        # Extract the date and combine with midnight to get the start of the day in PST
        start_of_day_pst = pst.localize(datetime.datetime.combine(current_datetime_pst.date(), datetime.time(0, 0)))

        # Convert to the desired format
        # Convert to the desired RFC3339 format with time zone offset
        timeMin = start_of_day_pst.strftime('%Y-%m-%dT%H:%M:%S%z')

        # Adjust the format to include a colon in the timezone offset (e.g., -07:00 instead of -0700)
        timeMin = timeMin[:-2] + ':' + timeMin[-2:]

        print(f'Getting the events for {timeMin}')

        # Calculate timeMax by adding one day to start_of_day_pst
        end_of_day_pst = start_of_day_pst + datetime.timedelta(days=1)
        timeMax = end_of_day_pst.strftime('%Y-%m-%dT%H:%M:%S%z')
        timeMax = timeMax[:-2] + ':' + timeMax[-2:]

        events_result = service.events().list(calendarId='primary', timeMin=timeMin,
                                              timeMax=timeMax, singleEvents=True,
                                              orderBy='startTime').execute()
        events = events_result.get('items', [])
        print(events)

        if not events:
            print('No upcoming events found.')
            return

        parsed_events = []

        for event in events:
            parsed_event = {
                "summary": event.get("summary", None),
                "description": event.get("description", None),
                "location": event.get("location", None),
                "start": event.get("start", {}).get("dateTime", None),
                "end": event.get("end", {}).get("dateTime", None),
                "attendees": [attendee.get("email", None) for attendee in event.get("attendees", [])]
            }
            parsed_events.append(parsed_event)
        return parsed_events

    except HttpError as error:
        print('An error occurred: %s' % error)

def get_ten_events():
    """Shows basic usage of the Google Calendar API.
    Returns the start and name of the next 10 events on the user's calendar.
    """
    creds = None
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.json', 'w') as token:
            token.write(creds.to_json())

    try:
        service = build('calendar', 'v3', credentials=creds)

        # Call the Calendar API
        now = datetime.datetime.utcnow().isoformat() + 'Z'  # 'Z' indicates UTC time
        print('Getting the upcoming 10 events')
        events_result = service.events().list(calendarId='primary', timeMin=now,
                                              maxResults=10, singleEvents=True,
                                              orderBy='startTime').execute()
        events = events_result.get('items', [])
        print(events)

        if not events:
            print('No upcoming events found.')
            return

        parsed_events = []

        for event in events:
            parsed_event = {
                "summary": event.get("summary", None),
                "description": event.get("description", None),
                "location": event.get("location", None),
                "start": event.get("start", {}).get("dateTime", None),
                "end": event.get("end", {}).get("dateTime", None),
                "attendees": [attendee.get("email", None) for attendee in event.get("attendees", [])]
            }
            parsed_events.append(parsed_event)
        return parsed_events

    except HttpError as error:
        print('An error occurred: %s' % error)

def main():
    #print(get_ten_events())
    print(get_day_events())

if __name__ == '__main__':
    main()