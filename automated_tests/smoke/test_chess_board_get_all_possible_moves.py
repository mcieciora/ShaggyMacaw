from glob import glob
from pytest import mark

from src.chess_board import ChessBoard

test_data_dict = {
    "test_resource_1": {
        True: 41,
        False: 31
    },
    "test_resource_2": {
        True: 42,
        False: 39
    },
    "test_resource_3": {
        True: 43,
        False: 40
    },
    "test_resource_4": {
        True: 37,
        False: 42
    },
    "test_resource_5": {
        True: 35,
        False: 20
    },
    "test_resource_6": {
        True: 37,
        False: 25
    },
    "test_resource_7": {
        True: 39,
        False: 39
    },
    "test_resource_8": {
        True: 48,
        False: 32
    },
    "test_resource_9": {
        True: 43,
        False: 35
    },
    "test_resource_10": {
        True: 30,
        False: 20
    }
}


def get_parametrized_test_set(test_file):
    parametrized_test_set_list = []
    full_test_file_path = glob(f"automated_tests/test_data/{test_file}")[0]
    with open(full_test_file_path, mode="r", encoding="utf-8") as test_fen_file:
        for index, line in enumerate(test_fen_file.readlines()):
            test_object = ChessBoard(line)
            actual_data = {}
            for active_colour in [True, False]:
                actual_data[active_colour] = [str(move) for move in test_object.generate_all_possible_moves()
                               if move.active_colour is active_colour]
            parametrized_test_set_list.append((actual_data, test_data_dict[f"test_resource_{index+1}"]))
    return parametrized_test_set_list


@mark.smoke
@mark.parametrize("test_data,expected_output", get_parametrized_test_set("fen_0"), ids=test_data_dict.keys())
def test__smoke__chess_board__generate_all_possible_moves(test_data, expected_output):
    for active_colour in test_data:
        actual_data = len(test_data[active_colour])
        expected_data = expected_output[active_colour]
        assert actual_data == expected_data, \
            f"Expected: {expected_data}, actual: {actual_data}. Generated moves: {test_data[active_colour]}"
