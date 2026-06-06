from pypdf import PdfReader

# Load PDF
pdf_path = "data/sample.pdf"
reader = PdfReader(pdf_path)

print(f"Total Pages: {len(reader.pages)}")

# Extract text
text = ""

for page_num, page in enumerate(reader.pages, start=1):
    page_text = page.extract_text()

    if page_text:
        text += page_text + "\n"

print(f"\nTotal Characters Extracted: {len(text)}")

# Chunking
chunk_size = 500
chunks = []

for i in range(0, len(text), chunk_size):
    chunk = text[i:i + chunk_size]
    chunks.append(chunk)

# Results
print(f"\nTotal Chunks Created: {len(chunks)}")

for index, chunk in enumerate(chunks, start=1):
    print(f"\n{'=' * 50}")
    print(f"Chunk {index}")
    print(f"{'=' * 50}")
    print(chunk)