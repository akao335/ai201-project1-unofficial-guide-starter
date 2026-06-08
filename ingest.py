import os
import re

DOCUMENTS_FOLDER = "documents"

def load_documents():
    """Load all .txt files from the documents folder."""
    documents = []
    
    for filename in os.listdir(DOCUMENTS_FOLDER):
        if filename.endswith(".txt"):
            filepath = os.path.join(DOCUMENTS_FOLDER, filename)
            with open(filepath, "r", encoding="utf-8") as f:
                raw_text = f.read()
            
            cleaned = clean_text(raw_text)
            
            if cleaned.strip():
                documents.append({
                    "source": filename,
                    "text": cleaned
                })
                print(f"Loaded: {filename} ({len(cleaned)} characters)")
    
    print(f"\nTotal documents loaded: {len(documents)}")
    return documents


def clean_text(text):
    """Remove noise from raw document text."""
    
    # Remove URLs
    text = re.sub(r'http\S+', '', text)
    
    # Remove HTML tags
    text = re.sub(r'<[^>]+>', '', text)
    
    # Remove HTML entities like &amp; &nbsp; &#39;
    text = re.sub(r'&[a-zA-Z]+;', '', text)
    text = re.sub(r'&#\d+;', '', text)
    
    # Remove Reddit-style vote counts and metadata (e.g. "↑ 42 points")
    text = re.sub(r'[↑↓]\s*\d+\s*(points?)?', '', text)
    
    # Remove lines that are just navigation/boilerplate
    boilerplate = [
        "skip to content", "skip to main", "sign in", "log in", "log out",
        "cookie", "privacy policy", "terms of service", "all rights reserved",
        "share", "report", "save", "hide", "reply", "give award",
        "posted by", "submitted by", "view all comments", "load more comments",
        "press j to jump", "press question mark"
    ]
    lines = text.split("\n")
    cleaned_lines = []
    for line in lines:
        if not any(phrase in line.lower() for phrase in boilerplate):
            cleaned_lines.append(line)
    text = "\n".join(cleaned_lines)
    
    # Collapse multiple blank lines into one
    text = re.sub(r'\n{3,}', '\n\n', text)
    
    # Collapse multiple spaces
    text = re.sub(r' {2,}', ' ', text)
    
    return text.strip()


def chunk_text(text, source, chunk_size=400, overlap=80):
    """Split text into chunks with overlap, keeping source metadata."""
    chunks = []
    start = 0
    chunk_index = 0
    
    while start < len(text):
        end = start + chunk_size
        chunk = text[start:end].strip()
        
        if len(chunk) > 0:
            chunks.append({
                "source": source,
                "chunk_index": chunk_index,
                "text": chunk
            })
            chunk_index += 1
        
        start += chunk_size - overlap
    
    return chunks


def get_all_chunks():
    """Load documents and return all chunks across all documents."""
    documents = load_documents()
    all_chunks = []
    
    for doc in documents:
        chunks = chunk_text(doc["text"], doc["source"])
        all_chunks.extend(chunks)
    
    print(f"Total chunks created: {len(all_chunks)}")
    return all_chunks


if __name__ == "__main__":
    all_chunks = get_all_chunks()
    
    print("\n--- 5 SAMPLE CHUNKS ---\n")
    step = max(1, len(all_chunks) // 5)
    sample_indices = [0, step, step*2, step*3, len(all_chunks)-1]
    
    for i in sample_indices:
        chunk = all_chunks[i]
        print(f"Chunk #{i} | Source: {chunk['source']}")
        print(f"Text: {chunk['text']}")
        print("-" * 60)