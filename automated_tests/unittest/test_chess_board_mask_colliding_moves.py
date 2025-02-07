from pytest import mark

from src.chess_board import ChessBoard


@mark.unittest
def test__unittest__chess_board__mask_colliding_moves():
    original_fen = "8/5p1N/6p1/8/5kPp/3K3P/P7/8 b - - 21 52"
    expected_data = ["f4e5", "f4f3", "f4g3", "d3d4", "d3c4", "d3c3", "d3c2", "d3d2", "d3e2"]
    test_object = ChessBoard(original_fen)

    moves_dict = {
        False: {"e3": "f4e3", "e4": "f4e4", "e5": "f4e5", "f3": "f4f3", "g3": "f4g3", "g4": "f4g4"},
        True: {"c2": "d3c2", "c3": "d3c3", "c4": "d3c4", "d2": "d3d2", "d4": "d3d4", "e2": "d3e2", "e3": "d3e3",
            "e4": "d3e4"}}
    
    actual_data = test_object.mask_colliding_moves(moves_dict)
    white_king_moves_number = len([move for move in actual_data if move.startswith("d3")])
    black_king_moves_number = len([move for move in actual_data if move.startswith("f4")])

    assert white_king_moves_number == 6, f"Expected: 6, actual: {white_king_moves_number}"
    # FIXME Fails on active_colour == False trying to take g4 while its defended by h3
    assert black_king_moves_number == 3, f"Expected: 3, actual: {black_king_moves_number}"

    for move in expected_data:
        assert move in actual_data, f"Expected: {move} not in {actual_data}"
