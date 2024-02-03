from pytest import mark
from src.main import get_google_com_status_code


@mark.smoke
def test__smoke__get_google_com_status_code():
    return_status_code = get_google_com_status_code()
    assert return_status_code == 200, f"Status code check failed. Actual {return_status_code}, Expected: 200"
