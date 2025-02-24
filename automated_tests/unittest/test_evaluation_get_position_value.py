from pytest import mark

from src.chess_board import ChessBoard
from src.evaluation import Evaluation
from src.piece import Piece


@mark.unittest
def test__unittest__evaluation__get_position_value__white_piece():
    board = ChessBoard("r1b1r1k1/1pb2pp1/2nq4/2N5/p1Rp2Pp/3N3P/PPQ1PPB1/5RK1 w - - 4 23")
    test_object = Evaluation(board)

    white_piece = Piece("K", (6, 0))
    actual_data = test_object.get_position_value(white_piece)
    assert actual_data == 40, f"Expected: 40, actual: {actual_data}"


@mark.unittest
def test__unittest__evaluation__get_position_value__black_piece():
    board = ChessBoard("r1b1r1k1/1pb2pp1/2nq4/2N5/p1Rp2Pp/3N3P/PPQ1PPB1/5RK1 w - - 4 23")
    test_object = Evaluation(board)

    black_piece = Piece("k", (6, 7))
    actual_data = test_object.get_position_value(black_piece)
    assert actual_data == 30, f"Expected: 30, actual: {actual_data}"
