from glob import glob
from pytest import mark

from src.fen import Fen
from automated_tests.test_resources.fen_0 import expected_data as fen_0_data


def get_parametrized_test_set(test_file, expected_data):
    parametrized_test_set_list = []
    full_test_file_path = glob(f"automated_tests/test_data/{test_file}")[0]
    with (open(full_test_file_path, mode="r") as test_fen_file):
        for index, line in enumerate(test_fen_file.readlines()):
            test_board = Fen(line.replace("\n", ""))
            parametrized_test_set_list.append((test_board, expected_data[f"test_resource_{index+1}"]))
    return parametrized_test_set_list


@mark.smoke
def test__fen__generate_board_setting():
    original_fen = "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1"
    test_object = Fen(original_fen)
    test_object.generate_board_setting()
    for attribute in ["board_setup", "active_colour", "castling_rights", "available_en_passant", "half_move_clock",
                      "full_move_number"]:
        assert hasattr(test_object, attribute), f"Expected: attribute {attribute} not found"


@mark.smoke
def test__smoke__generate_chess_board_from_fen():
    test_set = get_parametrized_test_set("fen_0", fen_0_data)
    for test_set_value in test_set:
        test_data, expected_output = test_set_value[0], test_set_value[1]
        for test_key, test_value in test_data.__dict__.items():
            if test_key in expected_output:
                assert test_value == expected_output[test_key], f"{test_key} failed on difference"
