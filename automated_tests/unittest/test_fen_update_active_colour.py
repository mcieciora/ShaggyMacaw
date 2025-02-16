from pytest import mark

from src.fen import Fen


@mark.unittest
def test__unittest__fen__update_active_colour():
    original_fen = "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 2 1"
    test_object = Fen(original_fen)
    test_object.update_active_colour()
    actual_data = test_object.active_colour
    assert actual_data is False, f"Expected: False, actual: {actual_data}"
