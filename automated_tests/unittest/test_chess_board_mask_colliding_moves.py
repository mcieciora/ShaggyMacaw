from pytest import mark

from src.chess_board import ChessBoard
from src.move import Move


@mark.unittest
def test__unittest__chess_board__mask_colliding_moves():
    original_fen = "8/5p1N/6p1/8/5kPp/3K3P/P7/8 b - - 21 52"
    expected_data = ["f4e5", "f4f3", "d3d4", "d3c4", "d3c3", "d3c2", "d3d2", "d3e2"]
    test_object = ChessBoard(original_fen)

    moves_dict = {
        False: {
            "e3": Move(original_square="f4", target_square="e3", active_colour=False),
            "e4": Move(original_square="f4", target_square="e4", active_colour=False),
            "e5": Move(original_square="f4", target_square="e5", active_colour=False),
            "f3": Move(original_square="f4", target_square="f3", active_colour=False),
            "g4": Move(original_square="f4", target_square="g4", active_colour=False)
        },
        True: {
            "c2": Move(original_square="d3", target_square="c2", active_colour=True),
            "c3": Move(original_square="d3", target_square="c3", active_colour=True),
            "c4": Move(original_square="d3", target_square="c4", active_colour=True),
            "d2": Move(original_square="d3", target_square="d2", active_colour=True),
            "d4": Move(original_square="d3", target_square="d4", active_colour=True),
            "e2": Move(original_square="d3", target_square="e2", active_colour=True),
            "e3": Move(original_square="d3", target_square="e3", active_colour=True),
            "e4": Move(original_square="d3", target_square="e4", active_colour=True),
        }
    }

    actual_data = test_object.mask_colliding_moves(moves_dict)
    white_king_moves_number = len([move for move in actual_data if str(move).startswith("d3")])
    black_king_moves_number = len([move for move in actual_data if str(move).startswith("f4")])

    assert white_king_moves_number == 6, f"Expected: 6, actual: {white_king_moves_number}"
    assert black_king_moves_number == 3, f"Expected: 3, actual: {black_king_moves_number}"

    for move in expected_data:
        assert move in [str(m) for m in actual_data], f"Expected: {move} not in {actual_data}"
