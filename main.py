from fastapi import FastAPI
from transformers import pipeline
from pydantic import BaseModel
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from pathlib import Path

translator = pipeline("translation_en_to_ml", model="Helsinki-NLP/opus-mt-en-ml")

app = FastAPI()

class TextInput(BaseModel):
    text: str


app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/")
async def home():
    return FileResponse(Path("static/index.html").resolve())

@app.post("/translate")
async def translate_text(data: TextInput):
    result = translator(data.text)
    return {"translation": result[0]["translation_text"]}



