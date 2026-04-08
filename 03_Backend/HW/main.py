from fastapi import FastAPI
from pydantic import BaseModel
from sentence_transformers import SentenceTransformer
from typing import List

app = FastAPI()

print("Loading model...")
model = SentenceTransformer("sergeyzh/rubert-mini-frida")
print("Model loaded!")

class TextRequest(BaseModel):
    text: str 

@app.get("/health")
def health_check():
    """Простая проверка: живой ли сервис"""
    return {"status": "ok"}

@app.post("/embed")
def get_embedding(request: TextRequest):
    """Принимает текст, возвращает эмбеддинг"""
    text = request.text
    embedding = model.encode(text)
    return {"embedding": embedding.tolist()}