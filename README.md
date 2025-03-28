# 📚 ResearchPal – AI-Powered Research Assistant  

**ResearchPal** is an AI-powered research assistant designed to help users upload, analyze, and query research papers using **LLMs and Vector Databases**. It supports **multiple PDFs**, extracts text, stores it in **ChromaDB**, and allows users to **ask questions and get precise answers** from the documents.  

## ✨ Features  
✅ Upload multiple research papers (PDFs)  
✅ Extract and store text for efficient retrieval  
✅ AI-powered summarization of documents  
✅ Intelligent Q&A system using **LLMs**  
✅ Fast retrieval via **ChromaDB vector search**  

---

## 🚀 Installation  

### **1️⃣ Clone the Repository**  
```bash
git clone https://github.com/your-username/ResearchPal.git
cd ResearchPal
```

### **2️⃣ Create a Virtual Environment (Recommended)**
```bash
python -m venv venv
source venv/bin/activate  # On Mac/Linux
venv\Scripts\activate  # On Windows
```

### **3️⃣ Install Dependencies**
```bash
pip install -r requirements.txt
```

---

## 🔥 Usage  

### **1️⃣ Start Ollama (LLM Backend)**
Ollama is required for processing queries. Start it using:  
```bash
ollama run llama2
```

### **2️⃣ Run ResearchPal**
```bash
streamlit run app.py
```
Now, open **http://localhost:8501** in your browser to start using the app.

---


## 🤖 How It Works  
1️⃣ **Upload PDFs** – The app extracts text and stores it in a **vector database**.  
2️⃣ **Summarize** – Click **"Generate Summary"** to get a concise overview of the paper.  
3️⃣ **Ask Questions** – Type any research-related query, and the AI retrieves the most relevant info.  

---

## 📌 Dependencies  
- **Streamlit** – UI for the research assistant  
- **PyMuPDF** – PDF text extraction  
- **ChromaDB** – Vector search database  
- **Ollama** – LLM for AI-powered Q&A  
- **SentenceTransformers** – Embedding model for vector storage  

Install them using:  
```bash
pip install -r requirements.txt
```

---

## 🏗 Future Improvements  
🔹 Support for **additional document formats** (DOCX, TXT)  
🔹 Improve chunking for **better retrieval accuracy**  
🔹 Add **citation & reference extraction**  

---

## 👨‍💻 Author  
- **Harsh Kumar**  
- **GitHub**: [your-username](https://github.com/your-username)  
- **LinkedIn**: [your-profile](https://linkedin.com/in/your-profile)  

---

## ⭐️ Show Some Love!  
If you found this project useful, consider giving it a ⭐ on GitHub! 😃  
