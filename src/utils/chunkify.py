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

    print(str(len(chunks)) + ' chunks created')

    return chunks

# def make_final_dataset(df: pd.DataFrame) -> pd.DataFrame:
#     '''Make final dataset with 6000 chunks per author'''
#     df_final = pd.DataFrame()
#     most_famous = ['Shakespeare William',
#                    'Montgomery L. M. (Lucy Maud)',
#                    'Wilde Oscar',
#                    'Dickens Charles',
#                    'Fitzgerald F. Scott (Francis Scott)',
#                    'Twain Mark',
#                    'Plato',
#                    'Homer',
#                    'Tolstoy Leo graf',
#                    'Austen Jane']

#     for author in most_famous:
#         df_author = df[df['Author'] == author]
#         df_author = df_author[:6000]
#         df_final = pd.concat([df_final, df_author])

#     df_final.rename(columns={'Author': 'y', 'Chunk': 'X'}, inplace=True)
#     return df_final
