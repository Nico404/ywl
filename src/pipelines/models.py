from gensim.models import Word2Vec

class Models:
    def word2vec(self, df):
        df['Book'] = df['Book'].apply(lambda x: Word2Vec(x, vector_size=10))
        return df

    # faire un fit du word2vec sur le corpus entier, puis un transform sur chaque chunk
