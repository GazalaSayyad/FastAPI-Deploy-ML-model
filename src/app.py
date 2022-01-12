# Importing Libraries
from transformers import pipeline
from fastapi import FastAPI
import uvicorn

app = FastAPI()
 
# Defining path operation for root endpoint
@app.get('/')
def main():
    return {'message': 'Welcome to Sentiment Analysis'}

@app.post('/sentiment_analysis')
async def query_sentiment_analysis(text: str):
    classifier = pipeline('sentiment-analysis')
    result = classifier(text)
    return result

