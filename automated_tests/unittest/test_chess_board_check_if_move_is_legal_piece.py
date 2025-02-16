from pytest import mark

from src.chess_board import ChessBoard
from src.piece import Piece, PieceMove


@mark.unittest
def test__unittest__chess_board__check_if_move_is_legal__piece():
    original_fen = "r1b1r1k1/1pb3p1/2nq1p2/2N3P1/pPRp3p/3N3P/P1Q1PPB1/5RK1 b - b3 4 23"
    test_object = ChessBoard(original_fen)
    piece = Piece("Q", (2, 1))
    actual_data = test_object.check_if_move_is_legal(piece, (0, -1), PieceMove.MOVE_OR_CAPTURE)
    assert actual_data.target_square == "c1", f"Expected: c1, actual: {actual_data}"


@mark.unittest
def test__unittest__chess_board__check_if_move_is_legal__out_of_boundaries__piece():
    original_fen = "r1b1r1k1/1pb3p1/2nq1p2/2N3P1/pPRp3p/3N3P/P1Q1PPB1/5RK1 b - b3 4 23"
    test_object = ChessBoard(original_fen)
    piece = Piece("r", (0, 7))
    actual_data = test_object.check_if_move_is_legal(piece, (-1, 0), PieceMove.MOVE_OR_CAPTURE)
    assert actual_data.is_move_legal is False, f"Expected: False, actual: {actual_data}"


@mark.unittest
def test__unittest__chess_board__check_if_move_is_legal__square_not_empty__piece():
    original_fen = "r1b1r1k1/1pb3p1/2nq1p2/2N3P1/pPRp3p/3N3P/P1Q1PPB1/5RK1 b - b3 4 23"
    test_object = ChessBoard(original_fen)
    piece = Piece("B", (6, 1))
    actual_data = test_object.check_if_move_is_legal(piece, (1, 1), PieceMove.MOVE_OR_CAPTURE)
    assert actual_data.is_capture is False, f"Expected: False, actual: {actual_data}"


@mark.unittest
def test__unittest__chess_board__check_if_move_is_legal__same_colour_capture__piece():
    original_fen = "r1b1r1k1/1pb3p1/2nq1p2/2N3P1/pPRp3p/3N3P/P1Q1PPB1/5RK1 b - b3 4 23"
    test_object = ChessBoard(original_fen)
    piece = Piece("R", (2, 3))
    actual_data = test_object.check_if_move_is_legal(piece, (0, 1), PieceMove.MOVE_OR_CAPTURE)
    assert actual_data.is_capture is False, f"Expected: False, actual: {actual_data}"


@mark.unittest
def test__unittest__chess_board__check_if_move_is_legal__capture__piece():
    original_fen = "r1b1r1k1/1pb3p1/2nq1p2/2N3P1/pPRp3p/3N3P/P1Q1PPB1/5RK1 b - b3 4 23"
    test_object = ChessBoard(original_fen)
    piece = Piece("N", (2, 4))
    actual_data = test_object.check_if_move_is_legal(piece, (-1, 2), PieceMove.MOVE_OR_CAPTURE)
    assert actual_data.target_square == "b7", f"Expected: b7, actual: {actual_data}"
