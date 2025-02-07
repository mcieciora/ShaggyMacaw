from pytest import mark

from src.chess_board import ChessBoard
from src.evaluation import Evaluation


@mark.unittest
def test__unittest__evaluation__evaluate():
    board = ChessBoard("r1b1r1k1/1pb2pp1/2nq4/2N5/p1Rp2Pp/3N3P/PPQ1PPB1/5RK1 w - - 4 23")
    test_object = Evaluation(board)
    pieces_value_map, position_value_map = test_object.evaluate()

    for active_colour in [True, False]:
        assert pieces_value_map[active_colour] != 0, f"Expected not: 0, actual: {pieces_value_map[active_colour]}"
        assert position_value_map[active_colour] != 0, f"Expected not: 0, actual: {position_value_map[active_colour]}"
