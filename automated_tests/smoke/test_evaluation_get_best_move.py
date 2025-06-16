from copy import deepcopy
from glob import glob
from pytest import mark

from src.chess_board import ChessBoard
from src.evaluation import Evaluation


test_data_dict = {
    "test_resource_1": {
        "expected_sequence_colour": [False, True, False],
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
            parametrized_test_set_list.append((board, test_data_dict[f"test_resource_{index+1}"]))
    return parametrized_test_set_list


@mark.smoke
@mark.parametrize("test_board,expected_output", get_parametrized_test_set("fen_0"), ids=test_data_dict.keys())
def test__smoke__evaluation__get_best_move(test_board, expected_output):
    starting_fen, starting_colour = test_board.fen.current_fen, test_board.fen.active_colour
    evaluation = Evaluation(test_board)
    actual_data = evaluation.get_best_move(5)
    assert evaluation.chess_board.fen.current_fen == starting_fen, "Starting and final fen does not match."
    for move in actual_data:
        assert move.active_colour is starting_colour, "Expected sequence colour does not match pattern."
        starting_colour = not starting_colour
        original_square_value = evaluation.chess_board.fen.get_square_value(move.original_square)
        assert move.piece_value == original_square_value.value, "Original square is not occupied by declared piece."
        evaluation.chess_board.move_piece(move)
