from lib import is_expired, TODAYS_DATE, format_datetime

past_date = format_datetime("08/08/1990")
future_date = format_datetime("12/02/2077")


def test_past_date() -> None:
    assert is_expired(past_date) is True


def test_future_date() -> None:
    assert is_expired(future_date) is False


def test_todays_date() -> None:
    assert is_expired(TODAYS_DATE) is True
