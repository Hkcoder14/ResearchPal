import streamlit as st
import os
from processing.text_extraction import extract_text
from processing.vector_store import store_text_in_vector_db, retrieve_text_from_vector_db
from processing.llm_integration import summarize_text, answer_question

# App Title
st.title("📚 ResearchPal – AI-Powered Research Assistant")

# Ensure folders exist
os.makedirs("papers", exist_ok=True)
os.makedirs("processed_texts", exist_ok=True)

# File Upload Section
uploaded_file = st.file_uploader("📂 Upload a Research Paper (PDF)", type="pdf")

if uploaded_file is not None:
    # Save PDF in "papers/" directory
    pdf_path = os.path.join("papers", uploaded_file.name)
    with open(pdf_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    st.write(f"✅ File saved to: `{pdf_path}`")

    # Extract text and save in "processed_texts/"
    st.write("📖 Extracting text from PDF...")
    extracted_text = extract_text(pdf_path)
    
    if extracted_text:
        text_filename = uploaded_file.name.replace(".pdf", ".txt")
        text_path = os.path.join("processed_texts", text_filename)
        with open(text_path, "w", encoding="utf-8") as text_file:
            text_file.write(extracted_text)

        st.write(f"✅ Extracted text saved to: `{text_path}`")

        # Store extracted text in vector database
        doc_id = uploaded_file.name.replace(".pdf", "")  # Extract document name without .pdf
        store_text_in_vector_db(extracted_text, doc_id)
        st.write("✅ Stored in vector database!")

        # Generate Summary
        if st.button("🔹 Generate Summary"):
            st.write("📝 Generating Summary...")
            summary = summarize_text(extracted_text)
            st.write(summary)

# 📑 **Dropdown to Select a Research Paper**
pdf_files = [f.replace(".txt", "") for f in os.listdir("processed_texts") if f.endswith(".txt")]
selected_pdf = st.selectbox("📑 Select a research paper to query:", pdf_files if pdf_files else ["No PDFs uploaded"])

# Q&A Section
st.subheader("🤖 Ask a Question About the Selected Paper")
query = st.text_input("Enter your question:")

if query:
    retrieved_texts = retrieve_text_from_vector_db(query, doc_id=selected_pdf)  # ✅ Filter by selected doc

    if retrieved_texts:
        context = " ".join(retrieved_texts)
        prompt = f"Based on the research paper '{selected_pdf}', answer:\n{query}\nContext:\n{context}"
        answer = answer_question(prompt, context)
    else:
        answer = "⚠️ No relevant information found in the selected research paper."

    st.write("🧠 AI Answer:", answer)
