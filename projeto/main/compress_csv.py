import zipfile


def zip_csv(CSV_FILE: str) -> None:

    with zipfile.ZipFile(
        "projeto/Teste_Arthur_Ferreira.zip", "w", zipfile.ZIP_DEFLATED
    ) as zipcsv:  # creates the zip file
        zipcsv.write(CSV_FILE)  # then creates a csv file in the zip


if __name__ == "__main__":  # module management

    zip_csv("projeto/csv/main.csv")
