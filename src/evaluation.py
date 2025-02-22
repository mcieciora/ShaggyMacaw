from copy import deepcopy
from src.piece import PieceType


pieces_value = {
    PieceType.PAWN: 100,
    PieceType.KNIGHT: 300,
    PieceType.BISHOP: 310,
    PieceType.ROOK: 500,
    PieceType.QUEEN: 900,
    PieceType.KING: 1,
}

position = {
    PieceType.PAWN: [
        [0, 0, 0, 0, 0, 0, 0, 0],
        [-31, 8, -7, -37, -36, -14, 3, -31],
        [-22, 9, 5, -11, -10, -2, 3, -19],
        [-26, 3, 10, 9, 6, 1, 0, -23],
        [-17, 16, -2, 15, 14, 0, 15, -13],
        [7, 29, 21, 44, 40, 31, 44, 7],
        [78, 83, 86, 73, 102, 82, 85, 90],
        [0, 0, 0, 0, 0, 0, 0, 0],
    ],
    PieceType.KNIGHT: [
        [-74, -23, -26, -24, -19, -35, -22, -69],
        [-23, -15, 2, 0, 2, 0, -23, -20],
        [-18, 10, 13, 22, 18, 15, 11, -14],
        [-1, 5, 31, 21, 22, 35, 2, 0],
        [24, 24, 45, 37, 33, 41, 25, 17],
        [10, 67, 1, 74, 73, 27, 62, -2],
        [-3, -6, 100, -36, 4, 62, -4, -14],
        [-66, -53, -75, -75, -10, -55, -58, -70],
    ],
    PieceType.BISHOP: [
        [-7, 2, -15, -12, -14, -15, -10, -10],
        [19, 20, 11, 6, 7, 6, 20, 16],
        [14, 25, 24, 15, 8, 25, 20, 15],
        [13, 10, 17, 23, 17, 16, 0, 7],
        [25, 17, 20, 34, 26, 25, 15, 10],
        [-9, 39, -32, 41, 52, -10, 28, -14],
        [-11, 20, 35, -42, -39, 31, 2, -22],
        [-59, -78, -82, -76, -23, -107, -37, -50],
    ],
    PieceType.ROOK: [
        [-30, -24, -18, 5, -2, -18, -31, -32],
        [-53, -38, -31, -26, -29, -43, -44, -53],
        [-42, -28, -42, -25, -25, -35, -26, -46],
        [-28, -35, -16, -21, -13, -29, -46, -30],
        [0, 5, 16, 13, 18, -4, -9, -6],
        [19, 35, 28, 33, 45, 27, 25, 15],
        [55, 29, 56, 67, 55, 62, 34, 60],
        [35, 29, 33, 4, 37, 33, 56, 50],
    ],
    PieceType.QUEEN: [
        [-39, -30, -31, -13, -31, -36, -34, -42],
        [-36, -18, 0, -19, -15, -15, -21, -38],
        [-30, -6, -13, -11, -16, -11, -16, -27],
        [-14, -15, -2, -5, -1, -10, -20, -22],
        [1, -16, 22, 17, 25, 20, -13, -6],
        [-2, 43, 32, 60, 72, 63, 43, 2],
        [14, 32, 60, -10, 20, 76, 57, 24],
        [6, 1, -8, -104, 69, 24, 88, 26],
    ],
    PieceType.KING: [
        [17, 30, -3, -14, 6, -1, 40, 18],
        [-4, 3, -14, -50, -57, -18, 13, 4],
        [-47, -42, -43, -79, -64, -32, -29, -32],
        [-55, -43, -52, -28, -51, -47, -8, -50],
        [-55, 50, 11, -4, -19, 13, 0, -49],
        [-62, 12, -57, 44, -67, 28, 37, -31],
        [-32, 10, 55, 56, 56, 55, 10, 3],
        [4, 54, 47, -99, -99, 60, 83, -62],
    ],
}


class Evaluation:
    """Chess board position evaluation class."""

    def __init__(self, chess_board):
        self.chess_board = chess_board

    def evaluate(self, return_values_as_map=False):
        """Evaluate total pieces value and position value."""
        pieces_value_map = {True: 0, False: 0}
        position_value_map = {True: 0, False: 0}
        all_pieces = sum(self.chess_board.fen.board_setup, [])
        for piece in all_pieces:
            if piece is not PieceType.EMPTY:
                pieces_value_map[piece.active_colour_white] += pieces_value[
                    piece.piece_type
                ]
                position_value_map[piece.active_colour_white] += (
                    self.get_position_value(piece)
                )

        if return_values_as_map:
            return pieces_value_map, position_value_map
        evaluation = (pieces_value_map[True] + position_value_map[True]) / (
            pieces_value_map[False] + position_value_map[False]
        )
        return round(evaluation, 9)

    def get_position_value(self, piece):
        """Get piece value based on square position map."""
        position_by_type = position[piece.piece_type]
        if piece.active_colour_white:
            return position_by_type[piece.position[1]][piece.position[0]]
        reversed_board = self.reverse_position(piece.piece_type)
        return reversed_board[piece.position[1]][piece.position[0]]

    @staticmethod
    def reverse_position(piece_type):
        """Reverse position perspective."""
        reversed_ranks = list(reversed(position[piece_type]))
        return [list(reversed(rank)) for rank in reversed_ranks]

    def get_best_move(self, n):
        """Get best move in position."""
        return_sequence = []
        for move_number in range(n):
            _chess_board_deep_copy = deepcopy(self.chess_board)
            active_colour = self.chess_board.fen.active_colour
            all_moves = self.chess_board.generate_all_possible_moves()

            _temp_evaluations = {}

            for move in all_moves:
                if move.active_colour is active_colour:
                    self.chess_board.move_piece(move)
                    _temp_evaluations[move] = self.evaluate(return_values_as_map=False)

            best_move = max(_temp_evaluations, key=_temp_evaluations.get)
            return_sequence.append(best_move)
            self.chess_board = _chess_board_deep_copy
            self.chess_board.move_piece(best_move)
            self.chess_board.fen.current_fen = self.chess_board.fen.regenerate_fen()
        return return_sequence
