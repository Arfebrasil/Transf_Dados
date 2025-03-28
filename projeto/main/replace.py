import pandas


def replace_words():

    df = pandas.read_csv("projeto/csv/main.csv")

    df.replace(
        {
            "Seg. Ambulatorial": {"AMB": "Seg. Ambulatorial"},
            "Seg. Odontológica": {"OD": "Seg. Odontológica"},
        },
        regex=True,
        inplace=True,
    )

    df.to_csv("projeto/csv/main.csv", index=False)


if __name__ == "__main__":

    replace_words()
