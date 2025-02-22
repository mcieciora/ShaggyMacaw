from pytest import mark

from src.chess_board import ChessBoard
from src.move import Move


test_data_dict = {
    "test_resource_1": {
        "fen": "8/P7/5k2/5B2/6Pp/1P3K1P/8/8 w - - 4 23",
        "moves": [
            Move(original_square="b3", target_square="b4", is_move_legal=True, piece_value="P", active_colour=True),
            Move(original_square="f6", target_square="e7", is_move_legal=True, piece_value="k", active_colour=False),
            Move(original_square="a7", target_square="a8", is_move_legal=True, piece_value="P", active_colour=True,
                 is_promotion=True, promotion_piece="Q"),
            Move(original_square="e7", target_square="d6", is_move_legal=True, piece_value="P", active_colour=False)
        ],
        "expected_data": "Q7/8/3k4/5B2/1P4Pp/5K1P/8/8 w - - 1 25"
    },
    "test_resource_2": {
        "fen": "2b1r1k1/1p3pp1/2n5/2N5/Q2p1NPp/7P/PP2P1B1/2q2RK1 b - - 2 28",
        "moves": [
            Move(original_square="c1", target_square="c5", is_move_legal=True, piece_value="q", active_colour=False),
            Move(original_square="b2", target_square="b4", is_move_legal=True, piece_value="P", active_colour=True),
            Move(original_square="c5", target_square="d6", is_move_legal=True, piece_value="q", active_colour=False),
            Move(original_square="b4", target_square="b5", is_move_legal=True, piece_value="P", active_colour=True),
            Move(original_square="d4", target_square="d3", is_move_legal=True, piece_value="p", active_colour=False),
            Move(original_square="f4", target_square="d3", is_move_legal=True, piece_value="N", active_colour=True,
                 is_capture=True),
        ],
        "expected_data": "2b1r1k1/1p3pp1/2nq4/1P6/Q5Pp/3N3P/P3P1B1/5RK1 b - - 0 31"
    },
    "test_resource_3": {
        "fen": "r1bqkb1r/pp3ppp/2n2n2/2pp4/3P4/2N2NP1/PP2PPBP/R1BQK2R b KQkq - 2 7",
        "moves": [
            Move(original_square="c5", target_square="c4", is_move_legal=True, piece_value="p", active_colour=False),
            Move(original_square="b2", target_square="b4", is_move_legal=True, piece_value="P", active_colour=True),
            Move(original_square="c4", target_square="b3", is_move_legal=True, piece_value="p", active_colour=False,
                 is_capture=True, is_en_passant=True),
            Move(original_square="e1", target_square="g1", is_move_legal=True, piece_value="K", active_colour=True,
                 is_castling=True),
            Move(original_square="b3", target_square="a2", is_move_legal=True, piece_value="p", active_colour=False,
                 is_capture=True),
            Move(original_square="a1", target_square="a2", is_move_legal=True, piece_value="R", active_colour=True,
                 is_capture=True)
        ],
        "expected_data": "r1bqkb1r/pp3ppp/2n2n2/3p4/3P4/2N2NP1/R3PPBP/2BQ1RK1 b kq - 0 10"
    },
    "test_resource_4": {
        "fen": "8/1p4k1/pR6/6p1/P1r5/5K2/1P6/8 w - - 1 44",
        "moves": [
            Move(original_square="b6", target_square="b7", is_move_legal=True, piece_value="R", active_colour=True,
                 is_capture=True),
            Move(original_square="g7", target_square="f6", is_move_legal=True, piece_value="k", active_colour=False),
            Move(original_square="b7", target_square="b6", is_move_legal=True, piece_value="R", active_colour=True),
            Move(original_square="f6", target_square="f5", is_move_legal=True, piece_value="k", active_colour=False),
            Move(original_square="b6", target_square="a6", is_move_legal=True, piece_value="R", active_colour=True,
                 is_capture=True),
            Move(original_square="c4", target_square="f4", is_move_legal=True, piece_value="r", active_colour=False)
        ],
        "expected_data": "8/8/R7/5kp1/P4r2/5K2/1P6/8 w - - 1 47"
    }
}


def get_parametrized_test_set():
    parametrized_test_set_list = [(test_key, test_data) for test_key, test_data in test_data_dict.items()]
    return parametrized_test_set_list


@mark.smoke
@mark.parametrize("test_key,test_data", get_parametrized_test_set(), ids=test_data_dict.keys())
def test__smoke__chess_board__move_piece_and_regenerate_fen(test_key, test_data):
    chess_board = ChessBoard(test_data["fen"])
    for move in test_data["moves"]:
        chess_board.move_piece(move)
    actual_result = chess_board.fen.regenerate_fen()
    assert actual_result == test_data["expected_data"], \
        f"Failed on {test_key}, expected: {test_data['expected_data']}, actual: {actual_result}"
