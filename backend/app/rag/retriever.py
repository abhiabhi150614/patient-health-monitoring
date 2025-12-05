import os
from langchain_chroma import Chroma
from langchain_openai import OpenAIEmbeddings

DB_PATH = os.path.join(os.path.dirname(__file__), '..', '..', 'chroma_db')

def get_retriever():
    from ..agents.llm import get_embeddings
    embeddings = get_embeddings()
        
    vector_store = Chroma(persist_directory=DB_PATH, embedding_function=embeddings)
    return vector_store.as_retriever(search_kwargs={"k": 3})

def rag_query(question: str, patient_context: str = ""):
    retriever = get_retriever()
    
    query = question
    if patient_context:
        query = f"Context: {patient_context}\nQuestion: {question}"
        
    docs = retriever.invoke(query)
    
    results = []
    for doc in docs:
        source_path = doc.metadata.get("source", "Nephrology Reference")
        # Clean up source to show only filename if it's a path
        if os.path.exists(source_path):
            source_name = os.path.basename(source_path)
        else:
            source_name = source_path
            
        results.append({
            "content": doc.page_content,
            "source": source_name
        })
    
    return results
