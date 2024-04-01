import os
import lzma
import shutil

def compactar_arquivo(arquivo_origem):
    with open(arquivo_origem, 'rb') as f_in:
        with lzma.open(arquivo_origem + '.xz', 'wb', preset=9) as f_out:
            shutil.copyfileobj(f_in, f_out)
    return arquivo_origem + '.xz'

def descompactar_arquivo(arquivo_compactado):
    nome_arquivo, _ = os.path.splitext(arquivo_compactado)
    arquivo_destino = nome_arquivo
    with lzma.open(arquivo_compactado, 'rb') as f_in:
        with open(arquivo_destino, 'wb') as f_out:
            shutil.copyfileobj(f_in, f_out)
    return arquivo_destino

def compactar_ou_descompactar_arquivo(caminho_arquivo):
    if os.path.exists(caminho_arquivo):
        nome_arquivo, extensao = os.path.splitext(caminho_arquivo)
        if extensao == '.xz':
            arquivo_descompactado = descompactar_arquivo(caminho_arquivo)
            print(f'Arquivo descompactado: {arquivo_descompactado}')
        else:
            arquivo_compactado = compactar_arquivo(caminho_arquivo)
            print(f'Arquivo compactado: {arquivo_compactado}')
    else:
        print(f'Arquivo não encontrado: {caminho_arquivo}')

def main():
    caminho_arquivo = 'bkp_file.mbox' # Arquivo para comprimir
    compactar_ou_descompactar_arquivo(caminho_arquivo)

if __name__ == "__main__":
    main()
