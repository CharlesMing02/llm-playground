import json

# Sample data
styles = ["casual", "formal", "sporty", "business casual", "beach"]
traits = ["dressy", "casual", "relaxed", "sharp", "cozy"]

clothing_pieces = [
    {"id": 1, "type": "shirt", "color": "blue", "size": "M", "brand": "Polo Ralph Lauren"},
    {"id": 2, "type": "pants", "color": "black", "size": "32", "brand": "Levi's 501 Original Fit Jeans"},
    {"id": 3, "type": "shoes", "color": "white", "size": "10", "brand": "Nike Killshot 2 Leather Shoes"},
    {"id": 4, "type": "jacket", "color": "brown", "size": "M", "brand": "Tommy Hilfiger Men's Classic Hooded Puffer Jacket"},
    {"id": 5, "type": "hat", "color": "black", "size": "L", "brand": "Adidas Originals Cap"},
    {"id": 6, "type": "shorts", "color": "khaki", "size": "32", "brand": "Under Armour Men's Raid 10-inch Workout Gym Shorts"},
    {"id": 7, "type": "sunglasses", "color": "black", "brand": "Ray-Ban Classic Aviator"},
    {"id": 8, "type": "watch", "color": "silver", "brand": "Seiko Men's Stainless Steel Watch"},
    {"id": 9, "type": "shirt", "color": "white", "size": "M", "brand": "Calvin Klein Cotton Classics"},
    {"id": 10, "type": "shoes", "color": "black", "size": "10", "brand": "Adidas Ultraboost 21"},
    {"id": 11, "type": "belt", "color": "brown", "brand": "Hermès Men's Belt"},
    {"id": 12, "type": "socks", "color": "gray", "size": "M", "brand": "Nike Performance Cushion Crew Training Socks"}
]

outfits = [
    {
        "id": 1,
        "pieces": [1, 2, 3, 8],
        "style": "casual",
        "traits": ["casual", "relaxed"],
        "convenience_score": 8,
        "like_score": 9
    },
    {
        "id": 2,
        "pieces": [9, 6, 10, 5, 7],
        "style": "beach",
        "traits": ["casual", "relaxed", "cozy"],
        "convenience_score": 9,
        "like_score": 7
    },
    {
        "id": 3,
        "pieces": [1, 2, 3, 4, 8, 11],
        "style": "business casual",
        "traits": ["sharp", "dressy"],
        "convenience_score": 7,
        "like_score": 8
    },
    {
        "id": 4,
        "pieces": [9, 2, 10, 12],
        "style": "sporty",
        "traits": ["relaxed", "sharp"],
        "convenience_score": 8,
        "like_score": 8
    }
]

# Additional clothing pieces
clothing_pieces.extend([
    {"id": 13, "type": "shirt", "color": "green", "size": "M", "brand": "Lacoste Classic Polo Shirt"},
    {"id": 14, "type": "pants", "color": "navy", "size": "32", "brand": "Dockers Classic Fit Chinos"},
    {"id": 15, "type": "shoes", "color": "brown", "size": "10", "brand": "Clarks Desert Boot"},
    {"id": 16, "type": "jacket", "color": "black", "size": "M", "brand": "North Face Thermoball Eco Jacket"},
    {"id": 17, "type": "tie", "color": "red", "brand": "Tommy Hilfiger Stripe Tie"},
    {"id": 18, "type": "shirt", "color": "striped blue", "size": "M", "brand": "Brooks Brothers Dress Shirt"},
    {"id": 19, "type": "shoes", "color": "black", "size": "10", "brand": "Allen Edmonds Park Avenue Oxford"},
    {"id": 20, "type": "sweater", "color": "gray", "size": "M", "brand": "Banana Republic Cashmere Sweater"}
])

# Additional outfits
outfits.extend([
    {
        "id": 5,
        "pieces": [13, 14, 15, 16],
        "style": "casual",
        "traits": ["casual", "cozy"],
        "convenience_score": 8,
        "like_score": 8
    },
    {
        "id": 6,
        "pieces": [18, 2, 19, 17],
        "style": "formal",
        "traits": ["dressy", "sharp"],
        "convenience_score": 7,
        "like_score": 9
    },
    {
        "id": 7,
        "pieces": [1, 6, 3, 5],
        "style": "beach",
        "traits": ["relaxed", "casual"],
        "convenience_score": 9,
        "like_score": 7
    },
    {
        "id": 8,
        "pieces": [18, 14, 19, 17, 20],
        "style": "business casual",
        "traits": ["sharp", "dressy"],
        "convenience_score": 8,
        "like_score": 9
    },
    {
        "id": 9,
        "pieces": [13, 2, 10, 12],
        "style": "sporty",
        "traits": ["relaxed", "casual"],
        "convenience_score": 8,
        "like_score": 8
    },
    {
        "id": 10,
        "pieces": [9, 14, 15, 16],
        "style": "casual",
        "traits": ["casual", "cozy"],
        "convenience_score": 8,
        "like_score": 7
    },
    {
        "id": 11,
        "pieces": [1, 2, 3, 4, 7],
        "style": "casual",
        "traits": ["relaxed", "casual"],
        "convenience_score": 9,
        "like_score": 8
    },
    {
        "id": 12,
        "pieces": [18, 6, 19, 17],
        "style": "formal",
        "traits": ["sharp", "dressy"],
        "convenience_score": 7,
        "like_score": 9
    },
    {
        "id": 13,
        "pieces": [13, 14, 3, 16],
        "style": "casual",
        "traits": ["casual", "relaxed"],
        "convenience_score": 8,
        "like_score": 8
    },
    {
        "id": 14,
        "pieces": [9, 2, 10, 12, 20],
        "style": "sporty",
        "traits": ["relaxed", "casual"],
        "convenience_score": 8,
        "like_score": 7
    }
])

data = {
    "clothing_pieces": clothing_pieces,
    "outfits": outfits
}

# Save to a JSON file
with open("outfits.json", "w") as file:
    json.dump(data, file, indent=4)

print("JSON file generated!")
