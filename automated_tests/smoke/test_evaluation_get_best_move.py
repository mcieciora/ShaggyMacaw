from glob import glob
from pytest import mark

from src.chess_board import ChessBoard
from src.evaluation import Evaluation


test_data_dict = {
    "test_resource_1": {
        "best_moves": []
    },
    "test_resource_2": {
        "best_moves": []
    },
    "test_resource_3": {
        "best_moves": []
    },
    "test_resource_4": {
        "best_moves": []
    },
    "test_resource_5": {
        "best_moves": []
    },
    "test_resource_6": {
        "best_moves": []
    },
    "test_resource_7": {
        "best_moves": []
    },
    "test_resource_8": {
        "best_moves": []
    },
    "test_resource_9": {
        "best_moves": []
    },
    "test_resource_10": {
        "best_moves": []
    },
}


def get_parametrized_test_set(test_file):
    parametrized_test_set_list = []
    full_test_file_path = glob(f"automated_tests/test_data/{test_file}")[0]
    with open(full_test_file_path, mode="r", encoding="utf-8") as test_fen_file:
        for index, line in enumerate(test_fen_file.readlines()):
            board = ChessBoard(line)
            test_object = Evaluation(board)
            actual_data = test_object.get_best_move(n=1)
            parametrized_test_set_list.append((actual_data, test_data_dict[f"test_resource_{index+1}"]))
    return parametrized_test_set_list


@mark.smoke
@mark.parametrize("test_data,expected_output", get_parametrized_test_set("fen_0"), ids=test_data_dict.keys())
def test__smoke__evaluation__get_best_move(test_data, expected_output):
    for test_key, test_value in test_data.__dict__.items():
        assert str(test_value) in expected_output["best_moves"], (f"Expected: {test_data} not in "
                                                                 f"{expected_output['best_moves']}")
