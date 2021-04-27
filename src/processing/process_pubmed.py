"""
Step responsible for the processing of the pubmed file
"""

from src.utils import read_csv
from src.config import 


def find_drugs_in_title(title, drugs_list):
    """
    Finds all the drugs in the title and returns them as a list
    """
    drugs_found = []

    title_words = title.split()
    for word in title_words:
        if word in drugs_list:
            drugs_found.append(word)
    
    return drugs_found


def process_pubmed():
    pubmed_df = read_csv(PREPROCESSED_PUBMED_FILEPATH)
    drugs_df = read_csv(PREPROCESSED_DRUGS_FILE_PATH)

    drugs_list = pubmed_df['drug'].tolist()

    for row in pubmed_df.iterrows():
        drugs_found = find_drugs_in_title(row['title'], drugs_list)


def main():
    """
    Applies the processing of the pubmed file
    """


if __name__ == "__main__":
    main()