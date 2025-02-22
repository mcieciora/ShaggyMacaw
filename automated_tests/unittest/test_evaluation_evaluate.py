from pytest import mark

from src.chess_board import ChessBoard
from src.evaluation import Evaluation


@mark.unittest
def test__unittest__evaluation__evaluate():
    board = ChessBoard("8/P7/5k2/5B2/6Pp/1P3K1P/8/8 b - - 4 23")
    test_object = Evaluation(board)
    actual_data = round(test_object.evaluate(), 2)
    assert actual_data == 18.83, f"Expected: 18.83, actual: {actual_data}"


@mark.unittest
def test__unittest__evaluation__evaluate__return_values_as_map():
    board = ChessBoard("r1b1r1k1/1pb2pp1/2nq4/2N5/p1Rp2Pp/3N3P/PPQ1PPB1/5RK1 w - - 4 23")
    test_object = Evaluation(board)
    pieces_value_map, position_value_map = test_object.evaluate(return_values_as_map=True)

    for active_colour in [True, False]:
        assert pieces_value_map[active_colour] != 0, f"Expected not: 0, actual: {pieces_value_map[active_colour]}"
        assert position_value_map[active_colour] != 0, f"Expected not: 0, actual: {position_value_map[active_colour]}"


@mark.unittest
def test__unittest__evaluation__evaluate__starting_position():
    board = ChessBoard("rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1")
    test_object = Evaluation(board)
    actual_data = round(test_object.evaluate(), 2)
    assert actual_data == 1.01, f"Expected: 1.01, actual: {actual_data}"


@mark.unittest
def test__unittest__evaluation__evaluate__starting_position_return_values_as_map():
    board = ChessBoard("rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1")
    test_object = Evaluation(board)
    pieces_value_map, position_value_map = test_object.evaluate(return_values_as_map=True)
    white_evaluation = pieces_value_map[True] + position_value_map[True]
    black_evaluation = pieces_value_map[False] + position_value_map[False]
    assert white_evaluation > black_evaluation, \
        f"White evaluation: {white_evaluation}; black evaluation: {black_evaluation}"
