import requests
from bs4 import BeautifulSoup
import pandas as pd

# pip install requests beautifulsoup4 pandas

url= "https://placarcongresso.com/pages/s-ranking.html"

response = requests.get(url)
response.encoding = 'utf-8'
soup = BeautifulSoup(response.text, "html.parser")

table = soup.find("table")

senadores= []
partidos= []

for row in table.find_all("tr")[1:]:
    cols = row.find_all("td")
    if len(cols)>= 3:
        nome= cols[1].get_text(strip= True)
        partido = cols[2].get_text(strip = True)
        senadores.append(nome)
        partidos.append(partido)

df = pd.DataFrame({"Senadores": senadores, "Partidos": partidos})

df.to_csv("senadores_partidos.csv", index=False, encoding="utf-8")

print(df.head())
