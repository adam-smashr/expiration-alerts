import pandas as pd
from datetime import date
from lib import days_left, format_datetime, is_expired


TODAYS_DATE = date.today()


def main():

    df = pd.read_excel(
        io="fridge_items.xlsx",
        dtype={
            "Name": "string",
            "Notes": "string",
        },
        converters={"Expiration Date": format_datetime},
    )

    df["Is Expired"] = [
        is_expired(expiration_date) for expiration_date in df["Expiration Date"]
    ]

    df["Days Left"] = [
        days_left(expiration_date) for expiration_date in df["Expiration Date"]
    ]

    print(df.to_string())


if __name__ == "__main__":
    main()
