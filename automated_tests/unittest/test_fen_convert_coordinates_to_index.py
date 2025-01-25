from pytest import mark

from src.fen import Fen


@mark.unittest
def test__unittest__fen__convert_index_to_coordinates():
    original_fen = "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1"
    expected_data_dict = {
        (0, 0): 0,
        (7, 0): 7,
        (0, 1): 8,
        (2, 2): 18,
        (5, 2): 21,
        (4, 3): 28,
        (6, 5): 46,
        (7, 6): 55,
        (2, 7): 58,
        (7, 7): 63
    }
    test_object = Fen(original_fen)
    for test_data, expected_data in expected_data_dict.items():
        actual_data = test_object.convert_coordinates_to_index(test_data[0], test_data[1])
        assert actual_data == expected_data, f"Failed on {test_data}, expected: {expected_data}, actual: {actual_data}"
