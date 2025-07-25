import logging

import pandas as pd
from lib import days_left, format_datetime, is_expired, generate_report


logger = logging.getLogger(__name__)
logging.basicConfig(
    level=logging.DEBUG,
    # filename="myapp.log",
    # filemode="w",
    format="%(asctime)s - %(levelname)s - %(message)s",
)


def main() -> None:

    df = pd.read_excel(io="food_items.xlsx")

    df["Expiration Date"] = df["Expiration Date"].apply(format_datetime)
    df["Is Expired"] = df["Expiration Date"].apply(is_expired)
    df["Days Left"] = df["Expiration Date"].apply(days_left)

    logger.info(generate_report(df, "grid"))


if __name__ == "__main__":
    main()
