import csv

entrada_csv = 'CSVs/partidos/senadores_nome_partido.csv'
saida_csv = 'CSVs/partidos/senadores_classificados.csv'

partidos_esquerda = ['PT', 'PSOL', 'PCdoB', 'PDT', 'PSB', 'REDE']
partidos_direita = ['PL', 'PP', 'REPUBLICANOS', 'UNIÃO', 'NOVO', 'PSL']
partidos_centro = ['MDB', 'PSD', 'PSDB', 'CIDADANIA', 'PODEMOS', 'AVANTE', 'PATRIOTA']

senadores_classificados = []

with open(entrada_csv, mode='r', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        partido = row['Partido']
        if partido in partidos_esquerda:
            posicao = 'Esquerda'
        elif partido in partidos_direita:
            posicao = 'Direita'
        elif partido in partidos_centro:
            posicao = 'Centro'
        else:
            posicao = 'Indefinido'
        
        senadores_classificados.append({
            'Nome': row['Nome'],
            'Partido': partido,
            'Posição': posicao
        })

with open(saida_csv, mode='w', newline='', encoding='utf-8') as csvfile:
    fieldnames = ['Nome', 'Partido', 'Posição']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    for senador in senadores_classificados:
        writer.writerow(senador)

print(f'✅ CSV com classificação gerado em: {saida_csv}')
