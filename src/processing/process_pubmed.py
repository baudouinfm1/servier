"""
Step responsible for the processing of the pubmed file
"""

import sys
sys.path.append('/Users/baudouinfauchier-magnan/Documents/notilus/prospects/servier/servier')

from src.utils import (
    read_csv,
    find_drugs_in_title,
    OutputGraph
)
from src.config import (
    PREPROCESSED_PUBMED_FILEPATH,
    PREPROCESSED_DRUGS_FILE_PATH
)


def process_pubmed(output_graph):
    pubmed_df = read_csv(PREPROCESSED_PUBMED_FILEPATH)
    drugs_df = read_csv(PREPROCESSED_DRUGS_FILE_PATH)

    drugs_list = drugs_df['drug'].tolist()

    for index, row in pubmed_df.iterrows():
        drugs_found = find_drugs_in_title(row['title'], drugs_list)
        for drug in drugs_found:
            output_graph.add_pubmed(drug, row['id'], row['date'])
            output_graph.add_journal(drug, row['journal'], row['date'])


def main():
    """
    Applies the processing of the pubmed file
    """
    output_graph = OutputGraph()

    process_pubmed(output_graph)
    output_graph.save_to_json('data/processed_pubmed.json')


if __name__ == "__main__":
    main()