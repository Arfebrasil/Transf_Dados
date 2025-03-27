import csv
import pdfplumber

PDF = "projeto/files/Anexo_I.pdf"

TABLE_COOR = (50, 130, 1370, 780)

RANGE_OF_PAGES = range(2, 181)


def pdf_to_csv() -> None:

    def create_base_csv() -> str:

        CSV_FOLDER = "projeto/csv/"

        CSV_STRUCTURE = 'PROCEDIMENTO,"RN (alteração)",VIGÊNCIA,"Seg. Odontológica","Seg. Ambulatorial",HCO,HSO,REF,PAC,DUT,SUBGRUPO,GRUPO,CAPÍTULO'

        with open(f"{CSV_FOLDER}main.csv") as csv:
            csv.write(CSV_STRUCTURE, "w", encoding="utf-8")

        return f"{CSV_FOLDER}main.csv"

    def indent() -> None:

        with open(f"{PATH}", "a") as file:
            file.write("\n")

    PATH = create_base_csv()

    with pdfplumber.open(PDF) as pdf:

        for page in RANGE_OF_PAGES:

            table_box = pdf.pages[page].crop(TABLE_COOR)

            table_content = table_box.extract_table()

            indent()

            for row in table_content:

                with open(f"{PATH}", "a", newline="", encoding="utf-8") as file:

                    writer = csv.writer(file)

                    writer.writerow(row)
