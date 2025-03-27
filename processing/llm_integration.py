import subprocess

def query_llm(prompt, model = "mistral"):
    command = f'ollama run {model} "{prompt}"'
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    return result.stdout.strip()

def summarize_text(text):
    """Summarize extracted research paper text using the LLM."""
    prompt = f"Summarize the following research paper:\n{text[:1000]}"  # Limit input for efficiency
    return query_llm(prompt)

def answer_question(question, context):
    """Answer a research-related question using retrieved text from ChromaDB."""
    prompt = (
        f"Based on the following research paper, provide a clear and concise answer to the question.\n\n"
        f"Context from the paper:\n{context}\n\n"
        f"Question: {question}\n"
        f"Answer concisely but informatively."
    )
    return query_llm(prompt)

if __name__ == "__main__":
    sample_text = "Transformers are deep learning architectures that use self-attention."
    print("🔹 Sample Summary:", summarize_text(sample_text))

    sample_question = "What is a Transformer model?"
    print("🔹 Answer:", answer_question(sample_question, sample_text))