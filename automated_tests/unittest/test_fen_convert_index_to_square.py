from pytest import mark, raises

from src.fen import Fen, NoSquareInBoard


@mark.unittest
def test__unittest__fen__convert_index_to_square():
    original_fen = "r1bqk1nr/1p3pbp/p1np2p1/4p3/2P1P3/2NB4/PP3PPP/RNBQK2R w KQkq - 2 9"
    expected_data_dict = {
        0: "a1",
        3: "d1",
        13: "f2",
        21: "f3",
        28: "e4",
        33: "b5",
        47: "h6",
        53: "f7",
        59: "d8",
        63: "h8"
    }
    test_object = Fen(original_fen)
    for test_data, expected_data in expected_data_dict.items():
        actual_data = test_object.convert_index_to_square(test_data)
        assert actual_data == expected_data, f"Failed on {test_data}, expected: {expected_data}, actual: {actual_data}"


@mark.unittest
def test__unittest__fen__convert_index_to_square__no_square_in_board():
    original_fen = "r1bqk1nr/1p3pbp/p1np2p1/4p3/2P1P3/2NB4/PP3PPP/RNBQK2R w KQkq - 2 9"
    test_object = Fen(original_fen)
    with raises(NoSquareInBoard):
        test_object.convert_index_to_square(64)
