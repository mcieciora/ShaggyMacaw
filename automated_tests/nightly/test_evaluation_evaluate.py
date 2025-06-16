from datetime import datetime
from glob import glob
from json import dumps
from pytest import mark

from src.chess_board import ChessBoard
from src.evaluation import Evaluation


@mark.nightly
def test__nightly__evaluation__measure_evaluate_runtime():
    fen_files = glob("automated_tests/test_data/*")
    runtime_results_map = {}
    for fen_file in fen_files:
        with open(fen_file, mode="r", encoding="utf-8") as test_fen_file:
            for line in test_fen_file.readlines():
                chess_board = ChessBoard(line)
                test_object = Evaluation(chess_board)
                start = datetime.now()
                test_object.evaluate()
                runtime = datetime.now() - start
                runtime_results_map[test_object.chess_board.fen.current_fen] = runtime.microseconds
    with open("results/measure_evaluate_runtime.json", mode="w", encoding="utf-8") as result_file:
        result_file.writelines(dumps(runtime_results_map))
