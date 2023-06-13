import json
import os
import pandas as pd
from config import Config

config = Config()

def build_lookup_table_top40() -> None:
    '''Build lookup table from metadata'''
    lookup_authors = dict()

    metadata = pd.read_csv(os.path.join(config.DATA_PROCESSED_PATH, 'books_metadata.csv'), names=['id', 'title', 'author', 'subjects', 'languages', 'formats', 'download_count'])
    metadata = metadata[['id', 'author']]

    for _, row in metadata.iterrows():
        lookup_authors[row['id']] = row['author']

    with open(os.path.join(config.DATA_PROCESSED_PATH, 'lookup_authors_top40.json'), 'w') as file:
        json.dump(lookup_authors, file)

    print(f'Lookup table saved to {os.path.join(config.DATA_PROCESSED_PATH, "lookup_authors.json")}')

def build_lookup_table() -> None:
    '''Build lookup table from metadata'''
    lookup_authors = dict()

    metadata = pd.read_csv(os.path.join(config.DATA_PROCESSED_PATH, 'books_metadata.csv'), names=['id', 'title', 'author', 'subjects', 'languages', 'formats', 'download_count'])
    metadata = metadata[['id', 'author']] # keep only relevant columns

    for _, row in metadata.iterrows():
        lookup_authors[row['id']] = row['author']

    with open(os.path.join(config.DATA_PROCESSED_PATH, 'lookup_authors.json'), 'w') as file:
        json.dump(lookup_authors, file)

    print(f'Lookup table saved to {os.path.join(config.DATA_PROCESSED_PATH, "lookup_authors.json")}')
