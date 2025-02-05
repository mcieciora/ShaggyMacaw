from src.fen import Fen
from src.piece import PieceType, PieceMove, Move


class ChessBoard:
    """Moves generation and chess board management class."""

    def __init__(self, fen):
        """Initialize ChessBoard object."""
        self.fen = Fen(fen)
        self.attacked_squares_map = {True: [], False: []}

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
                elif piece.piece_type is PieceType.KNIGHT:
                    all_possible_moves.extend(
                        self.generate_piece_moves(piece, not_continuous_movement=True)
                    )
                else:
                    pass
        return all_possible_moves

    def generate_pawn_moves(self, piece):
        """Generate pawn moves."""
        available_squares = []
        for movement in piece.movement_pattern:
            move = self.is_move_legal(piece, movement, PieceMove.MOVE)
            if piece.is_pawn_next_move_promotion() and move.is_move_legal:
                available_squares.extend(
                    [
                        f"{move.square}={promotion_move}"
                        for promotion_move in ["Q", "R", "N", "B"]
                    ]
                )
            elif move.is_move_legal:
                square_value = self.fen.convert_coordinates_to_square(
                    piece.position[0], piece.position[1]
                )
                available_squares.append(f"{square_value}{move.square}")
            else:
                break
        for capture in piece.capture_pattern:
            move = self.is_move_legal(piece, capture, PieceMove.CAPTURE)
            original_square = self.fen.convert_coordinates_to_square(
                piece.position[0], piece.position[1]
            )
            if piece.is_pawn_next_move_promotion() and move.is_move_legal:
                available_squares.extend(
                    [
                        f"{original_square}{move.square}={promotion_move}"
                        for promotion_move in ["Q", "R", "N", "B"]
                    ]
                )
            elif move.is_capture:
                available_squares.append(f"{original_square}{move.square}")
            if new_square := self.is_en_passant_possible(
                piece.position, capture, piece
            ):
                available_squares.append(new_square)
        return available_squares

    def generate_piece_moves(self, piece, not_continuous_movement=False):
        """Generate rook moves."""
        available_squares = []
        square_value = self.fen.convert_coordinates_to_square(
            piece.position[0], piece.position[1]
        )
        for movement in piece.movement_pattern:
            for multiplier in range(1, 8):
                multiplied_movement = tuple([multiplier * x for x in movement])
                move = self.is_move_legal(
                    piece, multiplied_movement, PieceMove.MOVE_OR_CAPTURE
                )
                if move.is_move_legal:
                    available_squares.append(f"{square_value}{move.square}")
                    if move.is_capture:
                        break
                else:
                    break
                if not_continuous_movement:
                    break
        return available_squares

    def get_attacked_squares(self, active_colour):
        """Return unique and sorted attacked squares list for selected active colour."""
        unique_list = list(set(self.attacked_squares_map[active_colour]))
        return sorted(unique_list)

    def is_move_legal(self, piece, movement, move_type):
        """Calculate new position, verify if square is in board and return Move object."""
        move = Move()
        x = piece.position[0] + movement[0]
        y = piece.position[1] + movement[1]
        if self.fen.coordinates_in_boundaries(x, y):
            square = self.fen.convert_coordinates_to_square(x, y)
            is_empty = self.fen.is_square_empty(square)
            if is_empty and move_type in [PieceMove.MOVE, PieceMove.MOVE_OR_CAPTURE]:
                move.is_move_legal = True
                move.square = square
                if move_type is PieceMove.MOVE_OR_CAPTURE:
                    self.attacked_squares_map[piece.active_colour_white].append(square)
            if is_empty and move_type is PieceMove.CAPTURE:
                self.attacked_squares_map[piece.active_colour_white].append(square)
            if not is_empty and move_type in [
                PieceMove.CAPTURE,
                PieceMove.MOVE_OR_CAPTURE,
            ]:
                if (
                    self.fen.get_square_active_colour(square)
                    is not piece.active_colour_white
                ):
                    move.is_move_legal = True
                    move.square = square
                    move.is_capture = True
                    self.attacked_squares_map[piece.active_colour_white].append(square)
        return move

    def is_en_passant_possible(self, position, capture, piece):
        """Verify if move is possible and check if square is occupied by opposite colour piece."""
        default_return = False
        original_square = self.fen.convert_coordinates_to_square(
            position[0], position[1]
        )
        move = self.is_move_legal(piece, capture, PieceMove.MOVE)
        if move.is_move_legal:
            if (
                self.fen.is_white_an_active_colour() is piece.active_colour_white
                and move.square == self.fen.available_en_passant
            ):
                default_return = f"{original_square}{move.square}"
        return default_return
