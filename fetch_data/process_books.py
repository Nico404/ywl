import os
import pandas as pd
import json
from config import Config
import sys

config = Config()


def read_book(book_id: str) -> str:
    '''Read book from file'''
    file_name = os.path.join(config.BOOKS_SHORTLIST_PATH, book_id)
    with open(file_name, 'r') as file:
        return file.read()

def read_book_top40(book_id: str) -> str:
    '''Read book from file'''
    file_name = os.path.join(config.BOOKS_TOP40_PATH, book_id)
    with open(file_name, 'r') as file:
        return file.read()


def get_author_name(filename:str) -> str:
    '''Get author name from filename with custom lookup table'''
    filename = filename.split('.')[0]    # remove extension in 2236.txt

    with open(os.path.join(config.DATA_PROCESSED_PATH, 'lookup_authors.json'), 'r') as file:
        file = json.load(file)
        print(file)
    return file[filename]

def get_author_name_top40(filename:str) -> str:
    '''Get author name from filename with custom lookup table'''
    filename = filename.split('.')[0]    # remove extension in 2236.txt

    with open(os.path.join(config.DATA_PROCESSED_PATH, 'lookup_authors_top40.json'), 'r') as file:
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


def process_books_from_top40(filename:str) -> None:
    ''' Process books and save them to a csv file you name for later use as df '''
    data = list()
    book_files = os.listdir(config.BOOKS_TOP40_PATH) # List[str] of all files in dir

    with open(os.path.join(config.DATA_PROCESSED_PATH, 'lookup_authors_top40.json'), 'r') as file:
        lookup_authors = json.load(file) # load lookup table

    for file in book_files:
        try:
            author_name = get_author_name_top40(file)
            book_text = read_book_top40(file)
            data.append({"Author": author_name, "Book": book_text}) # make a csv file with 2 columns (Author, Book)
            print(f'Processing author {author_name} and {book_text}')
        except Exception as e:
            print(f'Error processing file {file}: {str(e)}')

    df = pd.DataFrame(data)
    df.to_csv(os.path.join(config.DATA_PROCESSED_PATH, filename + ".csv"), index=False)
    print(f'Books processed and saved to {os.path.join(config.DATA_PROCESSED_PATH, filename + ".csv")}')


if __name__ == '__main__':
    process_books_from_shortlist('books_processed')

    process_books_from_top40('books_processed_top40')
