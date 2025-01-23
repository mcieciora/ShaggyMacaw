from pytest import mark

from src.chess_board import ChessBoard

test_data_dict = {
    "test_resource_1": {
        "fen": "r1b1r1k1/1pb3p1/2nq1p2/2N3P1/pPRp3p/3N3P/P1Q1PPB1/5RK1 b - b3 4 23",
        "index": 32,
        "piece": "p",
        "expected_result": ["a3", "axb3"]
    },
    "test_resource_2": {
        "fen": "r1b1r1k1/1pb3p1/2nq1p2/2N3P1/pPRp3p/3N3P/P1Q1PPB1/5RK1 b - b3 4 23",
        "index": 9,
        "piece": "p",
        "expected_result": ["b6", "b5"]
    },
    "test_resource_3": {
        "fen": "r1b1r1k1/1pb3p1/2nq1p2/2N3P1/pPRp3p/3N3P/P1Q1PPB1/5RK1 b - b3 4 23",
        "index": 35,
        "piece": "p",
        "expected_result": []
    },
    "test_resource_4": {
        "fen": "r1b1r1k1/1pb3p1/2nq1p2/2N3P1/pPRp3p/3N3P/P1Q1PPB1/5RK1 b - b3 4 23",
        "index": 21,
        "piece": "p",
        "expected_result": ["f5", "fxg5"]
    },
    "test_resource_5": {
        "fen": "r1b1r1k1/1pb3p1/2nq1p2/2N3P1/pPRp3p/3N3P/P1Q1PPB1/5RK1 b - b3 4 23",
        "index": 14,
        "piece": "p",
        "expected_result": ["g6"]
    },
    "test_resource_6": {
        "fen": "r1b1r1k1/1pb3p1/2nq1p2/2N3P1/pPRp3p/3N3P/P1Q1PPB1/5RK1 b - b3 4 23",
        "index": 39,
        "piece": "p",
        "expected_result": []
    },
    "test_resource_7": {
        "fen": "r1b1r1k1/1pb3p1/2nq1p2/2N3P1/pPRp3p/3N3P/P1Q1PPB1/5RK1 b - b3 4 23",
        "index": 48,
        "piece": "P",
        "expected_result": ["a3"]
    },
    "test_resource_8": {
        "fen": "r1b1r1k1/1pb3p1/2nq1p2/2N3P1/pPRp3p/3N3P/P1Q1PPB1/5RK1 b - b3 4 23",
        "index": 33,
        "piece": "P",
        "expected_result": ["b5"]
    },
    "test_resource_9": {
        "fen": "r1b1r1k1/1pb3p1/2nq1p2/2N3P1/pPRp3p/3N3P/P1Q1PPB1/5RK1 b - b3 4 23",
        "index": 52,
        "piece": "P",
        "expected_result": ["e3", "e4"]
    },
    "test_resource_10": {
        "fen": "r1b1r1k1/1pb3p1/2nq1p2/2N3P1/pPRp3p/3N3P/P1Q1PPB1/5RK1 b - b3 4 23",
        "index": 53,
        "piece": "P",
        "expected_result": ["f3", "f4"]
    },
    "test_resource_11": {
        "fen": "r1b1r1k1/1pb3p1/2nq1p2/2N3P1/pPRp3p/3N3P/P1Q1PPB1/5RK1 b - b3 4 23",
        "index": 30,
        "piece": "P",
        "expected_result": ["g6", "gxf6"]
    },
    "test_resource_12": {
        "fen": "r1b1r1k1/1pb3p1/2nq1p2/2N3P1/pPRp3p/3N3P/P1Q1PPB1/5RK1 b - b3 4 23",
        "index": 47,
        "piece": "P",
        "expected_result": []
    },
    "test_resource_13": {
        "fen": "r3r1k1/pp3p1p/1bn5/P5p1/3p1NbP/6P1/1P1NPPB1/R1R2K2 w - - 0 18",
        "index": 9,
        "piece": "p",
        "expected_result": []
    },
    "test_resource_14": {
        "fen": "r3r1k1/1P5p/2n2p2/6p1/2Pp1NbP/6P1/3NPPB1/R1R2K2 w - - 0 19 ",
        "index": 9,
        "piece": "P",
        "expected_result": ["b8=Q", "b8=N", "b8=R", "b8=B", "bxa8=Q", "bxa8=N", "bxa8=R", "bxa8=B"]
    },
    "test_resource_15": {
        "fen": "5k2/1R3p2/3N2p1/8/6Pp/2n2K1P/P2pr3/8 w - - 1 42",
        "index": 51,
        "piece": "p",
        "expected_result": ["d1=Q", "d1=N", "d1=R", "d1=B"]
    }
}


def get_parametrized_test_set():
    parametrized_test_set_list = []
    for test_key, test_data in test_data_dict.items():
        parametrized_test_set_list.append((test_key, test_data, test_data["expected_result"]))
    return parametrized_test_set_list



@mark.smoke
@mark.parametrize("test_key,test_data,expected_output", get_parametrized_test_set(), ids=test_data_dict.keys())
def test__smoke__chess_board__generate_pawn_moves(test_key, test_data, expected_output):
    test_object = ChessBoard(test_data["fen"])
    actual_result = test_object.generate_pawn_moves(test_data["index"], test_data["piece"])
    assert actual_result == test_data["expected_result"], (f"Failed on {test_key}, expected: "
                                                           f"{test_data['expected_result']}, actual: "
                                                           f"{actual_result}")
