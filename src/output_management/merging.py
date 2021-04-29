"""
Last step: responsible for the merging of the processed files
"""

from src.utils import (
    read_json,
    OutputGraph
)
from src.config import (
    PROCESSED_PUBMED_FILEPATH,
    PROCESSED_CLINICAL_TRIALS_FILE_PATH,
    OUTPUT_FILE_PATH
)


def merge_graphs():
    pubmed_graph = read_json(PROCESSED_PUBMED_FILEPATH)
    clinical_trials_graph = read_json(PROCESSED_CLINICAL_TRIALS_FILE_PATH)

    for drug in clinical_trials_graph.keys():
        if drug not in pubmed_graph.keys():
            pubmed_graph[drug] = clinical_trials_graph[drug]
        else:
            if 'clinical_trial' in clinical_trials_graph[drug].keys():
                pubmed_graph[drug]['clinical_trial'] = clinical_trials_graph[drug]['clinical_trial']
            if 'journal' in clinical_trials_graph[drug].keys():
                if 'journal' not in pubmed_graph[drug].keys():
                    pubmed_graph[drug]['journal'] = clinical_trials_graph[drug]['journal']
                else:
                    for journal in clinical_trials_graph[drug]['journal'].keys():
                        if journal in pubmed_graph[drug]['journal'].keys():
                            pubmed_graph[drug]['journal'][journal] += clinical_trials_graph[drug]['journal'][journal]
                        else:
                            pubmed_graph[drug]['journal'][journal] = clinical_trials_graph[drug]['journal'][journal]
    
    return pubmed_graph


def main():
    """
    Applies the merging of the output files
    """

    merged_graphs = merge_graphs()
    output_graph = OutputGraph(merged_graphs)
    output_graph.save_to_json(OUTPUT_FILE_PATH)


if __name__ == "__main__":
    main()