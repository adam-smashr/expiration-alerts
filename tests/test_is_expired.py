from lib import is_expired, TODAYS_DATE
from datetime import date

# past_date = date("08/08/1990")
past_date = date(month=8, day=8, year=1990)
# future_date = date("12/02/2077")
future_date = date(month=12, day=2, year=2077)


def test_past_date() -> None:
    assert is_expired(past_date) is True


def test_future_date() -> None:
    assert is_expired(future_date) is False


def test_todays_date() -> None:
    assert is_expired(TODAYS_DATE) is True
