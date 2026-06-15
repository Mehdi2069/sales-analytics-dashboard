import pandas as pd

def clean_sales_data(df):
    df["Date"] = pd.to_datetime(df["Date"])

    df.drop_duplicates(inplace=True)

    df.fillna({
        "Discount": 0
    }, inplace=True)

    df["Product"] = df["Product"].str.strip()
    df["Category"] = df["Category"].str.strip()
    df["Region"] = df["Region"].str.strip()

    df["Revenue"] = df["Quantity"] * df["Unit_Price"] * (1 - df["Discount"])
    df["Profit"] = df["Revenue"] - df["Cost"]

    return df