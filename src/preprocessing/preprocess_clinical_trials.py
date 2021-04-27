"""
Step responsible for the preprocessing of the clinical trials file
"""

import sys
sys.path.append('/Users/baudouinfauchier-magnan/Documents/notilus/prospects/servier/servier')
from src.config import (
    CLINICAL_TRIALS_INPUT_FILE_PATH,
    PREPROCESSED_CLINICAL_TRIALS_FILE_PATH
)
from src.utils import read_csv

def preprocess_clinical_trials():
    """
    Loads the clinical_trials file and preprocesses it

    :returns: a dataframe with clean data on clinical_trials
    :rtype: pandas.DataFrame
    """
    clinical_trials_df = read_csv(CLINICAL_TRIALS_INPUT_FILE_PATH)
    clinical_trials_df['scientific_title'] = clinical_trials_df['scientific_title'].str.lower()

    # Remove byte-like characters
    clinical_trials_df['scientific_title'] = clinical_trials_df['scientific_title'].apply(lambda x: x.replace('\\xc3', ''). replace('\\xb1', ''))
    clinical_trials_df['journal'] = clinical_trials_df['journal'].astype(str).apply(lambda x: x.replace('\\xc3', ''). replace('\\x28', ''))

    return clinical_trials_df


def main():
    """
    applies the preprocessing for the clinical_trials file

    :returns: a dataframe with clean data on clinical_trials
    :rtype: pandas.DataFrame
    """

    preprocessed_file = preprocess_clinical_trials()

    preprocessed_file.to_csv(PREPROCESSED_CLINICAL_TRIALS_FILE_PATH, index=False)


if __name__ == "__main__":
    main()