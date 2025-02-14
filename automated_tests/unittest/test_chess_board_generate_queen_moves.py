from pytest import mark

from src.chess_board import ChessBoard
from src.piece import Piece


@mark.unittest
def test__unittest__chess_board__generate_piece_moves__queen():
    original_fen = "4r2k/pp3p1p/1bn5/5p2/3pPP1q/P7/1P1QP1BP/2R3RK b - - 0 31"
    expected_data = ["h4g5", "h4f6", "h4e7", "h4d8", "h4g3", "h4f2", "h4e1", "h4h5", "h4h6", "h4h3", "h4h2", "h4g4",
                     "h4f4"]
    test_object = ChessBoard(original_fen)
    piece = Piece("q", (7, 3))
    actual_data = test_object.generate_piece_moves(piece)
    assert [str(result) for result in actual_data] == expected_data, f"Expected: {expected_data}, actual: {actual_data}"
