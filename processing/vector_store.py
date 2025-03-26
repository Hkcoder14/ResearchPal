import chromadb
import os

TEXT_FOLDER = "processed_texts"
DB_PATH = "../chroma_db"

# Initialize ChromaDB client
client = chromadb.PersistentClient(path=DB_PATH)
collection = client.get_or_create_collection("research_texts")

def store_text_in_vector_db(text, doc_id="default_doc"):
    """Stores extracted text into ChromaDB with a unique document ID."""
    collection.add(ids=[doc_id], documents=[text])
    print(f"✅ Stored: {doc_id} in ChromaDB")

def store_all_texts():
    """Reads extracted text files and stores them in ChromaDB."""
    for filename in os.listdir(TEXT_FOLDER):
        if filename.endswith(".txt"):
            file_path = os.path.join(TEXT_FOLDER, filename)
            with open(file_path, "r", encoding="utf-8") as f:
                text = f.read()
            
            doc_id = filename.replace(".txt", "")  # Use filename as doc ID
            store_text_in_vector_db(text, doc_id)

def retrieve_text_from_vector_db(query, doc_id):
    """Retrieve relevant text from ChromaDB based on query and filter by doc_id."""
    results = collection.query(query_texts=[query], n_results=5)

    # Ensure results are retrieved
    if not results or "documents" not in results:
        return []

    retrieved_texts = []
    for i, doc in enumerate(results["documents"]):
        if isinstance(doc, list):  # Ensure it's a list and extract text
            doc_text = " ".join(doc)  
        else:
            doc_text = doc
        
        # 🔥 Ensure doc_id matches (if metadata is available)
        if "metadatas" in results and results["metadatas"]:
            metadata_list = results["metadatas"]
            if i < len(metadata_list) and isinstance(metadata_list[i], dict):
                metadata = metadata_list[i]
                if metadata.get("doc_id") == doc_id:
                    retrieved_texts.append(doc_text)
        else:
            retrieved_texts.append(doc_text)  # Default to adding if no metadata

    return retrieved_texts



if __name__ == "__main__":
    store_all_texts()  # Store all processed texts
