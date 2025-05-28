import os
import pandas as pd

pasta_csvs = 'CSVs/Senadores/'
todos_votos = []

# Define os nomes que queremos para as colunas
nomes_colunas = ['DATA', 'NO', 'MATERIA', 'EMENTA', 'DESCRICAO', 'VOTO', 'RESULTADO']

for arquivo in os.listdir(pasta_csvs):
    if arquivo.endswith('.csv'):
        caminho = os.path.join(pasta_csvs, arquivo)
        nome_senador = arquivo.replace('.csv', '').strip()

        try:
            # Lê sem cabeçalho e aplica os nomes fixos
            df = pd.read_csv(caminho, header=None, names=nomes_colunas)

            # Limpa colunas que não interessam e adiciona o nome do senador
            df_filtrado = df[['DATA', 'VOTO']].copy()
            df_filtrado['NOME_SENADOR'] = nome_senador.upper()
            df_filtrado = df_filtrado[['NOME_SENADOR', 'DATA', 'VOTO']]

            # Remove linhas vazias
            df_filtrado = df_filtrado.dropna(subset=['DATA', 'VOTO'])

            todos_votos.append(df_filtrado)

        except Exception as e:
            print(f'Erro ao processar {arquivo}: {e}')

if todos_votos:
    df_unificado = pd.concat(todos_votos, ignore_index=True)
    df_unificado.to_csv('CSVs/Votos 2024/todos_votos_senadores.csv', index=False, encoding='utf-8-sig')
    print('Arquivo todos_votos_senadores.csv gerado com sucesso!')
else:
    print('Nenhum dado válido para concatenar. Verifique os arquivos.')
