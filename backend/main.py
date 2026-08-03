from fastapi import FastAPI, UploadFile, File

app = FastAPI()


@app.get("/")
def home():
    return {
        "message": "Welcome to AI Study Companion Backend!"
    }


@app.post("/upload")
async def upload_file(file: UploadFile = File(...)):
    return {
        "filename": file.filename,
        "content_type": file.content_type,
        "message": "File uploaded successfully!"
    }