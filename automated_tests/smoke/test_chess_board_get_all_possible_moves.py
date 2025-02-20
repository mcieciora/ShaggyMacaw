from pytest import mark

from src.chess_board import ChessBoard

test_data_dict = {
    "test_resource_1": {
        "fen": "r1bqk1nr/1p3pbp/p1np2p1/4p3/2P1P3/2NB4/PP3PPP/RNBQK2R w KQkq - 2 9",
        "active_colour": True,
        "expected_result": {
            True: 39,
            False: 39
        }
    }
}


def get_parametrized_test_set():
    parametrized_test_set_list = []
    for test_key, test_data in test_data_dict.items():
        parametrized_test_set_list.append((test_key, test_data, test_data["expected_result"]))
    return parametrized_test_set_list


@mark.smoke
@mark.parametrize("test_key,test_data,expected_output", get_parametrized_test_set(), ids=test_data_dict.keys())
def test__smoke__chess_board__generate_all_possible_moves(test_key, test_data, expected_output):
    test_object = ChessBoard(test_data["fen"])
    for active_colour, expected_value in test_data['expected_result'].items():
        actual_data = [str(move) for move in test_object.generate_all_possible_moves()
                       if move.active_colour is active_colour]
        assert len(actual_data) == test_data['expected_result'][active_colour], \
            f"Expected: {test_data['expected_result']}, actual: {len(actual_data)}"
