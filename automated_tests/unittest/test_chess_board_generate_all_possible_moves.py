from pytest import mark

from src.chess_board import ChessBoard


@mark.unittest
def test__unittest__chess_board__generate_all_possible_moves():
    original_fen = "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR b KQkq - 0 0"
    expected_data = ["b1c3", "b1a3", "g1h3", "g1f3", "a2a3", "a2a4", "b2b3", "b2b4", "c2c3", "c2c4", "d2d3", "d2d4",
                     "e2e3", "e2e4", "f2f3", "f2f4", "g2g3", "g2g4", "h2h3", "h2h4", "a7a6", "a7a5", "b7b6", "b7b5",
                     "c7c6", "c7c5", "d7d6", "d7d5", "e7e6", "e7e5", "f7f6", "f7f5", "g7g6", "g7g5", "h7h6", "h7h5",
                     "b8c6", "b8a6", "g8h6", "g8f6"]
    test_object = ChessBoard(original_fen)
    actual_data = test_object.generate_all_possible_moves()
    assert [str(result) for result in actual_data] == expected_data, f"Expected: {expected_data}, actual: {actual_data}"
