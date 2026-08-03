from fastapi import FastAPI, UploadFile, File
from util import extract_text_from_pdf, chunk_text

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

    return {
        "filename": file.filename,
        "total_chunks": len(chunks),
        "first_chunk": chunks[0] if chunks else "No text found"
    }