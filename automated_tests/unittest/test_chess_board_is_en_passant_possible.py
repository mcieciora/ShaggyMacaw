from pytest import mark

from src.chess_board import ChessBoard
from src.piece import Pawn, PieceMove


@mark.unittest
def test__unittest__chess_board__is_en_passant_possible__en_passant_possible_and_available():
    original_fen = "r1b1r1k1/1pb3p1/2nq1p2/2N3P1/pPRp3p/3N3P/P1Q1PPB1/5RK1 b - b3 4 23"
    test_object = ChessBoard(original_fen)
    pawn = Pawn("p", (0, 3))
    actual_data = test_object.is_move_legal(pawn, (1, -1), PieceMove.CAPTURE)
    assert actual_data.is_en_passant is True, f"Expected: True, actual: {actual_data}"
    assert actual_data.target_square == "b3", f"Expected: axb3, actual: {actual_data}"


@mark.unittest
def test__unittest__chess_board__is_en_passant_possible__en_passant_not_possible_and_available():
    original_fen = "r1b1r1k1/1pb3p1/2nq1p2/2N3P1/pPRp3p/3N3P/P1Q1PPB1/5RK1 b - b3 4 23"
    test_object = ChessBoard(original_fen)
    pawn = Pawn("p", (3, 4))
    actual_data = test_object.is_move_legal(pawn, (1, 1), PieceMove.MOVE_OR_CAPTURE)
    assert actual_data.is_en_passant is False, f"Expected: False, actual: {actual_data}"


@mark.unittest
def test__unittest__chess_board__is_en_passant_possible__en_passant_not_possible_and_not_available():
    original_fen = "r1b1r1k1/1pb3p1/2nq1p2/2N3P1/pPRp3p/3N3P/P1Q1PPB1/5RK1 b - - 4 23"
    test_object = ChessBoard(original_fen)
    pawn = Pawn("p", (3, 4))
    actual_data = test_object.is_move_legal(pawn, (1, -1), PieceMove.MOVE_OR_CAPTURE)
    assert actual_data.is_en_passant is False, f"Expected: False, actual: {actual_data}"
