from pytest import mark

from src.chess_board import ChessBoard
from src.piece import Piece


@mark.unittest
def test__unittest__chess_board__generate_piece_moves__knight():
    original_fen = "4r2k/pp3p1p/1bn5/5p2/3pPP1q/P7/1P1QP1BP/2R3RK b - - 0 31"
    expected_data = ["c6e7", "c6d8", "c6e5", "c6b8", "c6a5", "c6b4"]
    test_object = ChessBoard(original_fen)
    piece = Piece("n", (2, 5))
    actual_data = test_object.generate_piece_moves(piece, not_continuous_movement=True)
    assert [str(result) for result in actual_data] == expected_data, f"Expected: {expected_data}, actual: {actual_data}"
