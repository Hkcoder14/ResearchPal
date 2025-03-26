import fitz
import os 

DATA_FOLDER = "papers"
OUTPUT_FOLDER = "processed_texts"

def extract_text(pdf_path):

    doc = fitz.open(pdf_path)
    text = "\n".join([page.get_text() for page in doc])
    return text

def process_pdfs():

    for filename in os.listdir(DATA_FOLDER):
        if filename.endswith(".pdf"):
            pdf_path = os.path.join(DATA_FOLDER, filename)
            text = extract_text(pdf_path)

            output_file = os.path.join(OUTPUT_FOLDER, filename.replace(".pdf", ".txt"))
            with open(output_file, "w", encoding="utf-8") as f:
                f.write(text)
            
            print(f"Extracted text and saved {output_file}")

if __name__ == "__main__":
    process_pdfs()
                                       
