from src.piece import create_piece
from src.piece import PieceType


class Fen:
    """FEN notation parser and verification class."""

    def __init__(self, fen):
        """Initialize FEN object."""
        self.original_fen = fen
        self.board_squares = self.generate_board_squares()

        split_fen = self.original_fen.split()

        self.board_setup = self.parse_board_setup(split_fen[0])
        self.active_colour = self.parse_active_colour(split_fen[1])
        self.castling_rights = self.parse_castling_rights(split_fen[2])
        self.available_en_passant = self.parse_en_passant(split_fen[3])
        self.half_move_clock = self.parse_half_move(split_fen[4])
        self.full_move_number = self.parse_full_move(split_fen[5])

    def get_square_value(self, square):
        """Get pawn or piece value from given square."""
        files = ["a", "b", "c", "d", "e", "f", "g", "h"]
        try:
            file, rank = square[0], int(square[1]) - 1
            return self.board_setup[rank][files.index(file)]
        except (ValueError, IndexError) as exc:
            raise NoSquareInBoard(f"Square {square} not found in board.") from exc

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
        files = ["a", "b", "c", "d", "e", "f", "g", "h"]
        return f"{files[x]}{y + 1}"

    @staticmethod
    def coordinates_in_boundaries(x, y):
        """Check if coordinates y, x are in chess board boundaries."""
        return 0 <= x < 8 and 0 <= y < 8

    @staticmethod
    def generate_board_squares():
        """Generate list of possible chess board squares."""
        generated_squares = []
        files, ranks = ["a", "b", "c", "d", "e", "f", "g", "h"], list(range(1, 9))
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
