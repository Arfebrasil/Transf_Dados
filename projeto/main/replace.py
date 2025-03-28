import pandas


def replace_words(PATH) -> None:

    df = pandas.read_csv(PATH)

    df.replace(
        {
            "Seg. Ambulatorial": {"AMB": "Seg. Ambulatorial"},
            "Seg. Odontológica": {"OD": "Seg. Odontológica"},
        },
        regex=True,
        inplace=True,
    )

    df.to_csv(PATH, index=False)


if __name__ == "__main__":

    replace_words()
