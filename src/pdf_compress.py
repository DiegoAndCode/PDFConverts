from PyPDF2 import PdfReader, PdfWriter

def compress_pdf(input_path, output_path):
    with open(input_path, 'rb') as file:
        reader = PdfReader(file)
        writer = PdfWriter()

        for page in reader.pages:
            page.compress_content_streams()  # Comprime o conteúdo da página
            writer.add_page(page)
        
        with open(output_path, 'wb') as output_file:
            writer.write(output_file)

    print(f'O arquivo PDF foi comprimido e salvo em "{output_path}".')

if __name__ == '__main__':
    input_path = 'merged.pdf'
    output_path = 'compressed.pdf'
    compress_pdf(input_path, output_path)
