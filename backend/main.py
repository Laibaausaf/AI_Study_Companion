from fastapi import FastAPI, UploadFile, File
from qdrant_db import store_chunks
from util import (
    extract_text_from_pdf,
    chunk_text,
    generate_embeddings
)
from qdrant_db import client
from qdrant_db import search_chunks
from gemini import generate_answer, generate_study_plan
from fastapi.middleware.cors import CORSMiddleware
app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

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
class StudyPlanRequest(BaseModel):
    days: int

@app.post("/ask")
def ask_question(request: QuestionRequest):

    chunks = search_chunks(request.question)

    answer = generate_answer(
        request.question,
        chunks
    )

    return {
        "question": request.question,
        "answer": answer,
        "sources": chunks
    }
@app.post("/generate-study-plan")
def generate_plan(request: StudyPlanRequest):

    chunks = search_chunks(
        "complete syllabus",
        limit=15
    )

    plan = generate_study_plan(
        request.days,
        chunks
    )

    return {
        "study_plan": plan
    }