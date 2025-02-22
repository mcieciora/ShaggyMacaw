from pytest import mark

from src.chess_board import ChessBoard
from src.evaluation import Evaluation


@mark.unittest
def test__unittest__evaluation__get_best_move():
    board = ChessBoard("r1b1r1k1/1pb2pp1/2nq4/2N5/p1Rp2Pp/3N3P/PPQ1PPB1/5RK1 w - - 4 23")
    test_object = Evaluation(board)
    actual_data = test_object.get_best_move(n=3)
    assert type(actual_data) is list, f"Expected: type: Move, actual: {type(actual_data)}"
    assert len(actual_data) == 3, f"Expected: 3, actual: {len(actual_data)}"
