from lib import days_left, TODAYS_DATE
import datetime

past_date = TODAYS_DATE - datetime.timedelta(5)
future_date = TODAYS_DATE + datetime.timedelta(10)


def test_past_date() -> None:
    assert days_left(past_date) == -5


def test_future_date() -> None:
    assert days_left(future_date) == 10


def test_todays_date() -> None:
    assert days_left(TODAYS_DATE) == 0
