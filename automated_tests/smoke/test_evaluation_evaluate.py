from pytest import mark

from src.chess_board import ChessBoard
from src.evaluation import Evaluation


test_data_dict = {
    "test_resource_1": {
        "fen": "8/P7/5k2/5B2/6Pp/1P3K1P/8/8 b - - 4 23",
        "pieces_value_map": {
            True: 711,
            False: 101
        },
        "position_value_map": {
            True: 61,
            False: -60
        }
    }
}


def get_parametrized_test_set():
    parametrized_test_set_list = [(test_key, test_data) for test_key, test_data in test_data_dict.items()]
    return parametrized_test_set_list


@mark.smoke
@mark.parametrize("test_key,test_data", get_parametrized_test_set(), ids=test_data_dict.keys())
def test__smoke__evaluation__evaluate(test_key, test_data):
    chess_board = ChessBoard(test_data["fen"])
    test_object = Evaluation(chess_board)
    pieces_value_map, position_value_map = test_object.evaluate(return_values_as_map=True)
    for active_colour in [True, False]:
        expected_value = test_data["pieces_value_map"][active_colour]
        assert pieces_value_map[active_colour] == expected_value, (f"Expected: {expected_value}, "
                                                                   f"actual: {pieces_value_map[active_colour]}")
        expected_value = test_data["position_value_map"][active_colour]
        assert position_value_map[active_colour] == expected_value, (f"Expected: {expected_value}, "
                                                                     f"actual: {position_value_map[active_colour]}")
