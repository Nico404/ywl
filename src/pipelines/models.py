from gensim.models import Word2Vec

class Embedding:
    def word2vec_preprocessor(self, df):
        df['Chunk'] = df['Chunk'].apply(lambda x: Word2Vec(x, vector_size=10))
        return df

    # faire un fit du word2vec sur le corpus entier, puis un transform sur chaque chunk
