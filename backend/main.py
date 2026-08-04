from fastapi import FastAPI, UploadFile, File

from util import (
    extract_text_from_pdf,
    chunk_text,
    generate_embeddings
)
from qdrant_db import client

app = FastAPI()


@app.get("/")
def home():
    return {
        "message": "Welcome to AI Study Companion Backend!"
    }


@app.post("/upload")
async def upload_file(file: UploadFile = File(...)):
    file_bytes = await file.read()

    text = extract_text_from_pdf(file_bytes)

    chunks = chunk_text(text)

    embeddings = generate_embeddings(chunks)

    return {
        "filename": file.filename,
        "total_chunks": len(chunks),
        "embedding_dimension": len(embeddings[0]) if embeddings else 0
    }