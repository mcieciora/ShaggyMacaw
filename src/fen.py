from src.piece import create_piece
from src.piece import Piece, PieceType


files = ["a", "b", "c", "d", "e", "f", "g", "h"]


class Fen:
    """FEN notation parser and verification class."""

    def __init__(self, fen):
        """Initialize FEN object."""
        self.original_fen = fen
        self.board_squares = self.generate_board_squares()
        self.current_fen = self.original_fen

        fen_list = self.original_fen.split()
        self.board_setup = self.parse_board_setup(fen_list[0])
        self.active_colour = self.parse_active_colour(fen_list[1])
        self.castling_rights = self.parse_castling_rights(fen_list[2])
        self.available_en_passant = self.parse_en_passant(fen_list[3])
        self.half_move_clock = self.parse_half_move(fen_list[4])
        self.full_move_number = self.parse_full_move(fen_list[5])

    @staticmethod
    def get_position_from_square(square):
        """Get piece position from square value."""
        try:
            return files.index(square[0]), int(square[1]) - 1
        except (ValueError, IndexError) as exc:
            raise NoSquareInBoard(f"Square {square} not found in board.") from exc

    def get_square_value(self, square):
        """Get pawn or piece value from given square."""
        x, y = self.get_position_from_square(square)
        return self.board_setup[y][x]

    def is_square_empty(self, square):
        """Return true if given square value is -."""
        return self.get_square_value(square) == PieceType.EMPTY

    def get_square_active_colour(self, square):
        """Get pawn's or piece's colour from given square."""
        square_value = self.get_square_value(square)
        if not self.is_square_empty(square):
            return square_value.active_colour_white
        raise SquareEmpty(f"{square} is empty.")

    def is_white_an_active_colour(self):
        """Check if white is and active colour."""
        return self.active_colour

    @staticmethod
    def convert_coordinates_to_square(x, y):
        """Convert x, y coordinates to square value."""
        return f"{files[x]}{y + 1}"

    @staticmethod
    def coordinates_in_boundaries(x, y):
        """Check if coordinates y, x are in chess board boundaries."""
        return 0 <= x < 8 and 0 <= y < 8

    @staticmethod
    def generate_board_squares():
        """Generate list of possible chess board squares."""
        generated_squares = []
        ranks = list(range(1, 9))
        for rank in ranks:
            for file in files:
                generated_squares.append(f"{file}{rank}")
        return generated_squares

    @staticmethod
    def parse_board_setup(fen):
        """Parse board setup and verify number of files and ranks."""
        return_board = []
        ranks = fen.split("/")
        ranks.reverse()
        if ranks_number := (len(ranks)) != 8:
            raise WrongBoardSize(
                f"Number of ranks is incorrect. Expected is 8, but got: {ranks_number}"
            )
        for rank_index, rank in enumerate(ranks):
            temporary_rank = []
            position_offset = 0
            for square_index, value in enumerate(rank):
                if value.isdigit():
                    temporary_rank.extend([create_piece(value)] * int(value))
                    real_normalized = int(value) - 1
                    position_offset += real_normalized
                else:
                    temporary_rank.append(
                        create_piece(
                            value, position=(square_index + position_offset, rank_index)
                        )
                    )
            return_board.append(temporary_rank)
            if (rank_size := len(temporary_rank)) != 8:
                raise WrongBoardSize(
                    f"{rank_index} rank size if incorrect. Expected is 8, but got: {rank_size}"
                )
        return return_board

    @staticmethod
    def parse_active_colour(active_colour):
        """Parse and verify active colours value."""
        if active_colour in ["w", "b"]:
            return active_colour == "w"
        if isinstance(active_colour, bool):
            return {True: "w", False: "b"}[active_colour]
        raise WrongActiveColourValue(
            f"Active colour has incorrect value: {active_colour}, "
            f"expected: w/b or True/False"
        )

    @staticmethod
    def parse_castling_rights(castling_rights):
        """Parse and verify castling rights value."""
        if castling_rights not in [
            "-",
            "KQkq",
            "Kkq",
            "Qkq",
            "KQk",
            "Kk",
            "Qk",
            "KQq",
            "Kq",
            "KQ",
            "Qq",
            "K",
            "Q",
            "k",
            "q",
        ]:
            raise WrongCastlingRights(
                f"Castling rights have wrong value: {castling_rights}"
            )
        return castling_rights

    def parse_en_passant(self, en_passant_square):
        """Parse and verify en passant value."""
        if en_passant_square not in self.board_squares and en_passant_square != "-":
            raise WrongEnPassantValue(
                f"En passant square has wrong value: {en_passant_square}"
            )
        return en_passant_square

    @staticmethod
    def parse_half_move(half_move_value):
        """Parse and verify half move value."""
        try:
            return int(half_move_value)
        except ValueError as exc:
            raise NotIntegerHalfMoveValue(
                f"Half move value is not an integer: {half_move_value}"
            ) from exc

    @staticmethod
    def parse_full_move(full_move_value):
        """Parse and verify full move value."""
        try:
            return int(full_move_value)
        except ValueError as exc:
            raise NotIntegerFullMoveValue(
                f"Full move value is not an integer: {full_move_value}"
            ) from exc

    def regenerate_fen(self):
        """Generate FEN from current configuration."""
        board = "/".join(
            [self.parse_rank_to_fen(rank) for rank in reversed(self.board_setup)]
        )

        return (
            f"{board} {self.parse_active_colour(self.active_colour)} "
            f"{self.castling_rights} {self.available_en_passant} {self.half_move_clock} {self.full_move_number}"
        )

    @staticmethod
    def parse_rank_to_fen(rank_list):
        """Parse given rank back to FEN notation."""
        return_list = []

        active_value = None
        for square in rank_list:
            try:
                if active_value[0] == square:
                    active_value = (square, active_value[1] + 1)
                else:
                    return_list.append(active_value)
                    active_value = (square, 1)
            except TypeError:
                active_value = (square, 1)
        if active_value:
            return_list.append(active_value)
        return "".join(
            [str(x[1]) if x[0] == PieceType.EMPTY else x[0].value for x in return_list]
        )

    def update_board_setup(self, move, original, target):
        """Update board setup."""
        original_x, original_y = original[0], original[1]
        target_x, target_y = target[0], target[1]
        if move.is_promotion:
            new_piece = Piece(
                move.promotion_piece, self.get_position_from_square(move.target_square)
            )
            self.board_setup[target_y][target_x] = new_piece

            self.board_setup[original_y][original_x] = PieceType.EMPTY
        elif move.is_castling:
            rook_original_x = 0 if target_x == 2 else 7
            rook_target_x = 3 if target_x == 2 else 5
            self.board_setup[original_y][rook_target_x] = self.board_setup[original_y][
                rook_original_x
            ]
            self.board_setup[original_y][rook_original_x] = PieceType.EMPTY
            self.board_setup[target_y][target_x] = self.board_setup[original_y][
                original_x
            ]
            self.board_setup[original_y][original_x] = PieceType.EMPTY
        elif move.is_en_passant:
            self.board_setup[target_y][target_x] = self.board_setup[original_y][
                original_x
            ]
            self.board_setup[original_y][target_x] = PieceType.EMPTY
            self.board_setup[original_y][original_x] = PieceType.EMPTY
        else:
            self.board_setup[target_y][target_x] = self.board_setup[original_y][
                original_x
            ]
            self.board_setup[original_y][original_x] = PieceType.EMPTY

    def update_clocks(self, move):
        """Update half move and full move clock."""
        if move.is_capture or move.is_promotion or move.is_en_passant:
            self.half_move_clock = 0
        elif self.full_move_number > 1:
            self.half_move_clock += 1
        if not self.active_colour:
            self.full_move_number += 1

    def update_active_colour(self):
        """Update active colour."""
        self.active_colour = not self.active_colour

    def update_castling_rights(self, move):
        """Update castling rights."""
        if move.piece_value in ["K", "k"] or move.is_castling:
            original_square = {
                "K": "e1",
                "k": "e8",
            }
            if move.original_square == original_square[move.piece_value]:
                replacement_value = {"K": "KQ", "k": "kq"}
                for value in replacement_value[move.piece_value]:
                    self.castling_rights = self.castling_rights.replace(value, "")
                    if self.castling_rights == "":
                        self.castling_rights = "-"

        if move.piece_value in ["R", "r"]:
            original_square = {
                "R": {"a1": "Q", "h1": "K"},
                "r": {"a8": "q", "h8": "k"},
            }
            if move.original_square in original_square[move.piece_value].keys():
                self.castling_rights = self.castling_rights.replace(
                    original_square[move.piece_value][move.original_square], ""
                )
                if self.castling_rights == "":
                    self.castling_rights = "-"

    def update_en_passant(self, move, target, original_y):
        """Update en passant possibilities."""
        target_x, target_y = target[0], target[1]
        if move.piece_value in ["P", "p"] and target_y - original_y == 2:
            self.available_en_passant = f"{files[target_x]}3"
        else:
            self.available_en_passant = "-"


class WrongBoardSize(Exception):
    """Raised when board file or ranks has wrong length."""


class WrongActiveColourValue(Exception):
    """Raised when active colour value is incorrect."""


class WrongEnPassantValue(Exception):
    """Raised when en passant value is incorrect."""


class WrongCastlingRights(Exception):
    """Raised when castling rights value is incorrect."""


class NotIntegerHalfMoveValue(Exception):
    """Raised when half move value is not integer."""


class NotIntegerFullMoveValue(Exception):
    """Raised when full move value is not integer."""


class NoSquareInBoard(Exception):
    """Raised when given square is not available in board."""


class SquareEmpty(Exception):
    """Raised when square checked for active colour is empty. Use with is_square_empty instead."""
