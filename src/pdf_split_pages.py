import os
from PyPDF2 import PdfReader, PdfWriter

def split_pdf(input_pdf):
    input_pdf_name = os.path.splitext(input_pdf)[0]  # Remove a extensão .pdf
    reader = PdfReader(input_pdf)
    for i, page in enumerate(reader.pages):
        writer = PdfWriter()
        writer.add_page(page)

        output_pdf = f"{input_pdf_name}_{i}.pdf"
        with open(output_pdf, "wb") as f:
            writer.write(f)


def main():
    input_pdf = "merged.pdf"
    split_pdf(input_pdf)


if __name__ == "__main__":
    main()
