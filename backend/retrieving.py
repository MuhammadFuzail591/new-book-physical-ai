import cohere
from qdrant_client import QdrantClient
import os
from dotenv import load_dotenv

load_dotenv()

cohere_api_key = os.getenv("CO_API_KEY")
qdrant_api_key = os.getenv("QDRANT_API_KEY")

# Initialize Cohere client
cohere_client = cohere.Client(cohere_api_key)
 # Return the first embedding
# Connect to Qdrant
qdrant = QdrantClient(
    url="https://c10482d5-5b03-4499-ba9e-774bf6cc9929.europe-west3-0.gcp.cloud.qdrant.io", 
    api_key=qdrant_api_key
)

def get_embedding(text):
    """Get embedding vector from Cohere Embed v3"""
    response = cohere_client.embed(
        model="embed-english-v3.0",
        input_type="search_query", 
        texts=[text],
    )
    return response.embeddings[0]

def retrieve(query):
    embedding = get_embedding(query)
    result = qdrant.query_points(
        collection_name="fuzail-ai-book",
        query=embedding,
        limit=5
    )
    return [point.payload["text"] for point in result.points]

# Test
print(retrieve("What data do you have?"))