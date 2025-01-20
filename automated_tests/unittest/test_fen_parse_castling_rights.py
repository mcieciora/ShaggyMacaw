from pytest import mark, raises

from src.fen import Fen, WrongCastlingRights


@mark.unittest
def test__fen__parse_castling_rights():
    """Cover tc-0"""
    original_fen = "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1"
    test_object = Fen(original_fen)
    for castling_right in ["-", "KQkq", "Kkq", "Qkq", "KQk", "Kk", "Qk", "KQq", "Kq", "Qq"]:
        test_data = test_object.parse_castling_rights(castling_right)
        assert test_data == castling_right, f"Expected: True, actual: {test_data}"


@mark.unittest
def test__fen__parse_castling_rights__wrong_castling_rights():
    """Cover tc-0"""
    original_fen = "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1"
    test_object = Fen(original_fen)
    with raises(WrongCastlingRights):
        test_object.parse_castling_rights("XX")
