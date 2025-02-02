from pytest import mark, raises

from src.fen import Fen, WrongActiveColourValue


@mark.unittest
def test__unittest__fen__parse_active_colour__white_colour():
    original_fen = "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1"
    test_object = Fen(original_fen)
    actual_data = test_object.parse_active_colour("w")
    assert actual_data is True, f"Expected: True, actual: {actual_data}"


@mark.unittest
def test__unittest__fen__parse_active_colour__black_colour():
    original_fen = "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR b KQkq - 0 1"
    test_object = Fen(original_fen)
    actual_data = test_object.parse_active_colour("b")
    assert actual_data is False, f"Expected: False, actual: {actual_data}"


@mark.unittest
def test__unittest__fen__parse_active_colour__true():
    original_fen = "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1"
    test_object = Fen(original_fen)
    actual_data = test_object.parse_active_colour(True)
    assert actual_data == "w", f"Expected: w, actual: {actual_data}"


@mark.unittest
def test__unittest__fen__parse_active_colour__false():
    original_fen = "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR b KQkq - 0 1"
    test_object = Fen(original_fen)
    actual_data = test_object.parse_active_colour(False)
    assert actual_data == "b", f"Expected: b, actual: {actual_data}"


@mark.unittest
def test__unittest__fen__parse_active_colour__wrong_active_colour():
    original_fen = "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1"
    test_object = Fen(original_fen)

    with raises(WrongActiveColourValue):
        test_object.parse_active_colour("x")
