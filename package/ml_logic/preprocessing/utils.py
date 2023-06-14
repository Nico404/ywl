import re
import string
import pandas as pd
import os
from config import Config

config = Config()


#### RETRIEVE BODY FROM BOOK, CLEAN BODY ####
def body(text):
    """
    Extracts the body of a text without the header and the footer by gutenberg project
    """
    result = re.findall(r'\*\*\* START OF .+ \*\*\*(.*?)\*\*\* END OF .+ \*\*\*', text, flags=re.DOTALL)
    if result:
        body_ = result[0].strip()
    else:
        body_ = text
    return body_


#### CLEANING ####
def strip_html(text):
    '''Removes html tags from a string'''
    clean = re.compile('<.*?>')
    return re.sub(clean, '', text)

def clean_special_chars(text):
    '''Removes special chars from a string'''
    clean = re.sub(r'[\n\r\t]', '', text)
    return clean

def del_numbers(text):
    '''Removes numbers from a string'''
    clean = ''.join(char for char in text if not char.isdigit())
    return clean


#### CHUNK TEXT ####
def chunk_text(text: str, chunk_size=256) -> list[str]:
    '''Chunking data into chunks of specified word count'''
    words = text.split()  # Split the text into individual words
    chunks = list()
    current_chunk = list()

    for word in words:
        current_chunk.append(word)  # Add the word to the current chunk
        if len(current_chunk) == chunk_size:
            chunks.append(" ".join(current_chunk))  # Add the completed chunk to the list
            current_chunk = list()  # Reset current
    return chunks
