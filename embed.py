import chromadb
from sentence_transformers import SentenceTransformer
from ingest import get_all_chunks

COLLECTION_NAME = "utd_dining"

def build_vector_store():
    """Embed all chunks and store in ChromaDB."""
    
    print("Loading chunks...")
    all_chunks = get_all_chunks()
    
    print("\nLoading embedding model (this may take a minute first time)...")
    model = SentenceTransformer("all-MiniLM-L6-v2")
    
    print("Setting up ChromaDB...")
    client = chromadb.PersistentClient(path="./chroma_db")
    
    # Delete existing collection if it exists so we start fresh
    try:
        client.delete_collection(COLLECTION_NAME)
        print("Cleared existing collection.")
    except:
        pass
    
    collection = client.create_collection(COLLECTION_NAME)
    
    print(f"Embedding {len(all_chunks)} chunks...")
    texts = [chunk["text"] for chunk in all_chunks]
    embeddings = model.encode(texts, show_progress_bar=True)
    
    # Store chunks in ChromaDB with metadata
    collection.add(
        ids=[f"chunk_{i}" for i in range(len(all_chunks))],
        embeddings=[e.tolist() for e in embeddings],
        documents=texts,
        metadatas=[{
            "source": chunk["source"],
            "chunk_index": chunk["chunk_index"]
        } for chunk in all_chunks]
    )
    
    print(f"\nSuccessfully stored {len(all_chunks)} chunks in ChromaDB.")
    return collection


def get_collection():
    """Load existing ChromaDB collection."""
    client = chromadb.PersistentClient(path="./chroma_db")
    return client.get_collection(COLLECTION_NAME)


def retrieve(query, k=5):
    """Retrieve top-k most relevant chunks for a query."""
    model = SentenceTransformer("all-MiniLM-L6-v2")
    collection = get_collection()
    
    query_embedding = model.encode([query])[0].tolist()
    
    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=k,
        include=["documents", "metadatas", "distances"]
    )
    
    chunks = []
    for i in range(len(results["documents"][0])):
        chunks.append({
            "text": results["documents"][0][i],
            "source": results["metadatas"][0][i]["source"],
            "distance": round(results["distances"][0][i], 4)
        })
    
    return chunks


if __name__ == "__main__":
    # Build the vector store
    build_vector_store()
    
    # Test retrieval with your 5 evaluation questions
    test_queries = [
        "What dining options are at the Student Union?",
        "What times is the dining hall open on Monday?",
        "Can students use their meal plan at off-campus restaurants?",
        "What do students say about wait times at UTD dining?",
        "What are student opinions on overall food quality at UTD?"
    ]
    
    print("\n" + "="*60)
    print("RETRIEVAL TEST")
    print("="*60)
    
    for query in test_queries:
        print(f"\nQUERY: {query}")
        print("-" * 60)
        results = retrieve(query)
        for r in results:
            print(f"  Source: {r['source']} | Distance: {r['distance']}")
            print(f"  Text: {r['text'][:200]}...")
            print()