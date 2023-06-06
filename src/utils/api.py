import requests
import os
from bs4 import BeautifulSoup
import pandas as pd
from config.config import Config
from typing import Tuple, List, Dict


config = Config()

def save_last_next(next_page_token: str) -> None:
    ''' Save last next token to file '''
    with open(config.last_next_token_path, 'w') as file:
        file.write(next_page_token)

def load_last_next() -> str:
    ''' Load last next token from file '''
    with open(config.last_next_token_path, 'r') as file:
        return file.read()

def dl_books_from_page(endpoint: str) -> Tuple[List, str]:
    ''' Download json of the page and return books and next token '''
    response = requests.get(endpoint)
    if response.status_code == 200:
        books_data = response.json()
        next_token = books_data['next']
        books = books_data['results']
        return books, next_token
    else:
        return None, None

def parse_books_from_json(json: List[Dict]) -> List[Dict]:
    ''' Parse books from json page to list of dict '''
    books = list()
    for book in json:
        if 'text/plain' in book['formats'] and book['authors']: # making sure the book has a text/plain format and an author
            books.append({
                'id': book['id'],
                'title': book['title'],
                'authors': book['authors'][0]['name'],
                'subjects': book['subjects'],
                'languages': book['languages'],
                'formats': book['formats']['text/plain'],
                'download_count': book['download_count']
            })
    return books

def save_book_from_url(url: str) -> None:
    ''' Save book from formats-URL to data/raw folder'''
    response = requests.get(url)
    if response.status_code == 200:
        file_name_with_extension = os.path.basename(url)
        file_name, extension = os.path.splitext(file_name_with_extension)
        file_path = os.path.join(config.data_raw_path_global_fr,file_name)
        with open(file_path, 'w') as file:
            file.write(response.text.encode('utf-8').decode('utf-8'))

def download_all_books() -> None:
    ''' Download all books from the website, save them as .txt files and return a csv with the books metadata'''
    next_page = load_last_next() # load last next token from file
    while next_page:
        books, next_page = dl_books_from_page(next_page) # download books and get next from the page
        save_last_next(next_page) # save next to file
        if books:
            parsed_books = parse_books_from_json(books)
            for book in parsed_books:
                download_url = book['formats']
                save_book_from_url(download_url)
                print(book['title'], '... downloaded')

                # save each book as a row in a csv file
                with open(os.path.join(config.data_processed_path, 'books.csv'), 'a') as file:
                    subjects_str = ', '.join(book['subjects']).replace('"', '').replace(',', '')
                    title = book['title'].replace('"', '').replace(',', '')
                    authors = book['authors'].replace('"', '').replace(',', '')
                    languages = book['languages'][0]
                    formats = book['formats'].replace('"', '').replace(',', '')

                    file.write(f"{book['id']},{title},{authors},{subjects_str},{languages},{formats},{book['download_count']}\n")

if __name__ == "__main__":
    download_all_books()
