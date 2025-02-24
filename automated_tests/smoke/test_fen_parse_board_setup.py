from pytest import mark

from src.fen import Fen
from src.piece import PieceType

test_data_dict = {
    "test_resource_1": {
        "fen": "6k1/7p/6p1/p3r3/6P1/7P/1B3K2/3R4 b - - 2 9",
        "test_fen": "6k1/7p/6p1/p3r3/6P1/7P/1B3K2/3R4",
        "piece_indexes": (0, 3),
        "expected_result": {
            "active_colour_white": True,
            "piece_type": PieceType.ROOK,
            "position": (3, 0)
        }
    },
    "test_resource_2": {
        "fen": "6k1/7p/6p1/p3r3/6P1/7P/1B3K2/3R4 b - - 2 9",
        "test_fen": "6k1/7p/6p1/p3r3/6P1/7P/1B3K2/3R4",
        "piece_indexes": (4, 0),
        "expected_result": {
            "active_colour_white": False,
            "piece_type": PieceType.PAWN,
            "position": (0, 4)
        }
    },
    "test_resource_3": {
        "fen": "6k1/7p/6p1/p3r3/6P1/7P/1B3K2/3R4 b - - 2 9",
        "test_fen": "6k1/7p/6p1/p3r3/6P1/7P/1B3K2/3R4",
        "piece_indexes": (5, 6),
        "expected_result": {
            "active_colour_white": False,
            "piece_type": PieceType.PAWN,
            "position": (6, 5)
        }
    },
    "test_resource_4": {
        "fen": "6k1/7p/6p1/p3r3/6P1/7P/1B3K2/3R4 b - - 2 9",
        "test_fen": "6k1/7p/6p1/p3r3/6P1/7P/1B3K2/3R4",
        "piece_indexes": (1, 1),
        "expected_result": {
            "active_colour_white": True,
            "piece_type": PieceType.BISHOP,
            "position": (1, 1)
        }
    },
    "test_resource_5": {
        "fen": "6k1/7p/6p1/p3r3/6P1/7P/1B3K2/3R4 b - - 2 9",
        "test_fen": "6k1/7p/6p1/p3r3/6P1/7P/1B3K2/3R4",
        "piece_indexes": (1, 5),
        "expected_result": {
            "active_colour_white": True,
            "piece_type": PieceType.KING,
            "position": (5, 1)
        }
    },
    "test_resource_6": {
        "fen": "r1b1r1k1/1pb3p1/2nq1p2/2N3P1/pPRp3p/3N3P/P1Q1PPB1/5RK1 b - b3 4 23",
        "test_fen": "r1b1r1k1/1pb3p1/2nq1p2/2N3P1/pPRp3p/3N3P/P1Q1PPB1/5RK1",
        "piece_indexes": (6, 6),
        "expected_result": {
            "active_colour_white": False,
            "piece_type": PieceType.PAWN,
            "position": (6, 6)
        }
    },
    "test_resource_7": {
        "fen": "r1b1r1k1/1pb3p1/2nq1p2/2N3P1/pPRp3p/3N3P/P1Q1PPB1/5RK1 b - b3 4 23",
        "test_fen": "r1b1r1k1/1pb3p1/2nq1p2/2N3P1/pPRp3p/3N3P/P1Q1PPB1/5RK1",
        "piece_indexes": (1, 6),
        "expected_result": {
            "active_colour_white": True,
            "piece_type": PieceType.BISHOP,
            "position": (6, 1)
        }
    },
    "test_resource_8": {
        "fen": "r1b1r1k1/1pb3p1/2nq1p2/2N3P1/pPRp3p/3N3P/P1Q1PPB1/5RK1 b - b3 4 23",
        "test_fen": "r1b1r1k1/1pb3p1/2nq1p2/2N3P1/pPRp3p/3N3P/P1Q1PPB1/5RK1",
        "piece_indexes": (7, 6),
        "expected_result": {
            "active_colour_white": False,
            "piece_type": PieceType.KING,
            "position": (6, 7)
        }
    },
    "test_resource_9": {
        "fen": "r1b1r1k1/1pb3p1/2nq1p2/2N3P1/pPRp3p/3N3P/P1Q1PPB1/5RK1 b - b3 4 23",
        "test_fen": "r1b1r1k1/1pb3p1/2nq1p2/2N3P1/pPRp3p/3N3P/P1Q1PPB1/5RK1",
        "piece_indexes": (3, 7),
        "expected_result": {
            "active_colour_white": False,
            "piece_type": PieceType.PAWN,
            "position": (7, 3)
        }
    },
    "test_resource_10": {
        "fen": "r1b1r1k1/1pb3p1/2nq1p2/2N3P1/pPRp3p/3N3P/P1Q1PPB1/5RK1 b - b3 4 23",
        "test_fen": "r1b1r1k1/1pb3p1/2nq1p2/2N3P1/pPRp3p/3N3P/P1Q1PPB1/5RK1",
        "piece_indexes": (4, 2),
        "expected_result": {
            "active_colour_white": True,
            "piece_type": PieceType.KNIGHT,
            "position": (2, 4)
        }
    },
}


def get_parametrized_test_set():
    parametrized_test_set_list = []
    for test_data in test_data_dict.values():
        parametrized_test_set_list.append((test_data, test_data["expected_result"]))
    return parametrized_test_set_list


@mark.smoke
@mark.parametrize("test_data,expected_output", get_parametrized_test_set(), ids=test_data_dict.keys())
def test__smoke__fen__parse_board_setup__verify_fields(test_data, expected_output):
    test_object = Fen(test_data["fen"])
    return_data = test_object.parse_board_setup(test_data["test_fen"])
    x, y = test_data["piece_indexes"][0], test_data["piece_indexes"][1]
    tested_piece = return_data[x][y]
    for expected_key, expected_value in expected_output.items():
        actual_data = getattr(tested_piece, expected_key)
        assert actual_data == expected_value, f"Expected: {expected_value}, actual: {actual_data}"


@mark.smoke
def test__smoke__fen__parse_board_setup__verify_positions():
    test_object = Fen("r1b1r1k1/1pb3p1/2nq1p2/2N3P1/pPRp3p/3N3P/P1Q1PPB1/5RK1 b - b3 4 23")
    return_data = test_object.parse_board_setup("r1b1r1k1/1pb3p1/2nq1p2/2N3P1/pPRp3p/3N3P/P1Q1PPB1/5RK1")
    for file in range(8):
        for rank in range(8):
            expected_data = (rank, file)
            tested_piece = return_data[file][rank]
            if tested_piece is not PieceType.EMPTY:
                actual_data = tested_piece.position
                assert actual_data == expected_data, f"Expected: {expected_data}, actual: {actual_data}"
