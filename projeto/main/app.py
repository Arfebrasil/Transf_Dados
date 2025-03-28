import compress_csv
import extract
import replace


def main() -> None:

    PATH = extract.pdf_to_csv()
    replace.replace_words(PATH)
    compress_csv.zip_csv(PATH)


main()
