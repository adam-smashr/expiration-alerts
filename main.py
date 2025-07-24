import pandas as pd
from lib import days_left, format_datetime, is_expired, generate_report
from logger import get_credentials, create_logger


def main() -> None:

    creds = get_credentials("credentials.yaml")
    logger = create_logger(creds)

    df = pd.read_excel(io="food_items.xlsx")

    df["Expiration Date"] = df["Expiration Date"].apply(format_datetime)
    df["Is Expired"] = df["Expiration Date"].apply(is_expired)
    df["Days Left"] = df["Expiration Date"].apply(days_left)

    logger.error(generate_report(df, "grid"))


if __name__ == "__main__":
    main()
