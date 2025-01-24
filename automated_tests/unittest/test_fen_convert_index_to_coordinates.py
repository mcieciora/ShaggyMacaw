from pytest import mark

from src.fen import Fen


@mark.unittest
def test__unittest__fen__convert_index_to_coordinates():
    original_fen = "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1"
    expected_data_dict = {
        # 0: (0, 0),
        7: (0, 7),
        8: (1, 0),
        18: (2, 2),
        21: (2, 5),
        28: (3, 4),
        46: (5, 6),
        55: (6, 7),
        58: (7, 2),
        63: (7, 7)
    }
    test_object = Fen(original_fen)
    for test_data, expected_data in expected_data_dict.items():
        actual_data = test_object.convert_index_to_coordinates(test_data)
        assert actual_data == expected_data, f"Failed on {test_data}, expected: {expected_data}, actual: {actual_data}"
