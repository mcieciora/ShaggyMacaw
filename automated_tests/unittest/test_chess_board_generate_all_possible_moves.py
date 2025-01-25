from pytest import mark

from src.chess_board import ChessBoard


@mark.unittest
def test__unittest__chess_board__generate_all_possible_moves():
    original_fen = "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR b KQkq - 0 0"
    test_object = ChessBoard(original_fen)
    actual_data = len(test_object.generate_all_possible_moves())
    assert actual_data == 32, f"Expected: 20, actual: {actual_data}"
