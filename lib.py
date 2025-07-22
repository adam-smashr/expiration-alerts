import pandas as pd
from numpy import datetime64
from datetime import date

TODAYS_DATE = date.today()


def is_expired(expiration_date: date) -> bool:
    return expiration_date <= TODAYS_DATE


def days_left(expiration_date: date) -> int:
    return (expiration_date - TODAYS_DATE).days


def format_datetime(date_str: datetime64) -> date:
    return pd.Timestamp(date_str).date()


def generate_report(df: pd.DataFrame) -> str:
    """print each item and how many days until it expires, sorted by days left"""
    return df.loc[:, ["Name", "Days Left"]].sort_values(by="Days Left").to_string()
