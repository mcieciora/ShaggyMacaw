from copy import deepcopy
from pytest import mark

from src.chess_board import ChessBoard
from src.evaluation import Evaluation
from src.move import Move


@mark.unittest
def test__unittest__evaluation__get_best_move():
    board = ChessBoard("r1b1r1k1/1pb2pp1/2nq4/2N5/p1Rp2Pp/3N3P/PPQ1PPB1/5RK1 w - - 4 23")
    test_object = Evaluation(board)
    actual_data = test_object.get_best_move(n=1)
    assert type(actual_data) is Move, f"Expected: type: Move, actual: {type(actual_data)}"


@mark.unittest
def test__unittest__evaluation__get_best_move__no_board_change():
    board = ChessBoard("r1b1r1k1/1pb2pp1/2nq4/2N5/p1Rp2Pp/3N3P/PPQ1PPB1/5RK1 w - - 4 23")
    expected_board = deepcopy(board)
    test_object = Evaluation(board)
    actual_data = test_object.get_best_move(n=1)
    assert type(actual_data) is Move, f"Expected: type: Move, actual: {type(actual_data)}"
    assert test_object.chess_board == expected_board, f"Expected: {expected_board}, actual: {test_object.chess_board}"


@mark.unittest
def test__unittest__evaluation__get_best_move__move_piece():
    board = ChessBoard("r1b1r1k1/1pb2pp1/2nq4/2N5/p1Rp2Pp/3N3P/PPQ1PPB1/5RK1 w - - 4 23")
    expected_board = deepcopy(board)
    test_object = Evaluation(board)
    best_move = test_object.get_best_move(n=1)
    board.move_piece(best_move)
    assert test_object.chess_board != expected_board, f"Expected: {expected_board}, actual: {test_object.chess_board}"
