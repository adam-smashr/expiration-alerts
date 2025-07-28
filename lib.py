import logging
import pandas as pd

from numpy import datetime64
from datetime import date
from tabulate import tabulate, tabulate_formats

TODAYS_DATE = date.today()
REPORT_HEADERS = ["Name", "Days Left"]  # headers to include in report
WARNING_THRESHOLD = 10  # number of days before a food is considered expiring
TABLE_FORMAT = "simple"  # tabulate table format


logger = logging.getLogger(__name__)
logging.basicConfig(
    level=logging.DEBUG,
    filename="report.log",
    filemode="w",
    format="%(message)s",
)


def is_expired(expiration_date: date) -> bool:
    return expiration_date <= TODAYS_DATE


def days_left(expiration_date: date) -> int:
    return (expiration_date - TODAYS_DATE).days


def format_datetime(date_str: datetime64) -> date:
    return pd.Timestamp(date_str).date()


def format_table(table: pd.DataFrame, tablefmt: str) -> str:
    if tablefmt not in tabulate_formats:
        raise TypeError(f"Table format not compatible, expected: {tabulate_formats}")

    return tabulate(
        table.to_dict(orient="list"),
        headers="keys",
        tablefmt=tablefmt,
        showindex=False,
    )


def get_expiring_foods(df: pd.DataFrame) -> str:
    """
    return foods with less than a certain number of days, but exclude expired foods
    """
    table = df.loc[
        (df["Days Left"] < WARNING_THRESHOLD) & (df["Days Left"] > 0),
        REPORT_HEADERS,
    ]

    return format_table(table=table, tablefmt=TABLE_FORMAT)


def get_expired_foods(df: pd.DataFrame) -> str:
    table = df.loc[df["Is Expired"], REPORT_HEADERS]
    return format_table(table=table, tablefmt=TABLE_FORMAT)


def sort_by_expriy_date(df: pd.DataFrame) -> str:
    table = df.loc[:, REPORT_HEADERS].sort_values(by="Days Left")
    return format_table(table=table, tablefmt=TABLE_FORMAT)
