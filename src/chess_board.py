from types import new_class

from src.fen import Fen


class ChessBoard:
    """Moves generation and chess board management class."""

    def __init__(self, fen):
        """Initialize ChessBoard object."""
        self.fen = Fen(fen)
        self.possible_capture_dict = {
            True: [],
            False: []
        }

    def generate_all_possible_moves(self):
        """Generate all possible moves."""
        all_possible_moves = []
        for index, piece in enumerate(self.fen.board_setup):
            match piece:
                case "p" | "P":
                    all_possible_moves.extend(self.generate_pawn_moves(index, piece))
        return all_possible_moves

    def generate_pawn_moves(self, index, piece):
        """Generate pawn moves."""
        y, x = self.fen.convert_index_to_coordinates(index)

        pawn_movement_pattern = {
            True: [(0, -1), (0, -2)] if self.is_pawn_in_starting_position(piece, y) else [(0, -1)],
            False: [(0, 1), (0, 2)] if self.is_pawn_in_starting_position(piece, y) else [(0, 1)]
        }
        pawn_capture_pattern = {
            True: [(-1, -1), (1, -1)],
            False: [(-1, 1), (1, 1)]
        }
        movement_pattern = pawn_movement_pattern[piece.isupper()]
        capture_pattern = pawn_capture_pattern[piece.isupper()]

        available_squares = []
        for movement in movement_pattern:
            new_square = self.is_move_possible((x, y), movement, True)
            if self.is_pawn_next_move_promotion(piece, y) and new_square:
                available_squares.extend([f"{new_square}={promotion_move}" for promotion_move in ["Q", "R", "N", "B"]])
            elif new_square:
                available_squares.append(new_square)
            else:
                break
        for capture in capture_pattern:
            new_square = self.check_capture_square((x, y), capture, index, piece)
            if self.is_pawn_next_move_promotion(piece, y) and new_square:
                available_squares.extend([f"{new_square}={promotion_move}" for promotion_move in ["Q", "R", "N", "B"]])
            elif new_square:
                available_squares.append(new_square)
            if new_square := self.is_en_passant_possible((x, y), capture, index, piece):
                available_squares.append(new_square)
        return available_squares

    @staticmethod
    def is_pawn_in_starting_position(pawn, y):
        """Check if pawn is in starting position."""
        return pawn.isupper() and y == 6 or pawn.islower() and y == 1

    @staticmethod
    def is_pawn_next_move_promotion(pawn, y):
        """Check if pawn is on 7th rank."""
        return pawn.isupper() and y == 1 or pawn.islower() and y == 6

    def is_move_possible(self, position, movement, expected_empty):
        """Calculate new position, verify if square is in board and check if it is expected to be empty."""
        default_return = False
        x = position[0] + movement[0]
        y = position[1] + movement[1]
        if self.fen.coordinates_in_boundaries(y, x):
            new_index = self.fen.convert_coordinates_to_index(y, x)
            square = self.fen.convert_index_to_square(new_index)
            if expected_empty is self.fen.is_square_empty(square):
                default_return = square
        return default_return

    def check_capture_square(self, position, capture, index, piece):
        """Verify if move is possible and check if square is occupied by opposite colour piece."""
        default_return = False
        original_square = self.fen.convert_index_to_square(index)
        square = self.is_move_possible(position, capture, False)
        # TODO verify possible_capture_dict
        if square:
            self.possible_capture_dict[piece.isupper()].append(square)
        if square and self.fen.get_square_active_colour(square) is not piece.isupper():
            default_return = f"{original_square[0]}x{square}"
        return default_return

    def is_en_passant_possible(self, position, capture, index, piece):
        """Verify if move is possible and check if square is occupied by opposite colour piece."""
        default_return = False
        original_square = self.fen.convert_index_to_square(index)
        if new_square := self.is_move_possible((position[0], position[1]), capture, True):
            if self.fen.is_white_an_active_colour() is piece.isupper() and new_square == self.fen.available_en_passant:
                default_return = f"{original_square[0]}x{new_square}"
        return default_return
