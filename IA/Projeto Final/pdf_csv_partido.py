import pdfplumber
import re
import csv
import os

pasta_pdfs = "PDFs"
saida_csv = "CSVs/partidos/senadores_nome_partido.csv"

dados = []

padrao = re.compile(
    r"SENADOR:\s*(.+?)\s+PARTIDO:\s*(.+?)\s+UF:\s*([A-Z]{2})",
    re.IGNORECASE
)

# Percorre todos os arquivos da pasta_pdfs
for arquivo in os.listdir(pasta_pdfs):
    if arquivo.lower().endswith(".pdf"):
        caminho_pdf = os.path.join(pasta_pdfs, arquivo)
        with pdfplumber.open(caminho_pdf) as pdf:
            for pagina in pdf.pages:
                texto = pagina.extract_text()
                if not texto:
                    continue
                for linha in texto.split('\n'):
                    match = padrao.search(linha)
                    if match:
                        nome, partido, uf = match.groups()
                        dados.append((nome.strip(), partido.strip(), uf.strip()))

# Remover duplicatas
dados_unicos = list(set(dados))

# Garantir que a pasta existe
os.makedirs(os.path.dirname(saida_csv), exist_ok=True)

# Salvar CSV
with open(saida_csv, "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["nome", "partido", "uf"])
    for linha in dados_unicos:
        writer.writerow(linha)

print(f"✅ CSV com todos os senadores gerado: {saida_csv}")

#NÃO TESTADO COMPLETO: É PARA ESSE PROGRAMA LER TODOS OS PDFS DE CADA SENADOR E PEGAR O NOME, PARTIDO E UF