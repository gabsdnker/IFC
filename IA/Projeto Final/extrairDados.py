# src/scraper.py

import requests
from bs4 import BeautifulSoup
import pandas as pd

def get_senadores_em_exercicio():
    url = "https://www25.senado.leg.br/web/senadores/em-exercicio"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")

    tabela = soup.find("table", {"summary": "Senadores em exercício"})
    linhas = tabela.find_all("tr")[1:]  # pula o cabeçalho

    senadores = []

    for linha in linhas:
        colunas = linha.find_all("td")

        nome = colunas[0].get_text(strip=True)
        partido_uf = colunas[1].get_text(strip=True)

        if " - " in partido_uf:
            partido, uf = partido_uf.split(" - ")
        else:
            partido, uf = partido_uf, ""

        senadores.append({
            "nome": nome,
            "partido": partido,
            "uf": uf
        })

    df = pd.DataFrame(senadores)
    return df


if __name__ == "__main__":
    df_senadores = get_senadores_em_exercicio()
    df_senadores.to_csv("data/senadores.csv", index=False)
    print("Arquivo senadores.csv salvo com sucesso!")

