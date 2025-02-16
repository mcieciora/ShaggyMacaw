from pytest import mark

from src.chess_board import ChessBoard
from src.piece import Pawn


test_data_dict = {
    "test_resource_1": {
        "fen": "r1b1r1k1/1pb3p1/2nq1p2/2N3P1/pPRp3p/3N3P/P1Q1PPB1/5RK1 b - b3 4 23",
        "value": "p",
        "position": (0, 3),
        "expected_result": ["a4a3", "a4b3"]
    },
    "test_resource_2": {
        "fen": "r1b1r1k1/1pb3p1/2nq1p2/2N3P1/pPRp3p/3N3P/P1Q1PPB1/5RK1 b - b3 4 23",
        "value": "p",
        "position": (1, 6),
        "expected_result": ["b7b6", "b7b5"]
    },
    "test_resource_3": {
        "fen": "r1b1r1k1/1pb3p1/2nq1p2/2N3P1/pPRp3p/3N3P/P1Q1PPB1/5RK1 b - b3 4 23",
        "value": "p",
        "position": (3, 3),
        "expected_result": []
    },
    "test_resource_4": {
        "fen": "r1b1r1k1/1pb3p1/2nq1p2/2N3P1/pPRp3p/3N3P/P1Q1PPB1/5RK1 b - b3 4 23",
        "value": "p",
        "position": (5, 5),
        "expected_result": ["f6f5", "f6g5"]
    },
    "test_resource_5": {
        "fen": "r1b1r1k1/1pb3p1/2nq1p2/2N3P1/pPRp3p/3N3P/P1Q1PPB1/5RK1 b - b3 4 23",
        "value": "p",
        "position": (6, 6),
        "expected_result": ["g7g6"]
    },
    "test_resource_6": {
        "fen": "r1b1r1k1/1pb3p1/2nq1p2/2N3P1/pPRp3p/3N3P/P1Q1PPB1/5RK1 b - b3 4 23",
        "value": "p",
        "position": (7, 3),
        "expected_result": []
    },
    "test_resource_7": {
        "fen": "r1b1r1k1/1pb3p1/2nq1p2/2N3P1/pPRp3p/3N3P/P1Q1PPB1/5RK1 b - b3 4 23",
        "value": "P",
        "position": (0, 1),
        "expected_result": ["a2a3"]
    },
    "test_resource_8": {
        "fen": "r1b1r1k1/1pb3p1/2nq1p2/2N3P1/pPRp3p/3N3P/P1Q1PPB1/5RK1 b - b3 4 23",
        "value": "P",
        "position": (1, 3),
        "expected_result": ["b4b5"]
    },
    "test_resource_9": {
        "fen": "r1b1r1k1/1pb3p1/2nq1p2/2N3P1/pPRp3p/3N3P/P1Q1PPB1/5RK1 b - b3 4 23",
        "value": "P",
        "position": (4, 1),
        "expected_result": ["e2e3", "e2e4"]
    },
    "test_resource_10": {
        "fen": "r1b1r1k1/1pb3p1/2nq1p2/2N3P1/pPRp3p/3N3P/P1Q1PPB1/5RK1 b - b3 4 23",
        "value": "P",
        "position": (5, 1),
        "expected_result": ["f2f3", "f2f4"]
    },
    "test_resource_11": {
        "fen": "r1b1r1k1/1pb3p1/2nq1p2/2N3P1/pPRp3p/3N3P/P1Q1PPB1/5RK1 b - b3 4 23",
        "value": "P",
        "position": (6, 4),
        "expected_result": ["g5g6", "g5f6"]
    },
    "test_resource_12": {
        "fen": "r1b1r1k1/1pb3p1/2nq1p2/2N3P1/pPRp3p/3N3P/P1Q1PPB1/5RK1 b - b3 4 23",
        "value": "P",
        "position": (7, 2),
        "expected_result": []
    },
    "test_resource_13": {
        "fen": "r3r1k1/pp3p1p/1bn5/P5p1/3p1NbP/6P1/1P1NPPB1/R1R2K2 w - - 0 18",
        "value": "p",
        "position": (1, 6),
        "expected_result": []
    },
    "test_resource_14": {
        "fen": "r3r1k1/1P5p/2n2p2/6p1/2Pp1NbP/6P1/3NPPB1/R1R2K2 w - - 0 19",
        "value": "P",
        "position": (1, 6),
        "expected_result": ["b8=Q", "b8=R", "b8=N", "b8=B", "b7a8=Q", "b7a8=R", "b7a8=N", "b7a8=B"]
    },
    "test_resource_15": {
        "fen": "5k2/1R3p2/3N2p1/8/6Pp/2n2K1P/P2pr3/8 w - - 1 42",
        "value": "p",
        "position": (3, 1),
        "expected_result": ["d1=q", "d1=r", "d1=n", "d1=b"]
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
    pawn = Pawn(test_data["value"], test_data["position"])
    actual_result = test_object.generate_pawn_moves(pawn)
    assert [str(result) for result in actual_result] == test_data["expected_result"], (
        f"Failed on {test_key}, expected: {test_data['expected_result']}, actual: {actual_result}")
