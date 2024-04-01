import os
from PIL import Image
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.lib.utils import ImageReader

def convert_image_to_pdf(image_path):
    # Abrir a imagem
    image = Image.open(image_path)

    # Obtém as dimensões da imagem
    image_width, image_height = image.size

    # Remover a extensão .pdf
    pdf_name = os.path.splitext(image_path)[0] 

    # Criar um novo PDF
    pdf = canvas.Canvas(pdf_name, pagesize=A4)

    # Calcular as coordenadas para centralizar a imagem
    x_offset = (A4[0] - image_width) / 2
    y_offset = (A4[1] - image_height) / 2

    # Desenha a imagem no PDF
    pdf.drawImage(ImageReader(image_path), x_offset, y_offset, width=image_width, height=image_height, preserveAspectRatio=True, mask='auto')

    # Salva o PDF
    pdf.save()

if __name__ == '__main__':
    input_image = 'logo.jpeg'    # Imagem para converter em PDF

    convert_image_to_pdf(input_image)
