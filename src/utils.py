"""
Responsible for the implementation of utilities functions, like read_csv function.
"""

import pandas as pd
import yaml
import json


def read_csv(path_to_csv):
    df = pd.read_csv(path_to_csv)
    return df


def read_json_with_yaml(path_to_json):
    data = yaml.load(open(path_to_json))
    df = pd.DataFrame(data)
    return df


def read_json(path_to_json):
    data = json.load(open(path_to_json))
    return data


class OutputGraph:
    """
    Class implementing the output graph
    """

    def __init__(self, drugs_graph={}):
        self.drugs_graph = drugs_graph


    def add_pubmed(self, drug, pubmed_id, pubmed_date):
        if drug not in self.drugs_graph.keys():
            self.drugs_graph[drug] = {'pubmed': [{'id': pubmed_id, 'date': pubmed_date}]}
        else:
            if 'pubmed' not in self.drugs_graph[drug].keys():
                self.drugs_graph[drug]['pubmed'] = [{'id': pubmed_id, 'date': pubmed_date}]
            else:
                self.drugs_graph[drug]['pubmed'].append({'id': pubmed_id, 'date': pubmed_date})

    
    def add_clinical_trial(self, drug, clinical_trial_id, clinical_trial_date):
        if drug not in self.drugs_graph.keys():
            self.drugs_graph[drug] = {'clinical_trial': [{'id': clinical_trial_id, 'date': clinical_trial_date}]}
        else:
            if 'clinical_trial' not in self.drugs_graph[drug].keys():
                self.drugs_graph[drug]['clinical_trial'] = [{'id': clinical_trial_id, 'date': clinical_trial_date}]
            else:
                self.drugs_graph[drug]['clinical_trial'].append({'id': clinical_trial_id, 'date': clinical_trial_date})


    def add_journal(self, drug, journal_name, journal_date):
        if drug not in self.drugs_graph.keys():
            self.drugs_graph[drug] = {'journal': [{'name': journal_name, 'date': journal_date}]}
        else:
            if 'journal' not in self.drugs_graph[drug].keys():
                self.drugs_graph[drug]['journal'] = {journal_name: [journal_date]}
            else:
                if journal_name not in self.drugs_graph[drug]['journal'].keys():
                    self.drugs_graph[drug]['journal'][journal_name] = [journal_date]
                else:
                    self.drugs_graph[drug]['journal'][journal_name].append(journal_date)


    def save_to_json(self, output_file_name):
        with open(output_file_name, 'w') as outfile:
            json.dump(self.drugs_graph, outfile)