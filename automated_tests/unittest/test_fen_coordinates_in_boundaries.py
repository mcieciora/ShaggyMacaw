from pytest import mark

from src.fen import Fen


@mark.unittest
def test__unittest__fen__coordinates_in_boundaries():
    original_fen = "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1"
    expected_data_dict = {
        (0, 0): True,
        (0, 7): True,
        (7, 0): True,
        (7, 7): True,
        (2, 5): True,
        (4, 9): False,
        (4, 8): False,
        (4, 7): True,
        (6, 2): True,
        (7, 6): True,
        (-1, 4): False,
        (-2, 9): False
    }
    test_object = Fen(original_fen)
    for test_data, expected_data in expected_data_dict.items():
        actual_data = test_object.coordinates_in_boundaries(test_data[0], test_data[1])
        assert actual_data == expected_data, f"Failed on {test_data}, expected: {expected_data}, actual: {actual_data}"
