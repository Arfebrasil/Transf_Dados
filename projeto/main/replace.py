import pandas


def replace_words(
    PATH,
) -> None:  # opens the file and replace OD and AMB ONLY in the corresponding column

    df = pandas.read_csv(PATH)  # use pandas to read the csv

    df.replace(
        {
            "Seg. Ambulatorial": {"AMB": "Seg. Ambulatorial"},
            "Seg. Odontológica": {"OD": "Seg. Odontológica"},
        },
        regex=True,
        inplace=True,
    )  # defines which column will change which word for what

    df.to_csv(PATH, index=False)  # reloads the file


if __name__ == "__main__":  # module management

    replace_words()
