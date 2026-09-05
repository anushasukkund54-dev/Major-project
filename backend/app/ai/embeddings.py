from sentence_transformers import SentenceTransformer


class EmbeddingService:
    def __init__(self):
        self.model = SentenceTransformer("BAAI/bge-m3")

    def generate_embedding(self, text: str) -> list[float]:
        embedding = self.model.encode(text)
        return embedding.tolist()
    
    
    
if __name__ == "__main__":
    service = EmbeddingService()

    text = "Python developer with FastAPI and PostgreSQL experience."

    vector = service.generate_embedding(text)

    print("Embedding generated successfully!")
    print("Vector length:", len(vector))
    print("First 5 values:", vector[:5])    