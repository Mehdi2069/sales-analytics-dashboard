import pandas as pd


def clean_sales_data(df):
    print("\n--- CLEANING DATA ---")

    # 1. Convert Date column
    df["Date"] = pd.to_datetime(df["Date"])

    # 2. Remove duplicates
    before = len(df)
    df.drop_duplicates(inplace=True)
    after = len(df)

    print(f"Removed {before - after} duplicate rows")

    # 3. Handle missing values
    df["Discount"] = df["Discount"].fillna(0)

    # 4. Standardize text columns
    text_columns = ["Product", "Category", "Region", "Sales_Channel", "Payment_Method"]

    for col in text_columns:
        df[col] = df[col].str.strip()

    # 5. Recalculate Revenue (validation)
    df["Revenue"] = df["Quantity"] * df["Unit_Price"] * (1 - df["Discount"])

    # 6. Recalculate Profit
    df["Profit"] = df["Revenue"] - df["Cost"]

    print("Cleaning completed.")

    return df
