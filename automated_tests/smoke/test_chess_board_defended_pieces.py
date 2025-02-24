from pytest import mark

from src.chess_board import ChessBoard

test_data_dict = {
    "test_resource_1": {
        "fen": "rn1q1rk1/pb1pppbp/1p3np1/2P5/8/1P2PN2/PBP1BPPP/RN1Q1RK1 b - - 0 8",
        "expected_result": {
            True: ["a1", "a2", "b1", "b3", "c2", "d1", "e2", "e3", "f1", "f2", "f3", "g1", "g2", "h2"],
            False: ["a8", "a7", "b8", "b6", "d8", "d7", "e7", "f8", "f7", "f6", "g8", "g7", "g6", "h7"]
        }
    },
    "test_resource_2": {
        "fen": "r2q1rk1/pb3pbp/3ppnp1/2p1n3/2P5/1PN1P3/PBQNBPPP/R4RK1 b - - 1 13",
        "expected_result": {
            True: ["a1", "a2", "b2", "b3", "c3", "c4", "d2", "e2", "e3", "f1", "f2", "g1", "g2", "h2"],
            False: ["a8", "a7", "c5", "d6", "d8", "e5", "e6", "f6", "f7", "f8", "g6", "g7", "g8", "h7"]
        }
    },
    "test_resource_3": {
        "fen": "2rr2k1/pb2qpbp/5np1/2ppn3/8/1PN1P2P/PBQNBPP1/3RR1K1 w - - 0 18",
        "expected_result": {
            True: ["b2", "b3", "c3", "d1", "d2", "e1", "e2", "e3", "f2", "g2", "h3"],
            False: ["c8", "c5", "d8", "d5", "e5", "f7", "f6", "g7", "g6", "h7"]
        }
    },
    "test_resource_4": {
        "fen": "r3r1k1/pp3p1p/1bn5/6p1/3p1Nb1/6P1/PP1NPPBP/R1R2K2 w - g6 0 18",
        "expected_result": {
            True: ["a1", "a2", "c1", "e2", "f2", "f4", "g2", "g3"],
            False: ["a8", "a7", "b6", "c6", "d4", "e8", "f7", "g8", "h7"]
        }
    },
    "test_resource_5": {
        "fen": "2r3k1/p1r2p1p/6p1/2N1R3/2N5/1P5P/P4P2/6K1 w - - 0 31",
        "expected_result": {
            True: ["a2", "b3", "c4", "c5", "e5", "f2", "g1"],
            False: ["a7", "c7", "c8", "f7", "g6", "g8", "h7"]
        }
    }
}


def get_parametrized_test_set():
    parametrized_test_set_list = []
    for test_data in test_data_dict.values():
        parametrized_test_set_list.append((test_data, test_data["expected_result"]))
    return parametrized_test_set_list


@mark.smoke
@mark.parametrize("test_data,expected_output", get_parametrized_test_set(), ids=test_data_dict.keys())
def test__smoke__chess_board__defended_pieces(test_data, expected_output):
    test_object = ChessBoard(test_data["fen"])
    test_object.generate_all_possible_moves()
    for active_colour in test_object.defended_pieces:
        actual_data = test_object.defended_pieces[active_colour]
        expected_data = expected_output[active_colour]
        assert actual_data == expected_data, f"Expected: {expected_data}, actual: {actual_data}."
