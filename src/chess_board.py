from src.fen import Fen
from src.piece import PieceType


class ChessBoard:
    """Moves generation and chess board management class."""

    def __init__(self, fen):
        """Initialize ChessBoard object."""
        self.fen = Fen(fen)

    def generate_all_possible_moves(self):
        """Generate all possible moves."""
        all_possible_moves = []
        for rank in self.fen.board_setup:
            for piece in rank:
                if piece is PieceType.EMPTY:
                    continue
                if piece.piece_type is PieceType.PAWN:
                    all_possible_moves.extend(self.generate_pawn_moves(piece))
                elif piece.piece_type in [PieceType.ROOK, PieceType.BISHOP]:
                    all_possible_moves.extend(self.generate_piece_moves(piece))
                else:
                    pass
        return all_possible_moves

    def generate_pawn_moves(self, piece):
        """Generate pawn moves."""
        available_squares = []
        for movement in piece.movement_pattern:
            new_square = self.is_move_possible(piece.position, movement, True)
            if piece.is_pawn_next_move_promotion() and new_square:
                available_squares.extend([f"{new_square}={promotion_move}" for promotion_move in ["Q", "R", "N", "B"]])
            elif new_square:
                square_value = self.fen.convert_coordinates_to_square(piece.position[0], piece.position[1])
                available_squares.append(f"{square_value}{new_square}")
            else:
                break
        for capture in piece.capture_pattern:
            new_square = self.check_capture_square(piece, capture)
            if piece.is_pawn_next_move_promotion() and new_square:
                available_squares.extend([f"{new_square}={promotion_move}" for promotion_move in ["Q", "R", "N", "B"]])
            elif new_square:
                available_squares.append(new_square)
            if new_square := self.is_en_passant_possible(piece.position, capture, piece):
                available_squares.append(new_square)
        return available_squares

    def generate_piece_moves(self, piece):
        """Generate rook moves."""
        available_squares = []
        for movement in piece.movement_pattern:
            for multiplier in range(1, 8):
                multiplied_movement = tuple([multiplier*x for x in movement])
                if new_square := self.is_move_possible(piece.position, multiplied_movement, True):
                    square_value = self.fen.convert_coordinates_to_square(piece.position[0], piece.position[1])
                    available_squares.append(f"{square_value}{new_square}")
                elif new_square := self.check_capture_square(piece, multiplied_movement):
                    available_squares.append(new_square)
                    break
                else:
                    break
        return available_squares

    def is_move_possible(self, cur_position, movement, expected_empty):
        """Calculate new position, verify if square is in board and check if it is expected to be empty."""
        default_return = False
        x = cur_position[0] + movement[0]
        y = cur_position[1] + movement[1]
        if self.fen.coordinates_in_boundaries(x, y):
            square = self.fen.convert_coordinates_to_square(x, y)
            if expected_empty is self.fen.is_square_empty(square):
                default_return = square
        return default_return

    def check_capture_square(self, piece, capture):
        """Verify if move is possible and check if square is occupied by opposite colour piece."""
        default_return = False
        original_square = self.fen.convert_coordinates_to_square(piece.position[0], piece.position[1])
        square = self.is_move_possible(piece.position, capture, False)
        if square and self.fen.get_square_active_colour(square) is not piece.active_colour_white:
            default_return = f"{original_square}{square}"
        return default_return

    def is_en_passant_possible(self, position, capture, piece):
        """Verify if move is possible and check if square is occupied by opposite colour piece."""
        default_return = False
        original_square = self.fen.convert_coordinates_to_square(position[0], position[1])
        if new_square := self.is_move_possible((position[0], position[1]), capture, True):
            if (self.fen.is_white_an_active_colour() is piece.active_colour_white and new_square ==
                    self.fen.available_en_passant):
                default_return = f"{original_square}{new_square}"
        return default_return
