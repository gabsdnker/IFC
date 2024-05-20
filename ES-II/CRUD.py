import mysql.connector

def create_connection(host, username, password, database):
    try:
        conn = mysql.connector.connect(
            host=host,
            user=username,
            password=password,
            database=database
        )
        print("Conexão estabelecida com sucesso.")
        return conn
    except mysql.connector.Error as e:
        print(f"Erro ao conectar ao MySQL: {e}")
        return None

def generate_crud_procedures(conn, table_name):
    cursor = conn.cursor()
    cursor.execute(f"DESCRIBE {table_name}")
    columns = cursor.fetchall()
    
    # Criação da stored procedure de INSERT
    insert_query = f"CREATE PROCEDURE {table_name}_insert("
    for column in columns:
        insert_query += f"{column[0]} {column[1]}, "
    insert_query = insert_query[:-2] + ")"
    insert_query += "BEGIN "
    insert_query += f"INSERT INTO {table_name} VALUES ("
    for column in columns:
        insert_query += f"%s, "
    insert_query = insert_query[:-2] + "); END;"
    
    cursor.execute(insert_query)
    
    # Criação da stored procedure de SELECT
    select_query = f"CREATE PROCEDURE {table_name}_select() "
    select_query += f"BEGIN SELECT * FROM {table_name}; END;"
    
    cursor.execute(select_query)
    
    # Criação da stored procedure de UPDATE
    update_query = f"CREATE PROCEDURE {table_name}_update("
    for column in columns:
        update_query += f"{column[0]} {column[1]}, "
    update_query = update_query[:-2] + ")"
    update_query += "BEGIN "
    update_query += f"UPDATE {table_name} SET "
    for column in columns:
        update_query += f"{column[0]} = %s, "
    update_query = update_query[:-2] + " WHERE id = %s; END;"
    
    cursor.execute(update_query)
    
    # Criação da stored procedure de DELETE
    delete_query = f"CREATE PROCEDURE {table_name}_delete(id INT) "
    delete_query += f"BEGIN DELETE FROM {table_name} WHERE id = id; END;"
    
    cursor.execute(delete_query)
    
    cursor.close()
    print("Stored procedures CRUD criadas com sucesso.")

if __name__ == "__main__":
    # Configurações do banco de dados
    host = 'localhost'
    username = 'seu_usuario'
    password = 'sua_senha'
    database = 'seu_banco_de_dados'
    
    # Nome da tabela para a qual você deseja gerar as stored procedures CRUD
    table_name = 'sua_tabela'
    
    # Criação da conexão com o banco de dados
    conn = create_connection(host, username, password, database)
    
    if conn is not None:
        generate_crud_procedures(conn, table_name)
        conn.close()
