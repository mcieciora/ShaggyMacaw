from pytest import mark

from src.chess_board import ChessBoard
from src.piece import Piece


@mark.unittest
def test__unittest__chess_board__generate_piece_moves__rook():
    original_fen = "4qk2/2r3bp/1p1pb1p1/p4r2/1nPPpn2/2NB3P/5NP1/R1BQK2R w KQ - 2 9"
    expected_data = ["a1a2", "a1a3", "a1a4", "a1a5", "a1b1"]
    test_object = ChessBoard(original_fen)
    piece = Piece("R", (0, 0))
    actual_data = test_object.generate_piece_moves(piece)
    assert actual_data == expected_data, f"Expected: {expected_data}, actual: {actual_data}"

    expected_data = ["h1h2", "h1g1", "h1f1"]
    piece = Piece("R", (7, 0))
    actual_data = test_object.generate_piece_moves(piece)
    assert actual_data == expected_data, f"Expected: {expected_data}, actual: {actual_data}"
