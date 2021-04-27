"""
Step responsible for the preprocessing of the pubmed file
"""

import sys
sys.path.append('/Users/baudouinfauchier-magnan/Documents/notilus/prospects/servier/servier')
from src.config import (
    PUBMED_CSV_FILE_PATH,
    PUBMED_JSON_FILE_PATH,
    PREPROCESSED_PUBMED_FILEPATH
)
from src.utils import (
    read_csv,
    read_json
)

import pandas as pd

def preprocess_pubmed_csv():
    """
    Loads the pubmed csv file and preprocesses it

    :returns: a dataframe with clean data on pubmed
    :rtype: pandas.DataFrame
    """
    pubmed_df = read_csv(PUBMED_CSV_FILE_PATH)
    pubmed_df['title'] = pubmed_df['title'].str.lower()
    return pubmed_df


def preprocess_pubmed_json():
    """
    Loads the pubmed json file and preprocesses it

    :returns: a dataframe with clean data on pubmed
    :rtype: pandas.DataFrame
    """
    pubmed_df = read_json(PUBMED_JSON_FILE_PATH)

    pubmed_df['title'] = pubmed_df['title'].str.lower()

    pubmed_df['id'] = pd.to_numeric(pubmed_df['id'], errors='coerce')
    pubmed_df = pubmed_df[~pubmed_df['id'].isna()]
    pubmed_df['id'] = pubmed_df['id'].astype(int)
    
    return pubmed_df


def main():
    """
    applies the preprocessing for the pubmed file

    :returns: a dataframe with clean data on pubmed
    :rtype: pandas.DataFrame
    """

    preprocessed_csv_file = preprocess_pubmed_csv()
    preprocessed_json_file = preprocess_pubmed_json()

    preprocessed_file = pd.concat([preprocessed_csv_file, preprocessed_json_file])

    preprocessed_file.to_csv(PREPROCESSED_PUBMED_FILEPATH, index=False)


if __name__ == "__main__":
    main()