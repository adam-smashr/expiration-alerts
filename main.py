import logging

import pandas as pd

from lib import (
    days_left,
    format_datetime,
    is_expired,
    get_expired_foods,
    get_expiring_foods,
    sort_by_expriy_date,
    TODAYS_DATE,
    WARNING_THRESHOLD,
)


logger = logging.getLogger(__name__)
logging.basicConfig(
    level=logging.DEBUG,
    filename="report.log",
    filemode="w",
    format="%(message)s",
)


def main() -> None:

    df = pd.read_excel(io="food_items.xlsx")

    df["Expiration Date"] = df["Expiration Date"].apply(format_datetime)
    df["Is Expired"] = df["Expiration Date"].apply(is_expired)
    df["Days Left"] = df["Expiration Date"].apply(days_left)

    logging.info(f"Mick and Adam's Kitchen Inventory Report for {TODAYS_DATE}!\n\n")

    # expired_table = get_expired_foods(df)
    if expired_table := get_expired_foods(df):
        logging.info("The following foods are past the 'best by' date:")
        logging.info(expired_table + "\n\n")
    else:
        logging.info("No foods have expired\n\n")

    # expiring_table = get_almost_expired_foods(df)
    if expiring_table := get_expiring_foods(df):
        logging.info(
            f"The following foods have less than {WARNING_THRESHOLD} days left:"
        )
        logging.info(expiring_table + "\n\n")
    else:
        logging.info("No foods are close to expiring\n\n")

    logging.info("Kitchen Inventory:")
    logging.info(sort_by_expriy_date(df))


if __name__ == "__main__":
    main()
