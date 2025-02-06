from pytest import mark

from src.fen import Fen


@mark.unittest
def test__unittest__fen__regenerate_fen():
    original_fen = "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 2 1"
    test_object = Fen(original_fen)
    actual_data = test_object.regenerate_fen()
    assert actual_data == original_fen, f"Expected: {original_fen}, actual: {actual_data}"
