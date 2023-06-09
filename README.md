
# YouWriteLike

A NLP project, from scrapping to training, that aims to classify text style into 40 author classes. We have built a few models that can predict which writer's style is closest to your own writing style. Now, play, write, and learn!

You can try it out here: https://youwritelike.streamlit.app




## Demo

Watch our live demo to get a grasp of the entire project:
[![youwritelike](https://images.itnewsinfo.com/lmi/articles/grande/000000080406.jpg)](https://www.youtube.com/watch?v=5VZa8K2afMg&t=336s&ab_channel=PouetPouet "Click to Watch!")


## How it works

 ### Fetch Data

- Run **make download_all_books** to download all books from the gutenberg project.

The file fetch_data/checkpoint/last_next_token.txt needs to be populated with the starting endpoint of the api https://gutendex.com/books?languages=en,fr.

- Once the process has started, the last token will be replaced by the latest page https://gutendex.com/books/?languages=en%2Cfr%0A&page=5.
It allows for the scrapping process to be paused and restarted.

- **make stage_books** will stage only the list of authors that we want to work on from data/raw/books to data/raw/books_shortlist

 - **make process_books** will process the shortlisted books, build a lookup table with authors and books_processed.csv that can be opened in a dataframe with two columns: **Author | Book**

- **make run_all**

Reads the dataset and run preprocessing, and compiling the model. Training is all that's left to do.


## What we tried:

- 2 different preprocessing methods: cleaning everything or keeping punctuation and capital letters
-> Less cleaning performed better.

- RNN LSTM from scratch
- CNN Conv1D from scratch
- RNN GRU from scratch

We embeded the text with a word2vec model trained on the entire scope of books.
RNN GRU performed best.

We also tried to use pretrained models:
- Hugging Face's BERT base cased pretrained model with a different output layer
- Hugging Face's distilBERT pretrained model, a much lighter version of BERT with a different output layer

Our best performing model was the distilBERT with a 0.7 val accuracy.
We could only go up to 0.45 val accuracy after 24 epochs with BERT. ie notebook notebooks/03_training_bert_base_cased

## Metrics

## Authors

- [@Nico404](https://www.github.com/Nico404)
- [@Clement7991](https://www.github.com/Clement7991)
- [@lxmuresan](https://www.github.com/lxmuresan)
