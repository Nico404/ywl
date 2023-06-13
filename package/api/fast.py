import pandas as pd
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

@app.get("/")
def root():
    return {'greeting': 'Hello'}


# Allowing all middleware is optional, but good practice for dev purposes
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)

# http://127.0.0.1:8000/predict?text=sample_text
@app.get("/predict_gru")
def predict(
        text: str
    ):
    # load model here
    # apply preprocessing here
    # prediction here

    # simulate prediction output
    writer_scores_dict = {'Shakespeare': 0.31, 'Jane Austen': 0.32, 'Charles Dickens': 0.21, 'Mark Twain': 0.12, 'Oscar Wilde': 0.04}
    # only keep the top 3 writers
    top_3_writers = sorted(writer_scores_dict, key=writer_scores_dict.get, reverse=True)[:3]
    return top_3_writers

@app.get("/predict_bert")
def predict(
        text: str
    ):
    # load model here
    # apply preprocessing here
    # prediction here

    # simulate prediction output
    writer_scores_dict = {'Marco Polo': 0.11, 'Moliere': 0.52, 'Clement': 0.21, 'Alex': 0.12, 'Nico': 0.04}
    # only keep the top 3 writers
    top_3_writers = sorted(writer_scores_dict, key=writer_scores_dict.get, reverse=True)[:3]
    return top_3_writers
