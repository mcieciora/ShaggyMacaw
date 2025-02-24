from glob import glob
from pytest import mark

from src.chess_board import ChessBoard
from src.evaluation import Evaluation


test_data_dict = {
    "test_resource_1": {
        "expected_sequence_colour": [False, True, False]
    },
    "test_resource_2": {
        "expected_sequence_colour": [False, True, False]
    },
    "test_resource_3": {
        "expected_sequence_colour": [True, False, True]
    },
    "test_resource_4": {
        "expected_sequence_colour": [True, False, True]
    },
    "test_resource_5": {
        "expected_sequence_colour": [True, False, True]
    },
    "test_resource_6": {
        "expected_sequence_colour": [True, False, True]
    },
    "test_resource_7": {
        "expected_sequence_colour": [True, False, True]
    },
    "test_resource_8": {
        "expected_sequence_colour": [True, False, True]
    },
    "test_resource_9": {
        "expected_sequence_colour": [False, True, False]
    },
    "test_resource_10": {
        "expected_sequence_colour": [False, True, False]
    }
}


def get_parametrized_test_set(test_file):
    parametrized_test_set_list = []
    full_test_file_path = glob(f"automated_tests/test_data/{test_file}")[0]
    with open(full_test_file_path, mode="r", encoding="utf-8") as test_fen_file:
        for index, line in enumerate(test_fen_file.readlines()):
            board = ChessBoard(line)
            test_object = Evaluation(board)
            actual_data = test_object.get_best_move(n=3)
            parametrized_test_set_list.append((actual_data, test_data_dict[f"test_resource_{index+1}"]))
    return parametrized_test_set_list


@mark.smoke
@mark.parametrize("test_data,expected_output", get_parametrized_test_set("fen_0"), ids=test_data_dict.keys())
def test__smoke__evaluation__get_best_move(test_data, expected_output):
    actual_data = [move.active_colour for move in test_data]
    expected_data = expected_output["expected_sequence_colour"]
    assert actual_data == expected_data, f"Expected: {expected_data}, actual: {actual_data}"
