import pdfplumber
import csv
import re
import os

pasta_pdfs = 'PDFs'
arquivo_saida = 'CSVs/partidos/senadores_nome_partido.csv'

pagina_desejada = 0

# Regex melhorado para pegar nomes com ponto e apóstrofo
padrao = r'(SENADOR(?:A)?: [\w\sÁÉÍÓÚÂÊÔÃÕÇ\.\'-]+) PARTIDO: ([\w/]+)'

senadores = []

for arquivo in os.listdir(pasta_pdfs):
    if arquivo.endswith('.pdf'):
        caminho_pdf = os.path.join(pasta_pdfs, arquivo)
        print(f'Lendo {caminho_pdf}')
        try:
            with pdfplumber.open(caminho_pdf) as pdf:
                if pagina_desejada < len(pdf.pages):
                    pagina = pdf.pages[pagina_desejada]
                    texto_pagina = pagina.extract_text()
                    
                    matches = re.findall(padrao, texto_pagina)
                    for match in matches:
                        nome_completo = match[0].replace('SENADOR: ', '').replace('SENADORA: ', '').strip()
                        partido = match[1].strip()
                        senadores.append({
                            'Nome': nome_completo,
                            'Partido': partido
                        })
                else:
                    print(f'O PDF {arquivo} não tem página {pagina_desejada + 1}')
        except Exception as e:
            print(f'Erro ao processar {caminho_pdf}: {e}')

with open(arquivo_saida, mode='w', newline='', encoding='utf-8') as arquivo_csv:
    writer = csv.DictWriter(arquivo_csv, fieldnames=['Nome', 'Partido'])
    writer.writeheader()
    for senador in senadores:
        writer.writerow(senador)

print(f'CSV gerado com sucesso! Total de registros: {len(senadores)}')
print(f'Arquivo salvo em: {arquivo_saida}')
