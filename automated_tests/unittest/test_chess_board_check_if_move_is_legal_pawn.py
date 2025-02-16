from pytest import mark

from src.chess_board import ChessBoard
from src.piece import Pawn, PieceMove


@mark.unittest
def test__unittest__chess_board__check_if_move_is_legal__pawn():
    original_fen = "r1b1r1k1/1pb3p1/2nq1p2/2N3P1/pPRp3p/3N3P/P1Q1PPB1/5RK1 b - b3 4 23"
    test_object = ChessBoard(original_fen)
    pawn = Pawn("P", (1, 3))
    actual_data = test_object.check_if_move_is_legal(pawn, (0, 1), PieceMove.MOVE)
    assert actual_data.target_square == "b5", f"Expected: b5, actual: {actual_data}"


@mark.unittest
def test__unittest__chess_board__check_if_move_is_legal__out_of_boundaries__pawn():
    original_fen = "r1b1r1k1/1pb3p1/2nq1p2/2N3P1/pPRp3p/3N3P/P1Q1PPB1/5RK1 b - b3 4 23"
    test_object = ChessBoard(original_fen)
    pawn = Pawn("p", (0, 3))
    actual_data = test_object.check_if_move_is_legal(pawn, (-1, 0), PieceMove.MOVE)
    assert actual_data.is_move_legal is False, f"Expected: False, actual: {actual_data}"


@mark.unittest
def test__unittest__chess_board__check_if_move_is_legal__square_not_empty__pawn():
    original_fen = "r1b1r1k1/1pb3p1/2nq1p2/2N3P1/pPRp3p/3N3P/P1Q1PPB1/5RK1 b - b3 4 23"
    test_object = ChessBoard(original_fen)
    pawn = Pawn("P", (7, 2))
    actual_data = test_object.check_if_move_is_legal(pawn, (0, 1), PieceMove.MOVE)
    assert actual_data.is_en_passant is False, f"Expected: False, actual: {actual_data}"


@mark.unittest
def test__unittest__chess_board__check_if_move_is_legal__no_capture__pawn():
    original_fen = "r1b1r1k1/1pb3p1/2nq1p2/2N3P1/pPRp3p/3N3P/P1Q1PPB1/5RK1 b - b3 4 23"
    test_object = ChessBoard(original_fen)
    pawn = Pawn("P", (0, 1))
    actual_data = test_object.check_if_move_is_legal(pawn, (1, 1), PieceMove.CAPTURE)
    assert actual_data.is_capture is False, f"Expected: False, actual: {actual_data}"


@mark.unittest
def test__unittest__chess_board__check_if_move_is_legal__same_colour_capture__pawn():
    original_fen = "r1b1r1k1/1pb3p1/2nq1p2/2N3P1/pPRp3p/3N3P/P1Q1PPB1/5RK1 b - b3 4 23"
    test_object = ChessBoard(original_fen)
    pawn = Pawn("P", (1, 3))
    actual_data = test_object.check_if_move_is_legal(pawn, (1, 1), PieceMove.CAPTURE)
    assert actual_data.is_capture is False, f"Expected: False, actual: {actual_data}"


@mark.unittest
def test__unittest__chess_board__check_if_move_is_legal__capture__pawn():
    original_fen = "r1b1r1k1/1pb3p1/2nq1p2/2N3P1/pPRp3p/3N3P/P1Q1PPB1/5RK1 b - b3 4 23"
    test_object = ChessBoard(original_fen)
    pawn = Pawn("P", (6, 4))
    actual_data = test_object.check_if_move_is_legal(pawn, (-1, 1), PieceMove.CAPTURE)
    assert actual_data.target_square == "f6", f"Expected: f6, actual: {actual_data}"
