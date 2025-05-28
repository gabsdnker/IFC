import pandas as pd

# Lê o arquivo unificado
df = pd.read_csv('CSVs/Votos 2024/todos_votos_senadores.csv')

# Função para mapear votos
def mapear_voto(voto):
    voto = str(voto).strip().upper()
    if voto in ['SIM', 'AV', 'VOTOU']:
        return 1
    elif voto == 'NÃO':
        return -1
    else:
        return 0

# Aplica a função
df['VOTO_NUM'] = df['VOTO'].apply(mapear_voto)

# Cria matriz: linhas = senadores, colunas = DATA, valores = voto numérico
matriz = df.pivot_table(index='NOME_SENADOR', columns='DATA', values='VOTO_NUM', aggfunc='max')

# Preenche NaN com 0 e força valores discretos
matriz = matriz.fillna(0)
matriz = matriz.applymap(lambda x: 1 if x > 0 else (-1 if x < 0 else 0))

# Salva a matriz em CSV
matriz.to_csv('CSVs/Votos 2024/matriz_votos_senadores.csv', encoding='utf-8-sig')

print('Arquivo matriz_votos_senadores.csv gerado com sucesso!')
