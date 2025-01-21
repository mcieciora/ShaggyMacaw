from pytest import mark, raises

from src.fen import Fen, NoSquareInBoard


@mark.unittest
def test__unittest__fen__convert_square_to_index():
    original_fen = "r1bqk1nr/1p3pbp/p1np2p1/4p3/2P1P3/2NB4/PP3PPP/RNBQK2R w KQkq - 2 9"
    expected_data_dict = {
        "d1": 59,
        "a1": 56,
        "f2": 53,
        "h3": 47,
        "a4": 32,
        "e5": 28,
        "b6": 17,
        "g6": 22,
        "b7": 9,
        "h8": 7
    }
    test_object = Fen(original_fen)
    for test_data, expected_data in expected_data_dict.items():
        actual_data = test_object.convert_square_to_index(test_data)
        assert actual_data == expected_data, f"Failed on {test_data}, expected: {expected_data}, actual: {actual_data}"


@mark.unittest
def test__unittest__fen__convert_square_to_index__no_square_in_board():
    original_fen = "r1bqk1nr/1p3pbp/p1np2p1/4p3/2P1P3/2NB4/PP3PPP/RNBQK2R w KQkq - 2 9"
    test_object = Fen(original_fen)
    with raises(NoSquareInBoard):
        test_object.convert_square_to_index("x1")
