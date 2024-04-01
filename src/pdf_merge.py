from PyPDF2 import PdfReader, PdfWriter

def merge_pdfs(pdf1_path, pdf2_path, output_path):
    # Abre os arquivos PDF originais
    with open(pdf1_path, 'rb') as pdf1_file, open(pdf2_path, 'rb') as pdf2_file:
        reader1 = PdfReader(pdf1_file)
        reader2 = PdfReader(pdf2_file)
        
        # Cria um objeto PdfWriter para o novo arquivo PDF
        writer = PdfWriter()

        # Adiciona as páginas do primeiro PDF ao novo PDF
        for page in reader1.pages:
            writer.add_page(page)

        # Adiciona as páginas do segundo PDF ao novo PDF
        for page in reader2.pages:
            writer.add_page(page)

        # Salva o novo arquivo PDF
        with open(output_path, 'wb') as output_file:
            writer.write(output_file)

if __name__ == "__main__":
    pdf1_path = 'file1.pdf'
    pdf2_path = 'file2.pdf'
    output_path = 'merged.pdf'
    
    merge_pdfs(pdf1_path, pdf2_path, output_path)
    print(f"Os arquivos PDF foram mesclados com sucesso em '{output_path}'.")
    
