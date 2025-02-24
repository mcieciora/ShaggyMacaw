from pytest import mark

from src.chess_board import ChessBoard


test_data_dict = {
    "test_resource_1": {
        "fen": "6k1/7p/6p1/p3r3/6P1/7P/1B3K2/3R4 b - - 2 9",
        "expected_result": {
            True: ["a1", "a3", "b1", "c1", "c3", "d2", "d3", "d4", "d5", "d6", "d7", "d8", "e1", "e5", "f1", "f5",
                   "g1", "h1", "h5"],
            False: ["b4", "b5", "c5", "d5", "e1", "e2", "e3", "e4", "e6", "e7", "e8", "f5", "g5", "h5"]
        }
    },
    "test_resource_2": {
        "fen": "4qk2/2r3bp/1p1pb1p1/p4r2/1nPPpn2/2NB3P/5NP1/R1BQK2R w KQ - 2 9",
        "expected_result": {
            True: ["a2", "a3", "a4", "a5", "b1", "b2", "b3", "b5", "c2", "c5", "d2", "d5", "e2", "e3", "e4", "e5",
                   "f1", "f3", "f4", "g1", "g4", "h2", "h5"],
            False: ["a2", "a4", "a6", "a7", "a8", "b5", "b7", "b8", "c2", "c4", "c5", "c6", "c8", "d3", "d4", "d5",
                    "d7", "d8", "e2", "e5", "e7", "f3", "f6", "f7", "g2", "g5", "g8", "h3", "h5", "h6", "h8"]
        }
    },
    "test_resource_3": {
        "fen": "1rn2rk1/1p1q1pbp/p1npb1p1/3Np3/2P1P3/2NBB3/PP3PPP/R2Q1RK1 w - - 14 15",
        "expected_result": {
            True: ["a3", "a4", "a7", "b1", "b3", "b4", "b5", "b6", "c1", "c2", "c5", "c7", "d2", "d4", "e1", "e2",
                   "e7", "f3", "f4", "f5", "f6", "g3", "g4", "g5", "h3", "h5", "h6"],
            False: ["a5", "a7", "a8", "b4", "b5", "b6", "c5", "c7", "d4", "d5", "d8", "e7", "e8", "f4", "f5", "f6",
                    "g4", "h3", "h5", "h6", "h8"]
        }
    },
    "test_resource_4": {
        "fen": "rnbqkbnr/pppppppp/8/8/4P3/8/PPPP1PPP/RNBQKBNR b KQkq e3 0 1",
        "expected_result": {
            True: ["a3", "a6", "b3", "b5", "c3", "c4", "d3", "d5", "e2", "e3", "f3", "f5", "g3", "g4", "h3", "h5"],
            False: ["a6", "b6", "c6", "d6", "e6", "f6", "g6", "h6"]
        }
    },
    "test_resource_5": {
        "fen": "5k2/1R3p2/3N2p1/8/3p2Pp/2n2K1P/P3r3/8 b - - 1 42",
        "expected_result": {
            True: ["a7", "b1", "b2", "b3", "b4", "b5", "b6", "b8", "c4", "c7", "c8", "d7", "e2", "e3", "e4",
                   "e7", "e8", "f2", "f4", "f5", "f7", "g2", "g3", "h5"],
            False: ["a2", "b2", "c2", "d2", "e1", "f2", "g2", "h2", "e3", "e4", "e5", "e6", "e7", "e8", "b1", "d1",
                    "a4", "b5", "d5", "f5", "g3", "h5"]
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
def test__smoke__chess_board__get_attacked_squares(test_key, test_data, expected_output):
    test_object = ChessBoard(test_data["fen"])
    test_object.generate_all_possible_moves()
    for active_colour in test_data["expected_result"]:
        actual_result = sorted(test_object.get_attacked_squares(active_colour))
        assert actual_result == test_data["expected_result"][active_colour], (f"Failed on {test_key}, expected: "
                                                                     f"{test_data['expected_result']}, "
                                                                     f"actual: {actual_result}")
