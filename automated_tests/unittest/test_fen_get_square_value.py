from pytest import mark, raises

from src.fen import Fen, NoSquareInBoard


@mark.unittest
def test__unittest__fen__get_square_value():
    original_fen = "r1bqk1nr/1p3pbp/p1np2p1/4p3/2P1P3/2NB4/PP3PPP/RNBQK2R w KQkq - 2 9"
    expected_data_dict = {
        "c3": "N",
        "d1": "Q",
        "c6": "n",
        "e4": "P",
        "e5": "p",
        "a8": "r",
        "g7": "b"
    }
    test_object = Fen(original_fen)
    test_object.generate_board_setting()
    for test_data, expected_data in expected_data_dict.items():
        actual_data = test_object.get_square_value(test_data)
        assert actual_data == expected_data, f"Expected: {expected_data}, actual: {actual_data}"


@mark.unittest
def test__unittest__fen__get_square_value__no_square_in_board():
    original_fen = "r1bqk1nr/1p3pbp/p1np2p1/4p3/2P1P3/2NB4/PP3PPP/RNBQK2R w KQkq - 2 9"
    test_object = Fen(original_fen)
    test_object.generate_board_setting()
    with raises(NoSquareInBoard):
        test_object.get_square_value("x")
