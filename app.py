import streamlit as st
import os
from processing.text_extraction import extract_text
from processing.vector_store import store_text_in_vector_db, retrieve_text_from_vector_db
from processing.llm_integration import summarize_text, answer_question

# App Title
st.title("📚 ResearchPal – AI-Powered Research Assistant")

# File Upload Section
uploaded_file = st.file_uploader("📂 Upload a Research Paper (PDF)", type="pdf")

if uploaded_file is not None:
    with open("temp.pdf", "wb") as f:
        f.write(uploaded_file.getbuffer())

    st.write("📖 Extracting text from PDF...")
    extracted_text = extract_text("temp.pdf")

    if extracted_text:
        st.write("✅ Text extracted successfully!")
        
        # 🔥 Store text with document ID (PDF name)
        doc_id = uploaded_file.name.replace(".pdf", "")
        store_text_in_vector_db(extracted_text, doc_id=doc_id)

        # Summarization Button
        if st.button("🔹 Generate Summary"):
            st.write("📝 Generating Summary...")
            summary = summarize_text(extracted_text)
            st.write(summary)

# Q&A Section
st.subheader("🤖 Ask a Question About the Paper")

query = st.text_input("Enter your question:")
if query and uploaded_file is not None:
    doc_id = uploaded_file.name.replace(".pdf", "")
    retrieved_texts = retrieve_text_from_vector_db(query, doc_id)

    if retrieved_texts:
        context = " ".join(retrieved_texts)
        prompt = f"Based on this research paper, provide a precise answer to: {query}. Context:\n{context}\nGive a factual, concise response."
        answer = answer_question(prompt, context)
    else:
        answer = "⚠️ No relevant information found in the research paper."

    st.write("🧠 AI Answer:", answer)
