from pytest import mark

from src.chess_board import ChessBoard


test_data_dict = {
    "test_resource_1": {
        "fen": "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR b KQkq - 0 0",
        "expected_result": {
            True: ["a3", "b3", "c3", "d3", "e3", "f3", "g3", "h3"],
            False: ["a6", "b6", "c6", "d6", "e6", "f6", "g6", "h6"]
        }
    },
    # "test_resource_2": {
    #     "fen": "4qk2/2r3bp/1p1pb1p1/p4r2/1nPPpn2/2NB3P/5NP1/R1BQK2R w KQ - 2 9",
    #     "expected_result": {
    #         True: [],
    #         False: []
    #     }
    # }
}


def get_parametrized_test_set():
    parametrized_test_set_list = []
    for test_key, test_data in test_data_dict.items():
        parametrized_test_set_list.append((test_key, test_data, test_data["expected_result"]))
    return parametrized_test_set_list


@mark.smoke
@mark.parametrize("test_key,test_data,expected_output", get_parametrized_test_set(), ids=test_data_dict.keys())
def test__smoke__chess_board__get_attacked_squares(test_key, test_data, expected_output):
    test_object = ChessBoard(test_data["fen"])
    test_object.generate_all_possible_moves()
    actual_result = sorted(test_object.get_attacked_squares(True))
    assert actual_result == test_data["expected_result"][True], (f"Failed on {test_key}, expected: "
                                                           f"{test_data['expected_result']}, actual: "
                                                           f"{actual_result}")

    actual_result = sorted(test_object.get_attacked_squares(False))
    assert actual_result == test_data["expected_result"][False], (f"Failed on {test_key}, expected: "
                                                           f"{test_data['expected_result']}, actual: "
                                                           f"{actual_result}")
