"""
Step responsible for the processing of the clinical trial file
"""

import sys
sys.path.append('/Users/baudouinfauchier-magnan/Documents/notilus/prospects/servier/servier')

from src.utils import (
    read_csv,
    OutputGraph
)
from src.processing.utils import find_drugs_in_title
from src.config import (
    PREPROCESSED_CLINICAL_TRIALS_FILE_PATH,
    PREPROCESSED_DRUGS_FILE_PATH,
    PROCESSED_CLINICAL_TRIALS_FILE_PATH
)


def process_clinical_trial(output_graph):
    clinical_trial_df = read_csv(PREPROCESSED_CLINICAL_TRIALS_FILE_PATH)
    drugs_df = read_csv(PREPROCESSED_DRUGS_FILE_PATH)

    drugs_list = drugs_df['drug'].tolist()

    for index, row in clinical_trial_df.iterrows():
        drugs_found = find_drugs_in_title(row['scientific_title'], drugs_list)
        for drug in drugs_found:
            output_graph.add_clinical_trial(drug, row['id'], row['date'])
            output_graph.add_journal(drug, row['journal'], row['date'])


def main():
    """
    Applies the processing of the clinical trial file
    """
    output_graph = OutputGraph()

    process_clinical_trial(output_graph)
    output_graph.save_to_json(PROCESSED_CLINICAL_TRIALS_FILE_PATH)


if __name__ == "__main__":
    main()