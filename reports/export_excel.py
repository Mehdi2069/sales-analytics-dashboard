from io import BytesIO
import pandas as pd


def export_to_excel(df):
    """
    Export DataFrame to Excel format for Streamlit download.
    Returns Excel file as bytes.
    """

    output = BytesIO()

    with pd.ExcelWriter(
        output,
        engine="openpyxl"
    ) as writer:
        df.to_excel(
            writer,
            index=False,
            sheet_name="Sales Data"
        )

    output.seek(0)

    return output.getvalue()
