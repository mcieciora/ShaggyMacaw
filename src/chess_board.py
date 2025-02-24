from copy import deepcopy

from src.fen import Fen
from src.piece import PieceType, PieceMove
from src.move import Move


class ChessBoard:
    """Moves generation and chess board management class."""

    def __init__(self, fen):
        """Initialize ChessBoard object."""
        self.fen = Fen(fen)
        self.defended_pieces = {True: [], False: []}
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
                elif piece.piece_type in [
                    PieceType.ROOK,
                    PieceType.BISHOP,
                    PieceType.QUEEN,
                ]:
                    all_possible_moves.extend(self.generate_piece_moves(piece))
                elif piece.piece_type is PieceType.KNIGHT:
                    all_possible_moves.extend(
                        self.generate_piece_moves(piece, not_continuous_movement=True)
                    )
                elif piece.piece_type is PieceType.KING:
                    kings[piece.active_colour_white] = piece
                else:
                    raise UnknownPieceType(f"{type(piece)} not supported.")
        all_possible_moves.extend(self.generate_kings_moves(kings))
        return all_possible_moves

    def generate_pawn_moves(self, piece):
        """Generate pawn moves."""
        available_squares = []
        original_square = self.fen.convert_coordinates_to_square(
            piece.position[0], piece.position[1]
        )
        for move_type, movements in piece.movement_pattern.items():
            for movement in movements:
                move = self.check_if_move_is_legal(piece, movement, move_type)
                if move.is_move_legal:
                    move.original_square = original_square
                    move.is_promotion = piece.is_pawn_next_move_promotion()
                    if move.is_promotion:
                        for promotion_move in ["Q", "R", "N", "B"]:
                            temp_move = deepcopy(move)
                            temp_move.promotion_piece = (
                                promotion_move
                                if piece.active_colour_white
                                else promotion_move.lower()
                            )
                            available_squares.append(temp_move)
                    else:
                        available_squares.append(move)
                elif move_type is PieceMove.MOVE:
                    break
        return available_squares

    def generate_piece_moves(self, piece, not_continuous_movement=False):
        """Generate piece moves."""
        available_squares = []
        original_square = self.fen.convert_coordinates_to_square(
            piece.position[0], piece.position[1]
        )
        for movement in piece.movement_pattern:
            for multiplier in range(1, 8):
                multiplied_movement = tuple([multiplier * x for x in movement])
                move = self.check_if_move_is_legal(
                    piece, multiplied_movement, PieceMove.MOVE_OR_CAPTURE
                )
                if move.is_move_legal:
                    move.original_square = original_square
                    available_squares.append(move)
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
                move = self.check_if_move_is_legal(
                    king,
                    movement,
                    PieceMove.MOVE_OR_CAPTURE,
                    extend_attacked_squares=False,
                )
                if (
                    move.is_move_legal
                    and move.target_square
                    not in self.attacked_squares_map[not king.active_colour_white]
                    and move.target_square
                    not in self.defended_pieces[not king.active_colour_white]
                ):
                    move.original_square = square_value
                    possible_shared_squares_dict[king.active_colour_white][
                        move.target_square
                    ] = move
            for castling_right, squares in castling_rights[
                king.active_colour_white
            ].items():
                if castling_right in self.fen.castling_rights:
                    squares_empty = [
                        self.fen.get_square_value(square) is PieceType.EMPTY
                        for square in squares
                    ]
                    if (
                        all(squares_empty)
                        and squares[-1]
                        not in self.attacked_squares_map[not king.active_colour_white]
                    ):
                        castling_move = Move(
                            original_square=square_value,
                            target_square=squares[-1],
                            is_move_legal=True,
                            is_castling=True,
                            active_colour=king.active_colour_white,
                            piece_value=king.value,
                        )
                        possible_shared_squares_dict[king.active_colour_white][
                            squares[-1]
                        ] = castling_move
        return self.mask_colliding_moves(possible_shared_squares_dict)

    def mask_colliding_moves(self, moves_dict):
        """Get only unique moves out of connected kings moves list."""
        return_list = []
        for active_colour, moves in moves_dict.items():
            for move in list(
                set(moves_dict[active_colour]) - set(moves_dict[not active_colour])
            ):
                return_list.append(moves[move])
                self.attacked_squares_map[moves[move].active_colour].append(
                    moves[move].target_square
                )
        return return_list

    def get_attacked_squares(self, active_colour):
        """Return unique and sorted attacked squares list for selected active colour."""
        unique_list = list(set(self.attacked_squares_map[active_colour]))
        return sorted(unique_list)

    def get_defended_pieces(self, active_colour):
        """Return unique and sorted list of defended pieces of given colour."""
        unique_list = list(set(self.defended_pieces[active_colour]))
        return sorted(unique_list)

    def check_if_move_is_legal(
        self, piece, movement, move_type, extend_attacked_squares=True
    ):
        """Calculate new position, verify if square is in board and return Move object."""
        move = Move()
        x = piece.position[0] + movement[0]
        y = piece.position[1] + movement[1]
        if self.fen.coordinates_in_boundaries(x, y):
            square = self.fen.convert_coordinates_to_square(x, y)
            is_empty = self.fen.is_square_empty(square)
            move.active_colour = piece.active_colour_white
            if is_empty and move_type in [PieceMove.MOVE, PieceMove.MOVE_OR_CAPTURE]:
                move.is_move_legal = True
                move.target_square = square
                if move_type is PieceMove.MOVE_OR_CAPTURE and extend_attacked_squares:
                    self.attacked_squares_map[piece.active_colour_white].append(square)
            if is_empty and move_type is PieceMove.CAPTURE and extend_attacked_squares:
                if (
                    self.fen.is_white_an_active_colour() is piece.active_colour_white
                    and square == self.fen.available_en_passant
                ):
                    move.is_move_legal = True
                    move.target_square = square
                    move.is_en_passant = True
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
                    move.target_square = square
                    move.is_capture = True
                    if extend_attacked_squares:
                        self.attacked_squares_map[piece.active_colour_white].append(
                            square
                        )
                else:
                    self.defended_pieces[piece.active_colour_white].append(square)
        return move

    def move_piece(self, move):
        """Move piece and update current FEN value."""
        original_x, original_y = self.fen.get_position_from_square(move.original_square)
        target_x, target_y = self.fen.get_position_from_square(move.target_square)

        self.fen.update_board_setup(
            move, (original_x, original_y), (target_x, target_y)
        )
        self.fen.update_castling_rights(move)
        self.fen.update_en_passant(move, (target_x, target_y), original_y)
        self.fen.update_clocks(move)
        self.fen.update_active_colour()


class UnknownPieceType(Exception):
    """Raised when square parsed by get_all_possible_moves function is not known for logic."""
