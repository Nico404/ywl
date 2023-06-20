import os
import pandas as pd
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import tensorflow as tf
from config import Config
from transformers import TextClassificationPipeline
from transformers import AutoTokenizer
from transformers import TFAutoModelForSequenceClassification
from contextlib import asynccontextmanager

config = Config()

model = dict()


@asynccontextmanager
async def lifespan(app: FastAPI):
    # loading model
    model['predict_model'] = TFAutoModelForSequenceClassification.from_pretrained(config.FINAL_BERT_MODEL)
    model['predict_tokenizer'] = AutoTokenizer.from_pretrained(config.FINAL_BERT_TOKENIZER)
    model['pipe'] = TextClassificationPipeline(model=model['predict_model'], tokenizer=model['predict_tokenizer'], return_all_scores=True)
    print('Pretrained Model loaded')
    yield
    model.clear()
app = FastAPI(lifespan=lifespan)

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return {'greeting': 'Hello'}

# http://127.0.0.1:8002/predict_bert?text=lalala
@app.post("/predict_bert")
def predict(text: str):

    # create a dictionary with labels and scores
    labels_scores_dict = {item['label']: item['score'] for sublist in model['pipe'](text) for item in sublist}

    # order the dictionary by score
    sorted_dict = dict(sorted(labels_scores_dict.items(), key=lambda x: x[1], reverse=True))
    print(sorted_dict)
    return sorted_dict 