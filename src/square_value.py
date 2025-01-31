from enum import Enum


class SquareValue(Enum):
    """Enumeration of all possible values of square."""
    Empty = 0
    Pawn = 1
    Knight = 2
    Bishop = 3
    Rook = 4
    Queen = 5
    King = 6
