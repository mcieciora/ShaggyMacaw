from glob import glob
from pytest import mark

from src.fen import Fen

test_data_dict = {
    "test_resource_1": {
        "expected_result": "8/1p4k1/pR6/6p1/P1r5/5K2/1P6/8 b - - 1 44"
    },
    "test_resource_2": {
        "expected_result": "3k4/1p1r4/pR6/8/4K3/1P6/8/8 w - - 5 51"
    },
    "test_resource_3": {
        "expected_result": "8/8/p7/1p6/1k6/1P6/1K6/8 w - - 0 58"
    },
    "test_resource_4": {
        "expected_result": "r1bqkb1r/pp3ppp/2n2n2/2pp4/3P4/2N2NP1/PP2PPBP/R1BQK2R b KQkq - 2 7"
    },
    "test_resource_5": {
        "expected_result": "r1b2rk1/pp3pp1/1bn2q1p/8/N2p4/1N4P1/PP2PPBP/2RQ1RK1 b - - 1 14"
    },
    "test_resource_6": {
        "expected_result": "r1b1r1k1/1pb2pp1/2nq4/2N5/p1Rp2Pp/3N3P/PPQ1PPB1/5RK1 w - - 4 23"
    },
    "test_resource_7": {
        "expected_result": "2b1r1k1/1p3pp1/2n5/2N5/Q2p1NPp/7P/PP2P1B1/2q2RK1 b - - 2 28"
    },
    "test_resource_8": {
        "expected_result": "4r1k1/1p3pp1/2b5/3Bn3/3p1NPp/7P/PP2P3/5R1K w - - 1 34"
    },
    "test_resource_9": {
        "expected_result": "5k2/1R3p2/3N2p1/8/3p2Pp/2n2K1P/P3r3/8 b - - 1 42"
    },
    "test_resource_10": {
        "expected_result": "3R4/5p1N/6p1/8/3p1kPp/2n4P/P2r4/4K3 b - - 21 52"
    },
}


def get_parametrized_test_set(test_file):
    parametrized_test_set_list = []
    full_test_file_path = glob(f"automated_tests/test_data/{test_file}")[0]
    with open(full_test_file_path, mode="r", encoding="utf-8") as test_fen_file:
        for index, line in enumerate(test_fen_file.readlines()):
            test_board = Fen(line.replace("\n", ""))
            regenerated_fen = test_board.regenerate_fen()
            parametrized_test_set_list.append((regenerated_fen, test_data_dict[f"test_resource_{index+1}"]))
    return parametrized_test_set_list


@mark.smoke
@mark.parametrize("test_data,expected_output", get_parametrized_test_set("fen_1"), ids=test_data_dict.keys())
def test__smoke__fen__generate_board_from_fen(test_data, expected_output):
    assert test_data == expected_output["expected_result"], (f"Expected: {expected_output['expected_result']}, "
                                                             f"actual: {test_data}")
