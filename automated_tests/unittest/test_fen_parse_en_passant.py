from pytest import mark, raises

from src.fen import Fen, WrongEnPassantValue


@mark.unittest
def test__fen__parse_en_passant():
    original_fen = "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq a1 0 1"
    test_object = Fen(original_fen)
    test_data = test_object.parse_en_passant("a1")
    assert test_data == "a1", f"Expected: a1, actual: {test_data}"


@mark.unittest
def test__fen__parse_en_passant__no_square():
    original_fen = "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1"
    test_object = Fen(original_fen)
    test_data = test_object.parse_en_passant("-")
    assert test_data == "-", f"Expected: -, actual: {test_data}"


@mark.unittest
def test__fen__parse_en_passant__wrong_en_passant_square():
    original_fen = "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq xX 0 1"
    test_object = Fen(original_fen)
    with raises(WrongEnPassantValue):
        test_object.parse_en_passant("xX")
