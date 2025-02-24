from pytest import mark

from src.chess_board import ChessBoard


@mark.unittest
def test__unittest__chess_board__get_defended_pieces():
    expected_data = ["a2", "b1", "b2", "c1", "c2", "d1", "d2", "e1", "e2", "f1", "f2", "g1", "g2", "h2"]
    original_fen = "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR b KQkq - 0 0"
    test_object = ChessBoard(original_fen)
    test_object.generate_all_possible_moves()
    actual_data = test_object.get_defended_pieces(True)
    assert actual_data == expected_data, f"Expected: {expected_data}, actual: {actual_data}"
