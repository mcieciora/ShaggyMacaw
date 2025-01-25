from pytest import mark

from src.chess_board import ChessBoard


@mark.unittest
def test__unittest__chess_board__is_move_possible():
    original_fen = "r1b1r1k1/1pb3p1/2nq1p2/2N3P1/pPRp3p/3N3P/P1Q1PPB1/5RK1 b - b3 4 23"
    test_object = ChessBoard(original_fen)
    actual_data = test_object.is_move_possible((1, 3), (0, 1), True)
    assert actual_data == "b5", f"Expected: gxf6, actual: {actual_data}"

@mark.unittest
def test__unittest__chess_board__is_move_possible__out_of_boundaries():
    original_fen = "r1b1r1k1/1pb3p1/2nq1p2/2N3P1/pPRp3p/3N3P/P1Q1PPB1/5RK1 b - b3 4 23"
    test_object = ChessBoard(original_fen)
    actual_data = test_object.is_move_possible((7, 2), (1, 0), True)
    assert actual_data is False, f"Expected: False, actual: {actual_data}"

@mark.unittest
def test__unittest__chess_board__is_move_possible__square_not_empty():
    original_fen = "r1b1r1k1/1pb3p1/2nq1p2/2N3P1/pPRp3p/3N3P/P1Q1PPB1/5RK1 b - b3 4 23"
    test_object = ChessBoard(original_fen)
    actual_data = test_object.is_move_possible((7, 2), (0, 1), True)
    assert actual_data is False, f"Expected: False, actual: {actual_data}"
