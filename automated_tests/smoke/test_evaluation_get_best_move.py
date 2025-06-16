from glob import glob
from pytest import mark

from src.chess_board import ChessBoard
from src.evaluation import Evaluation


def get_parametrized_test_set(test_file):
    parametrized_test_set_list = []
    full_test_file_path = glob(f"automated_tests/test_data/{test_file}")[0]
    with open(full_test_file_path, mode="r", encoding="utf-8") as test_fen_file:
        for index, line in enumerate(test_fen_file.readlines()):
            board = ChessBoard(line)
            parametrized_test_set_list.append(board)
    return parametrized_test_set_list


@mark.smoke
@mark.parametrize("test_board", get_parametrized_test_set("fen_0"),
                  ids=[f"test_resource_{index}" for index in range(1, 11)])
def test__smoke__evaluation__get_best_move(test_board):
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
