import os

from dotenv import load_dotenv
from qdrant_client import QdrantClient
from qdrant_client.models import PointStruct
import uuid

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

def store_chunks(chunks, embeddings):
    points = []

    for chunk, embedding in zip(chunks, embeddings):
        points.append(
            PointStruct(
                id=str(uuid.uuid4()),
                vector=embedding,
                payload={
                    "text": chunk
                }
            )
        )

    client.upsert(
        collection_name=COLLECTION_NAME,
        points=points
    )