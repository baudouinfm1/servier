"""
Responsible for the implementation of utilities functions, like read_csv function.
"""

import pandas as pd
import yaml


def read_csv(path_to_csv):
    df = pd.read_csv(path_to_csv)
    return df


def read_json(path_to_json):
    data = yaml.load(open(path_to_json))
    df = pd.DataFrame(data)
    return df