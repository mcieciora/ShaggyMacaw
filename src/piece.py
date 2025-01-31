from src.square_value import SquareValue


class Pawn:
    """Pawn static values and behaviour declaration class."""

    def __init__(self, letter, position):
        """Initialize Pawn object."""
        self.piece_type = SquareValue.PAWN
        self.active_colour_white = letter.isupper()
        self.position = position

        pawn_movement_pattern = {
            True: [(0, 1), (0, 2)] if self.is_pawn_in_starting_position() else [(0, 1)],
            False: [(0, -1), (0, -2)] if self.is_pawn_in_starting_position() else [(0, -1)]
        }
        pawn_capture_pattern = {
            True: [(-1, 1), (1, 1)],
            False: [(-1, -1), (1, -1)]
        }

        self.movement_pattern = pawn_movement_pattern[self.active_colour_white]
        self.capture_pattern = pawn_capture_pattern[self.active_colour_white]

    def is_pawn_in_starting_position(self):
        """Check if pawn is in starting position."""
        return (self.active_colour_white and self.position[1] == 1 or not self.active_colour_white and
                self.position[1] == 6)

    def is_pawn_next_move_promotion(self):
        """Check if pawn is on 7th rank."""
        return (self.active_colour_white and self.position[1] == 6 or not self.active_colour_white and
                self.position[1] == 1)


class Piece:
    """Piece static values and behaviour declaration class."""

    letter_to_square_value_map = {
        "N": SquareValue.KNIGHT,
        "B": SquareValue.BISHOP,
        "R": SquareValue.ROOK,
        "Q": SquareValue.QUEEN
    }
    movement_patterns = {
        "-": SquareValue.EMPTY,
        "N": [(2, 1), (1, 2), (2, -1), (1, -2), (-2, 1), (-1, 2), (-2, -1), (-1, -2)],
        "B": [(1, 1), (1, -1), (-1, 1), (-1, -1)],
        "R": [(0, 1), (0, -1), (1, 0), (-1, 0)],
        "Q": [(1, 1), (1, -1), (-1, 1), (-1, -1), (0, 1), (0, -1), (1, 0), (-1, 0)],
        "K": [(1, 0), (0, 1),  (1, 1), (-1, 0), (0, -1), (-1, -1), (1, -1), (-1, 1)]
    }

    def __init__(self, letter, position):
        """Initialize Piece object."""
        self.piece_type = self.letter_to_square_value_map[letter.upper()]
        self.active_colour_white = letter.isupper()
        self.position = position
        self.movement_pattern = self.movement_patterns[letter]
