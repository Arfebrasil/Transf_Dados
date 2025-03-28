import csv

import pdfplumber

PDF = "projeto/files/Anexo_I.pdf"  # pdf path

TABLE_COOR = (50, 130, 1370, 780)  # default coordinates for every table in Anexo I

RANGE_OF_PAGES = range(2, 181)  # total pages


def pdf_to_csv() -> (
    None
):  # get every table from anexo and append it rows in the main.csv (headers not include)

    def create_base_csv() -> (
        str
    ):  # creates the main.csv, so no errors can occur, returns the path of the csv

        CSV_FOLDER = "projeto/csv/"  # csv path

        CSV_STRUCTURE = 'PROCEDIMENTO,"RN (alteração)",VIGÊNCIA,"Seg. Odontológica","Seg. Ambulatorial",HCO,HSO,REF,PAC,DUT,SUBGRUPO,GRUPO,CAPÍTULO'  # csv headers

        with open(
            f"{CSV_FOLDER}main.csv", "w", encoding="utf-8"
        ) as csv_file:  # creates the file
            csv_file.write(CSV_STRUCTURE)  # with the headers

        return f"{CSV_FOLDER}main.csv"  # also returns the csv path

    PATH = create_base_csv()  # first defining the path of csv

    with pdfplumber.open(PDF) as pdf:  # opens the pdf

        for (
            page
        ) in (
            RANGE_OF_PAGES
        ):  # a loop for every page in range of pages (get_number_of_pages can be included in other versions)

            table_box = pdf.pages[page].crop(
                TABLE_COOR
            )  # defines the area of each page that will be scanned

            table_content = (
                table_box.extract_table()
            )  # create a array of arrays(each array is a row of the table)

            with open(
                PATH, "a", newline="", encoding="utf-8"
            ) as file:  # opens the file

                file.write("\n")

                for (
                    row
                ) in (
                    table_content
                ):  # for each row in table_content write the row as csv

                    writer = csv.writer(file)

                    writer.writerow(row)


if __name__ == "__main__":

    pdf_to_csv()
