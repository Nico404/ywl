from gensim.models import Word2Vec, KeyedVectors
import gensim.downloader as api
import pandas as pd


class Models:
    def word2vec_model_100_12_1(self, df : pd.DataFrame, vector_size=100, window=12, min_count=1) -> pd.DataFrame:
        wordtovec = Word2Vec(df['Book'], vector_size=vector_size, window=window, min_count=min_count)
        df['Book'] = df['Book'].apply(lambda x: [wordtovec.wv[word] for word in x if word in wordtovec.wv])
        return df

    def word2vec_model_200_12_2(self, df : pd.DataFrame, vector_size=200, window=12, min_count=2) -> pd.DataFrame:
        wordtovec = Word2Vec(df['Book'], vector_size=vector_size, window=window, min_count=min_count)
        df['Book'] = df['Book'].apply(lambda x: [wordtovec.wv[word] for word in x if word in wordtovec.wv])
        return df

    # word2vec-google-news-300
    # def word2vec_model_pretrained(self, df : pd.DataFrame) -> pd.DataFrame:
    #     return df

    # def glove_model_(self, df : pd.DataFrame) -> pd.DataFrame:
    #     # TBD our version
    #     return df

    # def glove_model_pretrained(self, df : pd.DataFrame) -> pd.DataFrame:
    #     path = api.load("glove-twitter-25", return_path=True) # replace with local
    #     wordtovec = KeyedVectors.load_word2vec_format(path, binary=True)
    #     df['Book'] = df['Book'].apply(lambda x: [wordtovec[word] for word in x if word in wordtovec])
    #     return df
