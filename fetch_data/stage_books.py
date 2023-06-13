import os
import pandas as pd
from config import Config

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


def stage_top40_authors() -> None:
    '''Bring our top authors books to a separate top40 folder'''
    author_list = ['Motley John Lothrop',
                    'Twain Mark',
                    'Shakespeare William',
                    'Ebers Georg',
                    'Larned J. N. (Josephus Nelson)',
                    'Zola Émile',
                    'Dumas Alexandre',
                    'Fishburne William Brett',
                    'Grant Ulysses S. (Ulysses Simpson)',
                    'Thomas Aquinas Saint',
                    'Tolstoy Leo graf',
                    'Steele Richard Sir',
                    'Walsh James J. (James Joseph)',
                    'Holmes Oliver Wendell',
                    'Whittier John Greenleaf',
                    'Warner Charles Dudley',
                    'Plutarch',
                    'Hardy Thomas',
                    'Browning Robert',
                    'Benton Thomas Hart',
                    'Auerbach Berthold',
                    'Wood J. G. (John George)',
                    'Lincoln Abraham',
                    'Rose J. Holland (John Holland)',
                    'Haeckel Ernst',
                    'Smith Adam',
                    'Montaigne Michel de',
                    'Shelley Percy Bysshe',
                    'Mill John Stuart',
                    'Whewell William',
                    'Brown Goold',
                    'Poe Edgar Allan',
                    'Rose Joshua',
                    'Josephus Flavius',
                    'Lewis Meriwether',
                    'Spenser Edmund',
                    'Lemprière John',
                    'Polo Marco',
                    'Nuttall P. Austin',
                    'Rymer James Malcolm']


    books_df = pd.read_csv(os.path.join(config.DATA_PROCESSED_PATH, 'books_metadata.csv'), names=['id', 'title', 'author', 'subjects', 'languages', 'formats', 'download_count'])
    books_df = books_df[books_df['author'].isin(author_list)]

    book_list = books_df['id'].tolist() # list of all books from the most famous authors

    for book in book_list:
        print(f'Copying {config.BOOKS_RAW_PATH}{book}.txt to {config.BOOKS_TOP40_PATH}{book}.txt')
        # copy files from data/raw/books to data/raw/books_top40
        os.system(f"cp {config.BOOKS_RAW_PATH}{book}.txt {config.BOOKS_TOP40_PATH}{book}.txt 2>/dev/null")

if __name__ == '__main__':
    stage_top_authors()
    stage_top40_authors()
