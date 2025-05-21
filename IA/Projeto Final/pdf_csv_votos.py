#Transformar os PDFs em CSVs

import os
import tabula
from PyPDF2 import PdfReader
import pandas as pd

# Caminho da pasta com os PDFs
pasta_pdf = "PDFs"
# Caminho onde os CSVs serão salvos
pasta_saida = "CSVs/cada_senador"

# Criar pasta de saída se não existir
os.makedirs(pasta_saida, exist_ok=True)

# Percorrer todos os arquivos PDF
for nome_arquivo in os.listdir(pasta_pdf):
    if nome_arquivo.endswith(".pdf"):
        caminho_pdf = os.path.join(pasta_pdf, nome_arquivo)
        nome_base = os.path.splitext(nome_arquivo)[0]

        print(f"Processando: {nome_arquivo}")

        # Obter número de páginas
        leitor = PdfReader(caminho_pdf)
        num_paginas = len(leitor.pages)

        tabelas_pdf = []

        # Ler tabelas página por página
        for pagina in range(1, num_paginas + 1):
            try:
                tabelas = tabula.read_pdf(caminho_pdf, pages=pagina, multiple_tables=True)
                for tabela in tabelas:
                    if not tabela.empty:
                        tabelas_pdf.append(tabela)
            except Exception as e:
                print(f"  ⚠ Erro na página {pagina}: {e}")

        # Se alguma tabela foi extraída, concatenar e salvar
        if tabelas_pdf:
            tabela_unica = pd.concat(tabelas_pdf, ignore_index=True)
            caminho_csv = os.path.join(pasta_saida, f"{nome_base}.csv")
            tabela_unica.to_csv(caminho_csv, index=False)
            print(f"Tabela única salva em {caminho_csv}")
        else:
            print("Nenhuma tabela encontrada neste PDF.")

print("Processamento concluído.")
