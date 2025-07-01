# 🧠 SOM do Senado: Agrupamento Ideológico de Votação

Este projeto utiliza **Mapas Auto-Organizáveis (Self-Organizing Maps - SOM)** para analisar e visualizar agrupamentos de senadores brasileiros com base nos seus votos nominais em 2024.

## 📌 Objetivo

Agrupar senadores por **semelhança de voto** e representar graficamente os grupos ideológicos:
- Esquerda (🟣)
- Centro (🟠)
- Direita (🔵)

## 🗂️ Dados Utilizados

- `matriz_votos_senadores.csv`: matriz de votação com senadores como linhas e votações como colunas, com valores:
  - `1` = votou SIM / AP / Votou
  - `-1` = votou NÃO
  - `0` = ausente, abstenção ou obstrução
- `senadores_juntos.csv`: nome, partido e posição ideológica de cada senador.

## 🔧 Tecnologias

- Python 3.11+
- Pandas, NumPy
- MiniSom
- scikit-learn
- Matplotlib

## 📈 Resultado

A imagem abaixo mostra a visualização SOM com:
- **Cor da borda**: representa o cluster (agrupamento matemático)
- **Cor de preenchimento e forma**: representa a ideologia política

![SOM Senadores](imagens/som_senadores.png)

## ▶️ Como executar

1. Clone o repositório:
   ```bash
   git clone https://github.com/gabsdnker/Projeto-SOM-Senado.git
   cd Projeto-SOM-Senado
