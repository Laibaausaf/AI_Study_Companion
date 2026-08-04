from fastapi import FastAPI, UploadFile, File
from qdrant_db import store_chunks
from util import (
    extract_text_from_pdf,
    chunk_text,
    generate_embeddings
)
from qdrant_db import client
from qdrant_db import search_chunks

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
    store_chunks(chunks, embeddings)

    return {
    "filename": file.filename,
    "chunks_stored": len(chunks),
    "message": "Document stored successfully!"
}
from pydantic import BaseModel

class QuestionRequest(BaseModel):
    question: str


@app.post("/ask")
def ask_question(request: QuestionRequest):

    chunks = search_chunks(request.question)

    return {
        "question": request.question,
        "relevant_chunks": chunks
    }