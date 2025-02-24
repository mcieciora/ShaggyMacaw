from pytest import mark

from src.chess_board import ChessBoard
from src.piece import Piece


test_data_dict = {
    "test_resource_1": {
        "fen": "r1b1r1k1/1pb3p1/2nq1p2/2N3P1/pPRp3p/3N3P/P1Q1PPB1/5RK1 b - b3 4 23",
        "value": "B",
        "position": (6, 1),
        "expected_result": ["g2h1", "g2f3", "g2e4", "g2d5", "g2c6"]
    },
    "test_resource_2": {
        "fen": "r1b1r1k1/1pb3p1/2nq1p2/2N3P1/pPRp3p/3N3P/P1Q1PPB1/5RK1 b - b3 4 23",
        "value": "b",
        "position": (2, 6),
        "expected_result": ["c7d8", "c7b8", "c7b6", "c7a5"]
    },
    "test_resource_3": {
        "fen": "r1b1r1k1/1pb3p1/2nq1p2/2N3P1/pPRp3p/3N3P/P1Q1PPB1/5RK1 b - b3 4 23",
        "value": "b",
        "position": (2, 7),
        "expected_result": ["c8d7", "c8e6", "c8f5", "c8g4", "c8h3"]
    },
    "test_resource_4": {
        "fen": "r3r1k1/pp3p1p/1bn5/P5p1/3p1NbP/6P1/1P1NPPB1/R1R2K2 w - - 0 18",
        "value": "B",
        "position": (6, 1),
        "expected_result": ["g2h3", "g2h1", "g2f3", "g2e4", "g2d5", "g2c6", ]
    },
    "test_resource_5": {
        "fen": "r3r1k1/pp3p1p/1bn5/P5p1/3p1NbP/6P1/1P1NPPB1/R1R2K2 w - - 0 18",
        "value": "b",
        "position": (1, 5),
        "expected_result": ["b6c7", "b6d8", "b6c5", "b6a5"]
    },
    "test_resource_6": {
        "fen": "r3r1k1/pp3p1p/1bn5/P5p1/3p1NbP/6P1/1P1NPPB1/R1R2K2 w - - 0 18",
        "value": "b",
        "position": (6, 3),
        "expected_result": ["g4h5", "g4h3", "g4f5", "g4e6", "g4d7", "g4c8", "g4f3", "g4e2"]
    }
}


def get_parametrized_test_set():
    parametrized_test_set_list = []
    for test_key, test_data in test_data_dict.items():
        parametrized_test_set_list.append((test_key, test_data, test_data["expected_result"]))
    return parametrized_test_set_list


@mark.smoke
@mark.parametrize("test_key,test_data,expected_output", get_parametrized_test_set(), ids=test_data_dict.keys())
def test__smoke__chess_board__generate_bishop_moves(test_key, test_data, expected_output):
    test_object = ChessBoard(test_data["fen"])
    piece = Piece(test_data["value"], test_data["position"])
    actual_result = test_object.generate_piece_moves(piece)
    assert [str(result) for result in actual_result] == expected_output, \
        f"Failed on {test_key}, expected: {expected_output}, actual: {actual_result}"
