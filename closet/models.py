from dataclasses import dataclass, field
from typing import List, Optional

# hardcoded clothing ids in laundry
laundry = set([1])

@dataclass
class ClothingPiece:
    id: int
    type: str
    color: str
    size: Optional[str] = field(default=None)
    brand: Optional[str] = field(default=None)

    def generate_description(self):
        return f"{self.brand} {self.type} in {self.color}, size {self.size if self.size else 'N/A'}"

@dataclass
class Outfit:
    id: int
    pieces: List[ClothingPiece]
    style: str
    traits: List[str]
    convenience_score: int
    like_score: int

    def generate_description(self):
        pieces_description = " | ".join([piece.generate_description() for piece in self.pieces])
        return f"Outfit: {pieces_description} | Style: {self.style} | Traits: {', '.join(self.traits)} | Convenience Score: {self.convenience_score} | Like Score: {self.like_score}"

    def generate_metadata(self):
        return {
            "id": self.id,
            "available": all(piece.id not in laundry for piece in self.pieces)
        }