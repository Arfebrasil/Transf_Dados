import compress_csv
import extract
import replace


def main() -> (
    None
):  # runs the intire application for easier use / You can also run the program using main order with the Path

    PATH = (
        extract.pdf_to_csv()
    )  # reads through the pdf and creates csv based in each table row
    replace.replace_words(
        PATH
    )  # opens csv for raplacing OD and AMD ONLY in the corresponding column
    compress_csv.zip_csv(PATH)  # compress the csv in to a simple zip


main()
