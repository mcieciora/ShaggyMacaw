from pytest import mark

from src.chess_board import ChessBoard
from src.piece import Pawn


@mark.unittest
def test__unittest__chess_board__check_capture_square():
    original_fen = "r1b1r1k1/1pb3p1/2nq1p2/2N3P1/pPRp3p/3N3P/P1Q1PPB1/5RK1 b - b3 4 23"
    test_object = ChessBoard(original_fen)
    pawn = Pawn("P", (6, 4))
    actual_data = test_object.check_capture_square(pawn, (-1, 1))
    assert actual_data == "g5f6", f"Expected: g5f6, actual: {actual_data}"


@mark.unittest
def test__unittest__chess_board__check_capture_square__no_capture():
    original_fen = "r1b1r1k1/1pb3p1/2nq1p2/2N3P1/pPRp3p/3N3P/P1Q1PPB1/5RK1 b - b3 4 23"
    test_object = ChessBoard(original_fen)
    pawn = Pawn("P", (0, 1))
    actual_data = test_object.check_capture_square(pawn, (1, 1))
    assert actual_data is False, f"Expected: False, actual: {actual_data}"


@mark.unittest
def test__unittest__chess_board__check_capture_square__same_colour_capture():
    original_fen = "r1b1r1k1/1pb3p1/2nq1p2/2N3P1/pPRp3p/3N3P/P1Q1PPB1/5RK1 b - b3 4 23"
    test_object = ChessBoard(original_fen)
    pawn = Pawn("P", (1, 3))
    actual_data = test_object.check_capture_square(pawn, (1, 1))
    assert actual_data is False, f"Expected: False, actual: {actual_data}"
