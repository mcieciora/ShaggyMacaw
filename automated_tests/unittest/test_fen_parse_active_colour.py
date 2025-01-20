from pytest import mark, raises

from src.fen import Fen, WrongActiveColourValue


@mark.unittest
def test__fen__parse_active_colour__white_colour():
    """Cover tc-0"""
    original_fen = "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1"
    test_object = Fen(original_fen)
    test_data = test_object.parse_active_colour("w")
    assert test_data is True, f"Expected: True, actual: {test_data}"


@mark.unittest
def test__fen__parse_active_colour__black_colour():
    """Cover tc-0"""
    original_fen = "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR b KQkq - 0 1"
    test_object = Fen(original_fen)
    test_data = test_object.parse_active_colour("b")
    assert test_data is False, f"Expected: False, actual: {test_data}"


@mark.unittest
def test__fen__parse_active_colour__wrong_active_colour():
    """Cover tc-0"""
    original_fen = "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR x KQkq - 0 1"
    test_object = Fen(original_fen)

    with raises(WrongActiveColourValue):
        test_object.parse_active_colour("x")
