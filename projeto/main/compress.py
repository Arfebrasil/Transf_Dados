import zipfile


def zip_csv(CSV_FILE):

    with zipfile.ZipFile(
        "Teste_Arthur_Ferreira.zip", "w", zipfile.ZIP_DEFLATED
    ) as zipcsv:
        zipcsv.write(CSV_FILE)


if __name__ == "__main__":

    zip_csv("projeto/csv/main.csv")
