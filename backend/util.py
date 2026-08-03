import fitz
from sentence_transformers import SentenceTransformer

model = SentenceTransformer("all-MiniLM-L6-v2")
def extract_text_from_pdf(file_bytes):
    text = ""

    pdf = fitz.open(stream=file_bytes, filetype="pdf")

    for page in pdf:
        text += page.get_text()

    return text

def chunk_text(text, chunk_size=500):
    chunks = []

    for i in range(0, len(text), chunk_size):
        chunks.append(text[i:i + chunk_size])

    return chunks

def generate_embeddings(chunks):
    embeddings = model.encode(chunks)

    return embeddings.tolist()