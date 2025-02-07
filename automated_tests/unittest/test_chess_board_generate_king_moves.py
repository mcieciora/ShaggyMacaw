from pytest import mark

from src.chess_board import ChessBoard
from src.piece import Pawn


@mark.unittest
def test__unittest__chess_board__generate_king_moves():
    original_fen = "4r1k1/1p3pp1/2b5/3Bn3/3p1NPp/7P/PP2P3/5R1K w - - 1 34"
    expected_data = ["h1h2", "h1g1", "h1g2"]
    test_object = ChessBoard(original_fen)
    pawn = Pawn("K", (7, 0))
    actual_data = test_object.generate_king_moves(pawn)
    assert actual_data == expected_data, f"Expected: {expected_data}, actual: {actual_data}"
