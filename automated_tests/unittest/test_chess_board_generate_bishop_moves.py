from pytest import mark

from src.chess_board import ChessBoard
from src.piece import Piece


@mark.unittest
def test__unittest__chess_board__generate_piece_moves__bishop():
    original_fen = "4r2k/pp3p1p/1bn5/5p2/3pPP1q/P7/1P1QP1BP/2R3RK w - - 0 31"
    expected_data = ["b6c7", "b6d8", "b6c5", "b6a5"]
    test_object = ChessBoard(original_fen)
    piece = Piece("b", (1, 5))
    actual_data = test_object.generate_piece_moves(piece)
    assert actual_data == expected_data, f"Expected: {expected_data}, actual: {actual_data}"
