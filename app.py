from pypdf import PdfReader

pdf_path = "data/sample.pdf"
reader = PdfReader(pdf_path)
print(f"Total Pages:{len(reader.pages)}")
text = ""

for page_num, page in enumerate(reader.pages,start=1):
    page_text = page.extract_text()

    print(f"\n--------page{page_num}-------")

    if page_text:
        print(page_text[:200])
        text += page_text + "\n"

    else:
        print("No text found")
print(f"Total character extracted: {len{text}}")