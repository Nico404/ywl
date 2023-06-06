import pandas as pd
import os
from config.config import Config

config = Config()

def get_author_name(filename:str) -> str:
    '''Get author name from filename'''
    filename = filename.split('.')[0]    # remove extension in 2236.txt
    with open(os.path.join(config.DATA_PROCESSED_PATH, 'books_metadata.csv'), 'r') as file:
        for line in file:
            if filename in line:
                return line.split(',')[2] # return author name

def read_book(book_id: str) -> str:
    '''Read book from file'''
    file_name = os.path.join(config.BOOKS_SHORTLIST_PATH, book_id)
    with open(file_name, 'r') as file:
        return file.read()

def chunk_text(text: str, chunk_size=256) -> list[str]:
    '''Chunking data into chunks of size chunk_size'''
    chunks = list()
    for i in range(0, len(text), chunk_size):
        chunks.append(text[i:i + chunk_size])
    print(str(len(chunks)) + ' chunks created')
    return chunks

def save_all_books_to_dataframe() -> pd.DataFrame:
    data = list()
    book_files = os.listdir(config.BOOKS_SHORTLIST_PATH) # List[str] of all files in dir
    for file in book_files:
        author_name = get_author_name(file)
        book_text = read_book(file)
        chunks = chunk_text(book_text)
        for i, chunk in enumerate(chunks):
            data.append({"Author": author_name, "Chunk": chunk})
    df = pd.DataFrame(data)
    return df

def make_final_dataset(df: pd.DataFrame) -> pd.DataFrame:
    '''Make final dataset with 6000 chunks per author'''
    df_final = pd.DataFrame()
    most_famous = ['Shakespeare William',
                   'Montgomery L. M. (Lucy Maud)',
                   'Wilde Oscar',
                   'Dickens Charles',
                   'Fitzgerald F. Scott (Francis Scott)',
                   'Twain Mark',
                   'Plato',
                   'Homer',
                   'Tolstoy Leo graf',
                   'Austen Jane']

    for author in most_famous:
        df_author = df[df['Author'] == author]
        df_author = df_author[:6000]
        df_final = pd.concat([df_final, df_author])

    df_final.rename(columns={'Author': 'y', 'Chunk': 'X'}, inplace=True)
    return df_final


if __name__ == '__main__':
    df = save_all_books_to_dataframe()
    df = make_final_dataset(df)
    df.to_csv(os.path.join(config.DATA_PROCESSED_PATH, 'books_processed.csv'), index=False)
    print('Dataset saved to ' + os.path.join(config.DATA_PROCESSED_PATH, 'books_processed.csv'))
