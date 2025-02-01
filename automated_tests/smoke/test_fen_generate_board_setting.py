from glob import glob
from pytest import mark

from src.fen import Fen

test_data_dict = {
    "test_resource_1": {
        "white_move": False,
        "castling_rights": "-",
        "available_en_passant": "-",
        "half_move_clock": 0,
        "full_move_number": 8
    },
    "test_resource_2": {
        "white_move": False,
        "castling_rights": "-",
        "available_en_passant": "-",
        "half_move_clock": 1,
        "full_move_number": 13
    },
    "test_resource_3": {
        "white_move": True,
        "castling_rights": "-",
        "available_en_passant": "-",
        "half_move_clock": 0,
        "full_move_number": 18
    },
    "test_resource_4": {
        "white_move": True,
        "castling_rights": "-",
        "available_en_passant": "g6",
        "half_move_clock": 0,
        "full_move_number": 18
    },
    "test_resource_5": {
        "white_move": True,
        "castling_rights": "-",
        "available_en_passant": "-",
        "half_move_clock": 0,
        "full_move_number": 31
    },
    "test_resource_6": {
        "white_move": True,
        "castling_rights": "KQkq",
        "available_en_passant": "-",
        "half_move_clock": 0,
        "full_move_number": 4
    },
    "test_resource_7": {
        "white_move": True,
        "castling_rights": "KQkq",
        "available_en_passant": "-",
        "half_move_clock": 2,
        "full_move_number": 9
    },
    "test_resource_8": {
        "white_move": True,
        "castling_rights": "-",
        "available_en_passant": "-",
        "half_move_clock": 14,
        "full_move_number": 15
    },
    "test_resource_9": {
        "white_move": False,
        "castling_rights": "-",
        "available_en_passant": "-",
        "half_move_clock": 3,
        "full_move_number": 21
    },
    "test_resource_10": {
        "white_move": False,
        "castling_rights": "KQkq",
        "available_en_passant": "e3",
        "half_move_clock": 0,
        "full_move_number": 1
    },
}


def get_parametrized_test_set(test_file):
    parametrized_test_set_list = []
    full_test_file_path = glob(f"automated_tests/test_data/{test_file}")[0]
    with open(full_test_file_path, mode="r", encoding="utf-8") as test_fen_file:
        for index, line in enumerate(test_fen_file.readlines()):
            test_board = Fen(line.replace("\n", ""))
            parametrized_test_set_list.append((test_board, test_data_dict[f"test_resource_{index+1}"]))
    return parametrized_test_set_list


@mark.smoke
def test__smoke__fen__generate_board_setting():
    original_fen = "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1"
    test_object = Fen(original_fen)
    for attribute in ["board_setup", "active_colour", "castling_rights", "available_en_passant", "half_move_clock",
                      "full_move_number"]:
        assert hasattr(test_object, attribute), f"Expected: attribute {attribute} not found"


@mark.smoke
@mark.parametrize("test_data,expected_output", get_parametrized_test_set("fen_0"), ids=test_data_dict.keys())
def test__smoke__fen__generate_chess_board_from_fen(test_data, expected_output):
    for test_key, test_value in test_data.__dict__.items():
        if test_key in expected_output:
            assert test_value == expected_output[test_key], (f"Failed on {test_key}, "
                                                             f"expected: {expected_output[test_key]}, "
                                                             f"actual: {test_value}")
