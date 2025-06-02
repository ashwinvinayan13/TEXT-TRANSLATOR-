from fastapi import FastAPI
from transformers import pipeline
from pydantic import BaseModel

translator = pipeline("translation to english to malayalam ", model="Helsinki-NLP/opus-mt-en-ml")

app = FastAPI()

class TextInput(BaseModel):
    text: str