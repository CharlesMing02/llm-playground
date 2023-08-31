import json
from typing import List, Optional
from .models import ClothingPiece, Outfit
import os

dir_path = os.path.dirname(os.path.realpath(__file__))
hardcoded_path = os.path.join(dir_path, "outfits.json")

def load_data(file_path: str = hardcoded_path):
    with open(file_path, "r") as f:
        return json.load(f)

def get_clothing_piece_by_id(piece_id: int, file_path: str = hardcoded_path) -> Optional[ClothingPiece]:
    data = load_data(file_path)
    piece_data = next((piece for piece in data['clothing_pieces'] if piece['id'] == piece_id), None)
    if piece_data:
        return ClothingPiece(**piece_data)
    return None

def get_all_clothing_pieces(file_path: str = hardcoded_path) -> List[ClothingPiece]:
    data = load_data(file_path)
    return [ClothingPiece(**piece) for piece in data['clothing_pieces']]

def get_outfit_by_id(outfit_id: int, file_path: str = hardcoded_path) -> Optional[Outfit]:
    data = load_data(file_path)
    outfit_data = next((outfit for outfit in data['outfits'] if outfit['id'] == outfit_id), None)
    if outfit_data:
        pieces = [get_clothing_piece_by_id(piece_id) for piece_id in outfit_data['pieces']]
        return Outfit(pieces=pieces, **{k: outfit_data[k] for k in ['id', 'style', 'traits', 'convenience_score', 'like_score']})
    return None

def get_all_outfits(file_path: str = hardcoded_path) -> List[Outfit]:
    data = load_data(file_path)
    outfits = []
    for outfit_data in data['outfits']:
        pieces = [get_clothing_piece_by_id(piece_id) for piece_id in outfit_data['pieces']]
        outfits.append(Outfit(pieces=pieces, **{k: outfit_data[k] for k in ['id', 'style', 'traits', 'convenience_score', 'like_score']}))
    return outfits
