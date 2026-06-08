import os
from groq import Groq
from dotenv import load_dotenv
from embed import retrieve

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def ask(question):
    """Retrieve relevant chunks and generate a grounded answer."""
    
    # Step 1: Retrieve relevant chunks
    chunks = retrieve(question, k=5)
    
    # Step 2: Build context string from chunks
    context_parts = []
    sources = []
    
    for chunk in chunks:
        context_parts.append(f"[Source: {chunk['source']}]\n{chunk['text']}")
        if chunk['source'] not in sources:
            sources.append(chunk['source'])
    
    context = "\n\n".join(context_parts)
    
    # Step 3: Build prompt that enforces grounding
    prompt = f"""You are a helpful assistant for UT Dallas students looking for 
information about campus dining.

Answer the question using ONLY the information provided in the documents below.
Do not use any outside knowledge. If the documents do not contain enough 
information to answer the question, say exactly: 
"I don't have enough information in my documents to answer that."

Documents:
{context}

Question: {question}

Answer:"""
    
    # Step 4: Call Groq API
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "user", "content": prompt}],
        max_tokens=500,
        temperature=0.1
    )
    
    answer = response.choices[0].message.content.strip()
    
    return {
        "answer": answer,
        "sources": sources,
        "chunks": chunks
    }


if __name__ == "__main__":
    # Test all 5 evaluation questions
    test_questions = [
        "What dining options are at the Student Union?",
        "What times is the dining hall open on Monday?",
        "Can students use their meal plan at off-campus restaurants?",
        "What do students say about wait times at UTD dining?",
        "What are student opinions on overall food quality at UTD?"
    ]
    
    for question in test_questions:
        print("\n" + "="*60)
        print(f"QUESTION: {question}")
        print("="*60)
        result = ask(question)
        print(f"ANSWER:\n{result['answer']}")
        print(f"\nSOURCES: {', '.join(result['sources'])}")