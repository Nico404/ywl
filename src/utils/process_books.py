import os
import pandas as pd
from config.config import Config

config = Config()

def read_book(book_id: str) -> str:
    '''Read book from file'''
    file_name = os.path.join(config.BOOKS_SHORTLIST_PATH, book_id)
    with open(file_name, 'r') as file:
        return file.read()

def get_author_name(filename:str) -> str:
    '''Get author name from filename'''
    filename = filename.split('.')[0]    # remove extension in 2236.txt
    with open(os.path.join(config.DATA_PROCESSED_PATH, 'books_metadata.csv'), 'r') as file:
        for line in file:
            if filename in line:
                return line.split(',')[2] # return author name

def process_books() -> None:
    ''' Process books and save them to csv '''
    data = list()
    book_files = os.listdir(config.BOOKS_SHORTLIST_PATH) # List[str] of all files in dir
    for file in book_files:
        author_name = get_author_name(file)
        book_text = read_book(file)
        # make a csv file with 2 columns (author, book_text)
        data.append({"Author": author_name, "Book": book_text})
    df = pd.DataFrame(data)
    df.to_csv(os.path.join(config.DATA_PROCESSED_PATH, 'books_processed.csv'), index=False)
    print('Books processed and saved to books_processed.csv')

if __name__ == '__main__':
    process_books()
