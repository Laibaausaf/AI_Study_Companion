import os

from dotenv import load_dotenv
from qdrant_client import QdrantClient

load_dotenv()

client = QdrantClient(
    url=os.getenv("QDRANT_URL"),
    api_key=os.getenv("QDRANT_API_KEY"),
)

from qdrant_client.models import VectorParams, Distance

COLLECTION_NAME = "study_notes"

collections = client.get_collections().collections

if not any(c.name == COLLECTION_NAME for c in collections):
    client.create_collection(
        collection_name=COLLECTION_NAME,
        vectors_config=VectorParams(
            size=384,
            distance=Distance.COSINE,
        ),
    )