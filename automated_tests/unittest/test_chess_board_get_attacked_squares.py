from pytest import mark

from src.chess_board import ChessBoard


@mark.unittest
def test__unittest__chess_board__get_attacked_squares():
    expected_data = ["a3", "b3", "c3", "d3", "e3", "f3", "g3", "h3"]
    original_fen = "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR b KQkq - 0 0"
    test_object = ChessBoard(original_fen)
    test_object.generate_all_possible_moves()
    actual_data = test_object.get_attacked_squares(True)
    assert actual_data == expected_data, f"Expected: {expected_data}, actual: {actual_data}"
