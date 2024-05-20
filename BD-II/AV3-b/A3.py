## Aqui está um exemplo de um programa Python que percorre os registros obtidos pela consulta A1a (clientes com aluguéis ativos):
import mysql.connector

# Conecta ao banco de dados
conn = mysql.connector.connect(
    host="localhost",
    user="aluno@D07-PC10",
    password="root",
    database="sakila"
)

# Cria um cursor
cursor = conn.cursor()

# Consulta SQL
sql = """
    SELECT first_name, last_name
    FROM customer
    WHERE customer_id IN (SELECT customer_id FROM rental WHERE return_date IS NULL)
"""

# Executa a consulta
cursor.execute(sql)

# Percorre os registros
for (first_name, last_name) in cursor:
    print(f"Nome: {first_name} {last_name}")

# Fecha a conexão
conn.close()

## Certifique-se de substituir "seu_host", "seu_usuario" e "sua_senha" pelas informações corretas de conexão ao seu banco de dados MySQL.