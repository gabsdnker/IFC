import pandas as pd

# Lê os CSVs
df_nome_partido = pd.read_csv('CSVs/partidos/senadores_nome_partido.csv')
df_classificados = pd.read_csv('CSVs/partidos/senadores_classificados.csv')

# Merge pelo 'Nome'
df_merged = pd.merge(df_nome_partido, df_classificados, on='Nome', how='inner')

# Verifica se Partido_x e Partido_y são iguais em todas as linhas
if (df_merged['Partido_x'] == df_merged['Partido_y']).all():
    # Se sim, mantém só uma coluna e renomeia para 'Partido'
    df_merged = df_merged.drop(columns=['Partido_y'])
    df_merged = df_merged.rename(columns={'Partido_x': 'Partido'})
else:
    print("Atenção: colunas Partido_x e Partido_y têm valores diferentes!")

# Salva o resultado final
df_merged.to_csv('CSVs/partidos/senadores_juntos.csv', index=False)

print("Arquivo final salvo como senadores_juntos.csv")