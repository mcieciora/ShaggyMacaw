from pytest import mark

from src.chess_board import ChessBoard
from src.piece import Piece


@mark.unittest
def test__unittest__chess_board__generate_rook_moves__one_rook():
    original_fen = "4qk2/2r3bp/1p1pb1p1/p4r2/1nPPpn2/2NB3P/5NP1/R1BQK2R w KQ - 2 9"
    expected_data = ["a1a2", "a1a3", "a1a4", "a1a5", "a1b1"]
    test_object = ChessBoard(original_fen)
    piece = Piece("R", (0, 0))
    actual_data = test_object.generate_rook_moves(piece)
    assert actual_data == expected_data, f"Expected: {expected_data}, actual: {actual_data}"

    expected_data = ["h1h2", "h1g1", "h1f1"]
    piece = Piece("R", (7, 0))
    actual_data = test_object.generate_rook_moves(piece)
    assert actual_data == expected_data, f"Expected: {expected_data}, actual: {actual_data}"


@mark.unittest
def test__unittest__chess_board__generate_rook_moves__two_rooks():
    original_fen = "4qk2/2r3bp/1p1pb1p1/p4r2/1nPPpn2/2NB3P/5NP1/R1BQK2R w KQ - 2 9"
    expected_data = ["f5f6", "f5f7", "f5g5", "f5h5", "f5e5", "f5d5", "f5c5", "f5b5"]
    test_object = ChessBoard(original_fen)
    piece = Piece("r", (5, 4))
    actual_data = test_object.generate_rook_moves(piece)
    assert actual_data == expected_data, f"Expected: {expected_data}, actual: {actual_data}"

    expected_data = ["c7c8", "c7c6", "c7c5", "c7c4", "c7d7", "c7e7", "c7f7", "c7b7", "c7a7"]
    piece = Piece("r", (2, 6))
    actual_data = test_object.generate_rook_moves(piece)
    assert actual_data == expected_data, f"Expected: {expected_data}, actual: {actual_data}"
