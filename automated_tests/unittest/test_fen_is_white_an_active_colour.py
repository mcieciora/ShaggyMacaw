from pytest import mark

from src.fen import Fen


@mark.unittest
def test__unittest__fen__is_white_an_active_colour__white_active():
    original_fen = "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 2"
    test_object = Fen(original_fen)
    actual_data = test_object.is_white_an_active_colour()
    assert actual_data is True, f"Expected: True, actual: {actual_data}"


@mark.unittest
def test__unittest__fen__is_white_an_active_colour__black_active():
    original_fen = "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR b KQkq - 0 2"
    test_object = Fen(original_fen)
    actual_data = test_object.is_white_an_active_colour()
    assert actual_data is False, f"Expected: False, actual: {actual_data}"
