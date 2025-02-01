from pytest import mark, raises

from src.fen import Fen, NoSquareInBoard
from src.square_value import PieceValue


@mark.unittest
def test__unittest__fen__get_square_value():
    original_fen = "r1bqk1nr/1p3pbp/p1np2p1/4p3/2P1P3/2NB4/PP3PPP/RNBQK2R w KQkq - 2 9"
    expected_data_dict = {
        "c3": PieceValue.KNIGHT,
        "d1": PieceValue.QUEEN,
        "c6": PieceValue.KNIGHT,
        "e4": PieceValue.PAWN,
        "e5": PieceValue.PAWN,
        "a8": PieceValue.ROOK,
        "g7": PieceValue.BISHOP
    }
    test_object = Fen(original_fen)
    for test_data, expected_data in expected_data_dict.items():
        actual_data = test_object.get_square_value(test_data).piece_type
        assert actual_data == expected_data, f"Expected: {expected_data}, actual: {actual_data}"


@mark.unittest
def test__unittest__fen__get_square_value__no_square_in_board():
    original_fen = "r1bqk1nr/1p3pbp/p1np2p1/4p3/2P1P3/2NB4/PP3PPP/RNBQK2R w KQkq - 2 9"
    test_object = Fen(original_fen)
    with raises(NoSquareInBoard):
        test_object.get_square_value("x")
