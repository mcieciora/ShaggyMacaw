from enum import Enum


class PieceValue(Enum):
    """Enumeration of all possible values of square."""

    EMPTY = 0
    PAWN = 1
    KNIGHT = 2
    BISHOP = 3
    ROOK = 4
    QUEEN = 5
    KING = 6
