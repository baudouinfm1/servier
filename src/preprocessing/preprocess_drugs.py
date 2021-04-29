"""
Step responsible for the preprocessing of the drugs file
"""

from src.config import (
    DRUGS_INPUT_FILE_PATH,
    PREPROCESSED_DRUGS_FILE_PATH
)
from src.utils import read_csv

def preprocess_drugs():
    """
    Loads the drugs file and preprocesses it

    :returns: a dataframe with clean data on drugs
    :rtype: pandas.DataFrame
    """
    drugs_df = read_csv(DRUGS_INPUT_FILE_PATH)
    drugs_df['drug'] = drugs_df['drug'].str.lower()
    return drugs_df


def main():
    """
    applies the preprocessing for the drugs file

    :returns: a dataframe with clean data on drugs
    :rtype: pandas.DataFrame
    """

    preprocessed_file = preprocess_drugs()

    preprocessed_file.to_csv(PREPROCESSED_DRUGS_FILE_PATH, index=False)


if __name__ == "__main__":
    main()