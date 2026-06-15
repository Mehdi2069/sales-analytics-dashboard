import pandas as pd

def audit_data(df):
    print("\n--- DATA INFO ---")
    print(df.info())

    print("\n--- MISSING VALUES ---")
    print(df.isnull().sum())

    print("\n--- DUPLICATES ---")
    print(df.duplicated().sum())

    print("\n--- STATISTICS ---")
    print(df.describe())

    print("\n--- SAMPLE DATA ---")
    print(df.head())