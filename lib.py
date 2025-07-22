import pandas as pd
from datetime import date
from typing import Any

TODAYS_DATE = date.today()


def is_expired(expiration_date: date) -> bool:
    return expiration_date <= TODAYS_DATE


def days_left(expiration_date: date) -> int:
    return (expiration_date - TODAYS_DATE).days


def format_datetime(date_str: Any) -> date:
    return pd.Timestamp(date_str).date()
