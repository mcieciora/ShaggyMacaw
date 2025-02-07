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
        kings = {True: None, False: None}
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
                elif piece.piece_type is PieceType.KING:
                    kings[piece.active_colour_white] = piece
                else:
                    pass
        all_possible_moves.extend(self.generate_kings_moves(kings))
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
        """Generate piece moves."""
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

    def generate_kings_moves(self, kings):
        """Generate king moves."""
        possible_shared_squares_dict = {True: {}, False: {}}
        castling_rights = {
            True: {"K": ["f1", "g1"], "Q": ["d1", "b1", "c1"]},
            False: {"k": ["f8", "g8"], "q": ["d8", "b8", "c8"]},
        }
        for king in kings.values():
            square_value = self.fen.convert_coordinates_to_square(
                king.position[0], king.position[1]
            )
            for movement in king.movement_pattern:
                move = self.is_move_legal(
                    king,
                    movement,
                    PieceMove.MOVE_OR_CAPTURE,
                    extend_attacked_squares=False,
                )
                if (
                    move.is_move_legal
                    and move.square
                    not in self.attacked_squares_map[not king.active_colour_white]
                ):
                    possible_shared_squares_dict[king.active_colour_white][
                        move.square
                    ] = f"{square_value}{move.square}"
            for castling_right, squares in castling_rights[
                king.active_colour_white
            ].items():
                if castling_right in self.fen.castling_rights:
                    squares_empty = [
                        (
                            True
                            if self.fen.get_square_value(square) is PieceType.EMPTY
                            else False
                        )
                        for square in squares
                    ]
                    if (
                        all(squares_empty)
                        and squares[-1]
                        not in self.attacked_squares_map[not king.active_colour_white]
                    ):
                        possible_shared_squares_dict[king.active_colour_white][
                            squares[-1]
                        ] = f"{square_value}{squares[-1]}"
        return self.mask_colliding_moves(possible_shared_squares_dict)

    @staticmethod
    def mask_colliding_moves(moves_dict):
        """Get only unique moves out of connected kings moves list."""
        return_list = []
        for active_colour, moves in moves_dict.items():
            for move in list(
                set(moves_dict[active_colour]) - set(moves_dict[not active_colour])
            ):
                return_list.append(moves[move])
        return return_list

    def get_attacked_squares(self, active_colour):
        """Return unique and sorted attacked squares list for selected active colour."""
        unique_list = list(set(self.attacked_squares_map[active_colour]))
        return sorted(unique_list)

    def is_move_legal(self, piece, movement, move_type, extend_attacked_squares=True):
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
                if move_type is PieceMove.MOVE_OR_CAPTURE and extend_attacked_squares:
                    self.attacked_squares_map[piece.active_colour_white].append(square)
            if is_empty and move_type is PieceMove.CAPTURE and extend_attacked_squares:
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
                    if extend_attacked_squares:
                        self.attacked_squares_map[piece.active_colour_white].append(
                            square
                        )
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
