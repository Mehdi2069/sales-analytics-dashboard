try:
    import pandas as pd
except ImportError:
    raise ImportError(
        "pandas is required to run audit_data. Install it with: pip install pandas"
    )

def audit_data(df):
    print("\n--- DATA INFO ---")
    # df.info() prints directly; avoid printing its None return value
    df.info()

    print("\n--- MISSING VALUES ---")
    print(df.isnull().sum())

    print("\n--- DUPLICATES ---")
    print(df.duplicated().sum())

    print("\n--- STATISTICS ---")
    print(df.describe())

    print("\n--- SAMPLE DATA ---")
    print(df.head())