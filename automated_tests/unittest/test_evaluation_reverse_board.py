from pytest import mark

from src.chess_board import ChessBoard
from src.evaluation import Evaluation
from src.piece import PieceType


@mark.unittest
def test__unittest__evaluation__reverse_board():
    original_fen = "r1b1r1k1/1pb3p1/2nq1p2/2N3P1/pPRp3p/3N3P/P1Q1PPB1/5RK1 b - b3 4 23"
    expected_data = [10, 15, 25, 26, 34, 20, 17, 25]
    chess_board = ChessBoard(original_fen)
    test_object = Evaluation(chess_board)
    actual_data = test_object.reverse_position(PieceType.BISHOP)[3]
    assert actual_data == expected_data, f"Expected: {expected_data}, actual: {actual_data}"
