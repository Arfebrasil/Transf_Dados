import pandas as pd


def csv_to_excel() -> (
    None
):  # for better visualziation, turns csv table into excel "table"

    csv = pd.read_csv("projeto/csv/test.csv")  # reads the csv in the folder
    csv.to_excel(
        "test.xls", index=False, engine="openpyxl"
    )  # turn csv into a excel table creating a file
