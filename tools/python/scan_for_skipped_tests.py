from sys import exit  # pylint: disable=redefined-builtin
from glob import glob


def scan_for_skipped_tests():
    """
    Script searches for all skip marks in test suites.

    :return: None
    """
    skipped_tests_dict = {}
    for python_file in glob("automated_tests/**/test_*.py"):
        with open(python_file, "r", encoding="utf-8") as file:
            file_content = file.read()
            pattern = "@mark.skip"
            if pattern in file_content:
                skipped_tests_dict[python_file] = file_content.count(pattern)
                print(
                    f"[ERR] {file_content.count(pattern)} skip mark(s) found in: {python_file}"
                )
    if skipped_tests_dict.keys():
        exit(1)


if __name__ == "__main__":
    scan_for_skipped_tests()
