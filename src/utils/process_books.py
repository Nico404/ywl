import os
import pandas as pd
import json
from config.config import Config
import sys

config = Config()

def stage_top_authors() -> None:
    '''Bring our top authors books to a separate shortlist folder'''
    author_list = ['Shakespeare William',
               'Montgomery L. M. (Lucy Maud)',
               'Wilde Oscar',
               'Dickens Charles',
               'Fitzgerald F. Scott (Francis Scott)',
               'Twain Mark',
               'Plato',
               'Homer',
               'Tolstoy Leo graf',
               'Austen Jane']

    books_df = pd.read_csv(os.path.join(config.DATA_PROCESSED_PATH, 'books_metadata.csv'), names=['id', 'title', 'author', 'subjects', 'languages', 'formats', 'download_count'])
    books_df = books_df[books_df['author'].isin(author_list)]

    book_list = books_df['id'].tolist() # list of all books from the most famous authors 472

    for book in book_list:
        print(f'Copying {config.BOOKS_RAW_PATH}{book}.txt to {config.BOOKS_SHORTLIST_PATH}{book}.txt')
        # copy files from data/raw/books to data/raw/books_shortlist
        os.system(f"cp {config.BOOKS_RAW_PATH}{book}.txt {config.BOOKS_SHORTLIST_PATH}{book}.txt 2>/dev/null")


def build_lookup_table() -> None:
    '''Build lookup table from metadata'''
    lookup_authors = dict()

    metadata = pd.read_csv(os.path.join(config.DATA_PROCESSED_PATH, 'books_metadata.csv'), names=['id', 'title', 'author', 'subjects', 'languages', 'formats', 'download_count'])
    metadata = metadata[['id', 'author']]

    for _, row in metadata.iterrows():
        lookup_authors[row['id']] = row['author']

    with open(os.path.join(config.DATA_PROCESSED_PATH, 'lookup_authors.json'), 'w') as file:
        json.dump(lookup_authors, file)

    print(f'Lookup table saved to {os.path.join(config.DATA_PROCESSED_PATH, "lookup_authors.json")}')


def read_book(book_id: str) -> str:
    '''Read book from file'''
    file_name = os.path.join(config.BOOKS_SHORTLIST_PATH, book_id)
    with open(file_name, 'r') as file:
        return file.read()


def get_author_name(filename:str) -> str:
    '''Get author name from filename with custom lookup table'''
    filename = filename.split('.')[0]    # remove extension in 2236.txt

    with open(os.path.join(config.DATA_PROCESSED_PATH, 'lookup_authors.json'), 'r') as file:
        file = json.load(file)
        print(file)
    return file[filename]


def process_books_from_shortlist(filename:str) -> None:
    ''' Process books and save them to a csv file you name for later use as df '''
    data = list()
    book_files = os.listdir(config.BOOKS_SHORTLIST_PATH) # List[str] of all files in dir

    with open(os.path.join(config.DATA_PROCESSED_PATH, 'lookup_authors.json'), 'r') as file:
        lookup_authors = json.load(file) # load lookup table

    for file in book_files:
        author_name = get_author_name(file)
        book_text = read_book(file)
        print(f'Processing author {author_name} and {book_text}')
        data.append({"Author": author_name, "Book": book_text}) # make a csv file with 2 columns (Author, Book)

    df = pd.DataFrame(data)
    df.to_csv(os.path.join(config.DATA_PROCESSED_PATH, filename + ".csv"), index=False)
    print(f'Books processed and saved to {os.path.join(config.DATA_PROCESSED_PATH, filename + ".csv")}')

if __name__ == '__main__':
    # build_lookup_table()
    process_books_from_shortlist('books_processed')
    # stage_top_authors()
