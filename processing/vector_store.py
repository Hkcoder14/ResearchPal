import chromadb
import os

TEXT_FOLDER = "processed_texts"
DB_PATH = "../chroma_db"

# Initialize ChromaDB client
client = chromadb.PersistentClient(path=DB_PATH)
collection = client.get_or_create_collection("research_texts")

def store_text_in_vector_db(text, doc_id="default_doc"):
    """Stores extracted text into ChromaDB by chunking long texts."""
    chunk_size = 500  # Each chunk contains 500 characters
    text_chunks = [text[i:i + chunk_size] for i in range(0, len(text), chunk_size)]
    
    # Store chunks with unique chunk IDs
    for i, chunk in enumerate(text_chunks):
        chunk_id = f"{doc_id}_{i}"
        collection.add(ids=[chunk_id], documents=[chunk], metadatas=[{"doc_id": doc_id}])
    
    print(f"✅ Stored {len(text_chunks)} chunks in ChromaDB for {doc_id}")

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
    """Retrieve relevant text from ChromaDB based on query and document ID."""
    results = collection.query(query_texts=[query], n_results=5)

    print(f"🔍 Querying ChromaDB for: {query} (from document: {doc_id})")
    print("🛠 Raw Results:", results)

    if not results or "documents" not in results:
        return []

    retrieved_texts = []

    # ✅ Iterate over results and check metadata for matching doc_id
    for i, doc in enumerate(results["documents"]):
        doc_text = " ".join(doc) if isinstance(doc, list) else doc  # Ensure string format

        metadata_list = results.get("metadatas", [])
        if metadata_list and i < len(metadata_list) and isinstance(metadata_list[i], dict):
            metadata = metadata_list[i]
            if metadata.get("doc_id") == doc_id:
                retrieved_texts.append(doc_text)  # ✅ Add only if doc_id matches
        else:
            print(f"⚠️ No metadata found for chunk {i}, adding as fallback.")
            retrieved_texts.append(doc_text)  # ✅ Fallback: Add text if no metadata

    # ✅ Print Debugging Info
    print("✅ Retrieved Texts:", retrieved_texts)  
    return retrieved_texts


if __name__ == "__main__":
    store_all_texts()  # Store all processed texts
