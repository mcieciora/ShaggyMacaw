from enum import Enum


class PieceType(Enum):
    """Enumeration of all possible values of square."""

    EMPTY = 0
    PAWN = 1
    KNIGHT = 2
    BISHOP = 3
    ROOK = 4
    QUEEN = 5
    KING = 6


class PieceMove(Enum):
    """Enumeration of moves types."""

    MOVE = 0
    CAPTURE = 1
    MOVE_OR_CAPTURE = 2


value_to_square_value_map = {
    "N": PieceType.KNIGHT,
    "B": PieceType.BISHOP,
    "R": PieceType.ROOK,
    "Q": PieceType.QUEEN,
    "K": PieceType.KING,
}

movement_patterns = {
    "N": [(2, 1), (1, 2), (2, -1), (1, -2), (-2, 1), (-1, 2), (-2, -1), (-1, -2)],
    "B": [(1, 1), (1, -1), (-1, 1), (-1, -1)],
    "R": [(0, 1), (0, -1), (1, 0), (-1, 0)],
    "Q": [(1, 1), (1, -1), (-1, 1), (-1, -1), (0, 1), (0, -1), (1, 0), (-1, 0)],
    "K": [(1, 0), (0, 1), (1, 1), (-1, 0), (0, -1), (-1, -1), (1, -1), (-1, 1)],
}

pawn_movement_pattern = {
    PieceMove.MOVE: {
        True: {True: [(0, 1), (0, 2)], False: [(0, 1)]},
        False: {True: [(0, -1), (0, -2)], False: [(0, -1)]},
    },
    PieceMove.CAPTURE: {True: [(-1, 1), (1, 1)], False: [(-1, -1), (1, -1)]},
}


def create_piece(value, position=None):
    """Piece factory function."""
    if value.isdigit():
        return PieceType.EMPTY
    if value in ["p", "P"]:
        return Pawn(value, position)
    return Piece(value, position)


class Pawn:
    """Pawn static values and behaviour declaration class."""

    def __init__(self, value, position):
        """Initialize Pawn object."""
        self.value = value
        self.position = position
        self.piece_type = PieceType.PAWN
        self.active_colour_white = self.value.isupper()
        self.movement_pattern = {
            move_type: (
                movement[self.active_colour_white][self.is_pawn_in_starting_position()]
                if move_type is PieceMove.MOVE
                else movement[self.active_colour_white]
            )
            for move_type, movement in pawn_movement_pattern.items()
        }

    def is_pawn_in_starting_position(self):
        """Check if pawn is in starting position."""
        return (
            self.active_colour_white
            and self.position[1] == 1
            or not self.active_colour_white
            and self.position[1] == 6
        )

    def is_pawn_next_move_promotion(self):
        """Check if pawn is on 7th rank."""
        return (
            self.active_colour_white
            and self.position[1] == 6
            or not self.active_colour_white
            and self.position[1] == 1
        )


class Piece:
    """Piece static values and behaviour declaration class."""

    def __init__(self, value, position):
        """Initialize Piece object."""
        self.value = value
        self.position = position
        self.piece_type = value_to_square_value_map[value.upper()]
        self.active_colour_white = self.value.isupper()
        self.movement_pattern = movement_patterns[value.upper()]
