import pandas as pd
import os
from config.config import Config

config = Config()

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

    # print(str(len(chunks)) + ' chunks created')

    return chunks
