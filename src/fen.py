from itertools import product

class Fen:
    """

    """
    def __init__(self, fen):
        """

        """
        self.original_fen = fen
        self.board_squares = self.generate_board_squares()


    def generate_board_setup(self):
        """

        """
        parsed_fen = {}
        split_fen = self.original_fen.split()

        parsed_fen["board_setup"] = self.parse_board_setup(split_fen[0])
        parsed_fen["active_colour"] = self.parse_active_colour(split_fen[1])
        parsed_fen["castling_rights"] = self.parse_castling_rights(split_fen[2])
        parsed_fen["available_en_passant"] = self.parse_en_passant(split_fen[3])
        parsed_fen["half_move_clock"] = self.parse_half_move(split_fen[4])
        parsed_fen["full_move_number"] = self.parse_full_move(split_fen[5])

        for key, value in parsed_fen:
            setattr(self, key, value)

    @staticmethod
    def generate_board_squares():
        """

        """
        files = ["a", "b", "c", "d", "e", "f", "g", "h"]
        rows = list(range(1, 9))
        product_list = list(product(files, rows))
        return [''.join(map(str, x)) for x in product_list]

    @staticmethod
    def parse_board_setup(fen):
        """

        """
        return_board = []
        rows = fen.split("/")
        if rows_number := (len(rows)) != 8:
            raise WrongBoardSize(f"Number of rows is incorrect. Expected is 8, but got: {rows_number}")
        for index, row in enumerate(rows):
            temp_row = []
            for square in row:
                if square.isdigit():
                    temp_row.append(square)
                else:
                    [temp_row.append('') for _ in range(eval(square))]
            if row_size := (len(temp_row)) != 8:
                raise WrongBoardSize(f"{index} row size if incorrect. Expected is 8, but got: {row_size}")
            return_board.append(temp_row)
        return return_board

    @staticmethod
    def parse_active_colour(active_colour):
        """

        """
        if active_colour not in ["w", "b"]:
            raise WrongActiveColourValue(f"Active colour has incorrect value: {active_colour}, expected: w/b")
        return True if active_colour == "w" else False

    @staticmethod
    def parse_castling_rights(castling_rights):
        """

        """
        if not castling_rights in ["-", "KQkq", "Kkq", "Qkq", "KQk", "Kk", "Qk", "KQq", "Kq", "Qq"]:
            raise WrongCastlingRights(f"Castling rights have wrong value: {castling_rights}")
        return castling_rights

    def parse_en_passant(self, en_passant_square):
        """

        """
        if not en_passant_square in self.board_squares:
            raise WrongEnPassantValue(f"En passant square has wrong value: {en_passant_square}")
        return en_passant_square


    @staticmethod
    def parse_half_move(half_move_value):
        """

        """
        try:
            return int(half_move_value)
        except ValueError:
            raise NotIntegerHalfMoveValue(f"Half move value is not an integer: {half_move_value}")

    @staticmethod
    def parse_full_move(full_move_value):
        """

        """
        try:
            return int(full_move_value)
        except ValueError:
            raise NotIntegerFullMoveValue(f"Full move value is not an integer: {full_move_value}")

class WrongBoardSize(Exception):
    pass

class WrongActiveColourValue(Exception):
    pass

class WrongEnPassantValue(Exception):
    pass

class WrongCastlingRights(Exception):
    pass

class NotIntegerHalfMoveValue(Exception):
    pass

class NotIntegerFullMoveValue(Exception):
    pass
