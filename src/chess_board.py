from src.fen import Fen
from src.piece import Pawn


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
            square = self.fen.convert_index_to_square(index)
            match piece:
                case "p" | "P":
                    all_possible_moves.extend(self.generate_pawn_moves(square))
        return all_possible_moves

    def generate_pawn_moves(self, square):
        """Generate pawn moves."""
        index = self.fen.convert_square_to_index(square)
        piece = self.fen.get_square_value(square)
        y, x = self.fen.convert_index_to_coordinates(index)

        pawn = Pawn(piece, (x, y))

        available_squares = []
        for movement in pawn.movement_pattern:
            new_square = self.is_move_possible((x, y), movement, True)
            if pawn.is_pawn_next_move_promotion() and new_square:
                available_squares.extend([f"{new_square}={promotion_move}" for promotion_move in ["Q", "R", "N", "B"]])
            elif new_square:
                available_squares.append(f"{square}{new_square}")
            else:
                break
        for capture in pawn.capture_pattern:
            new_square = self.check_capture_square((x, y), capture, pawn)
            if pawn.is_pawn_next_move_promotion() and new_square:
                available_squares.extend([f"{new_square}={promotion_move}" for promotion_move in ["Q", "R", "N", "B"]])
            elif new_square:
                available_squares.append(new_square)
            if new_square := self.is_en_passant_possible((x, y), capture, pawn):
                available_squares.append(new_square)
        return available_squares

    def is_move_possible(self, cur_position, movement, expected_empty):
        """Calculate new position, verify if square is in board and check if it is expected to be empty."""
        default_return = False
        x = cur_position[0] + movement[0]
        y = cur_position[1] + movement[1]
        if self.fen.coordinates_in_boundaries(x, y):
            new_index = self.fen.convert_coordinates_to_index(x, y)
            square = self.fen.convert_index_to_square(new_index)
            if expected_empty is self.fen.is_square_empty(square):
                default_return = square
        return default_return

    def check_capture_square(self, cur_position, capture, piece):
        """Verify if move is possible and check if square is occupied by opposite colour piece."""
        default_return = False
        original_square_index = self.fen.convert_coordinates_to_index(cur_position[0], cur_position[1])
        original_square = self.fen.convert_index_to_square(original_square_index)
        square = self.is_move_possible(cur_position, capture, False)
        # TODO verify possible_capture_dict
        if square:
            self.possible_capture_dict[piece.active_colour_white].append(square)
        if square and self.fen.get_square_active_colour(square) is not piece.active_colour_white:
            default_return = f"{original_square}{square}"
        return default_return

    def is_en_passant_possible(self, position, capture, piece):
        """Verify if move is possible and check if square is occupied by opposite colour piece."""
        default_return = False
        original_square_index = self.fen.convert_coordinates_to_index(position[0], position[1])
        original_square = self.fen.convert_index_to_square(original_square_index)
        if new_square := self.is_move_possible((position[0], position[1]), capture, True):
            if self.fen.is_white_an_active_colour() is piece.active_colour_white and new_square == self.fen.available_en_passant:
                default_return = f"{original_square}{new_square}"
        return default_return
