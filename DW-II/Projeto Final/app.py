# Autores: Gabriel Rodrigues, Gabrielli Danker, and Marco Antonio
# Ultima edição: 18/06/2024

# Imports necessários
from flask import Flask, request, session, render_template, redirect, url_for
from flask_session import Session
import mysql.connector 
import hashlib

# Inicia o Flask
app = Flask("Goal Tickets")

# Define o Secret_key e o type da session
app.config['SECRET_KEY'] = 'vasco_da_gama'
app.config['SESSION_TYPE'] = 'filesystem'

# Cria a Session
Session(app)

# Define o banco de dados e suas configurações
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Root123!",
)

# Define o cursor
cursor = db.cursor()

# Criar o banco de dados "Usuários" se não existir
cursor.execute("CREATE DATABASE IF NOT EXISTS Usuários")
cursor.execute("USE Usuários")

# Cria a tabela de informações de cadastro do usuário
cursor.execute("CREATE TABLE IF NOT EXISTS info_cadastro (id INT AUTO_INCREMENT PRIMARY KEY, nome VARCHAR(255), cpf VARCHAR(255), email VARCHAR(255), ddd VARCHAR(2), celular VARCHAR(9), senha VARCHAR(255))")

# Define as variáveis
status = "deslogado"
nome_perfil = ""
cpf_perfil = ""
email_perfil = ""
ddd_perfil = ""
cel_perfil = ""
senha_digitada = ""
email_digitado = ""
cadastro = ""
genero_perfil = ""
dia_perfil = ""
mes_perfil = ""
ano_perfil = ""
cep_perfil = ""
cidade_perfil = ""
bairro_perfil = ""
rua_perfil = ""
numero_perfil = ""
complemento_perfil = ""
add_info_extras = ""
cpf_usuario = ""
executado = False


################################################################################################################################


@app.route('/')
def index():
    # Define as variáveis globais
    global status, nome_perfil

    # Renderiza o template de HOME passando as variáveis necessárias
    return render_template('index.html', status=status, nome_perfil=nome_perfil)

@app.route('/Ajuda')
def ajuda():
    # Define as variáveis globais
    global status, nome_perfil

    # Renderiza o template de dúvidas passando as variáveis necessárias
    return render_template("ajuda.html", status=status, nome_perfil=nome_perfil)

@app.route('/SignUp')
def nova_conta():
    # Define as variáveis globais
    global status, nome_perfil

    # Renderiza o template de cadastro passando as variáveis necessárias
    return render_template("nova_conta.html", status=status, nome_perfil=nome_perfil)

@app.route('/Login')
def conta():
    # Define as variáveis globais
    global status, nome_perfil, senha_digitada, email_digitado, cadastro, executado
    
    # Renderiza o template de login passando as variáveis necessárias
    return render_template("conta.html", status=status, nome_perfil=nome_perfil, senha_digitada=senha_digitada, email_digitado=email_digitado, cadastro=cadastro)

@app.route('/Perfil')
def perfil():
    # Define as variáveis globais
    global nome_perfil, cpf_perfil, email_perfil, ddd_perfil, cel_perfil, status, genero_perfil, dia_perfil, mes_perfil, ano_perfil, cep_perfil, cidade_perfil, bairro_perfil, rua_perfil, numero_perfil, complemento_perfil, cpf_usuario, executado

    # Verifica se o usuário já está logado e se esse bloco de código já foi executado
    if status == "Logado" and executado == False:
        # Seleciona os dados extras adicionados na tabela referente ao cpf que está logado atualmente
        cpf_usuario = dados[1]
        comando5 = "SELECT genero, dia, mes, ano, cep, cidade, bairro, rua, numero, complemento FROM info_extra WHERE cpf = %s"
        cursor.execute(comando5, (cpf_usuario,))
        resultado_comando5 = cursor.fetchone()

        # Cria a sessão do usuário
        session['usuario'] = cpf_usuario
        executado = True

        # Verifica se o usuário está na sessão
        if 'usuario' in session:
            nome_perfil = dados[0]
            cpf_perfil = dados[1]
            email_perfil = dados[2]
            ddd_perfil = dados[3]
            cel_perfil = dados[4]
            print(nome_perfil, cpf_perfil, email_perfil, ddd_perfil, cel_perfil)

            # Verifica se está sendo adicionado alguma nova informação no perfil do usuário
            if resultado_comando5 is not None:
                genero_perfil = resultado_comando5[0]
                dia_perfil = resultado_comando5[1]
                mes_perfil = resultado_comando5[2]
                ano_perfil = resultado_comando5[3]
                cep_perfil = resultado_comando5[4]
                cidade_perfil = resultado_comando5[5]
                bairro_perfil = resultado_comando5[6]
                rua_perfil = resultado_comando5[7]
                numero_perfil = resultado_comando5[8]
                complemento_perfil = resultado_comando5[9]
                
            else:
                cursor.fetchall()

    # Renderiza o template do perfil passando as variáveis necessárias
    return render_template("perfil.html", nome_perfil=nome_perfil, cpf_perfil=cpf_perfil, email_perfil=email_perfil, ddd_perfil=ddd_perfil, cel_perfil=cel_perfil, status=status, genero_perfil=genero_perfil, dia_perfil=dia_perfil, mes_perfil=mes_perfil, ano_perfil=ano_perfil, cep_perfil=cep_perfil, cidade_perfil=cidade_perfil, bairro_perfil=bairro_perfil, rua_perfil=rua_perfil, numero_perfil=numero_perfil, complemento_perfil=complemento_perfil)

@app.route('/EsqueceuSenha')
def esqueceu_senha():
    # Define as variáveis globais
    global status, nome_perfil

    # Renderiza o template "esqueci minha senha" passando as variáveis necessárias
    return render_template("esqueceu_senha.html", status=status, nome_perfil=nome_perfil)

@app.route('/Rodada1')
def jogos():
    # Define as variáveis globais
    global status, nome_perfil

    # Renderiza o template da Rodada-1 passando as variáveis necessárias
    return render_template("jogos.html", status=status, nome_perfil=nome_perfil)

@app.route('/Rodada2')
def jogos_2():
    # Define as variáveis globais
    global status, nome_perfil

    # Renderiza o template da Rodada-2 passando as variáveis necessárias
    return render_template("jogos_2.html", status=status, nome_perfil=nome_perfil)

@app.route('/Rodada3')
def jogos_3():
    # Define as variáveis globais
    global status, nome_perfil

    # Renderiza o template da Rodada-3 passando as variáveis necessárias
    return render_template("jogos_3.html", status=status, nome_perfil=nome_perfil)

@app.route('/Pagamento')
def pagamento():
    # Define as variáveis globais
    global status, nome_perfil

    # Renderiza o template da Rodada-3 passando as variáveis necessárias
    return render_template("pagamento.html", status=status, nome_perfil=nome_perfil)

########################### JOGOS DA RODADA 1 ###########################

@app.route('/Rodada1-Jogo1')
def jogo_1_1():
    global status, nome_perfil
    return render_template('jogos/Rodada-1/jogo-1.html', status=status, nome_perfil=nome_perfil)

@app.route('/Rodada1-Jogo2')
def jogo_1_2():
    global status, nome_perfil
    return render_template('jogos/Rodada-1/jogo-2.html', status=status, nome_perfil=nome_perfil)
@app.route('/Rodada1-Jogo3')

def jogo_1_3():
    global status, nome_perfil
    return render_template('jogos/Rodada-1/jogo-3.html', status=status, nome_perfil=nome_perfil)

@app.route('/Rodada1-Jogo4')
def jogo_1_4():
    global status, nome_perfil
    return render_template('jogos/Rodada-1/jogo-4.html', status=status, nome_perfil=nome_perfil)

@app.route('/Rodada1-Jogo5')
def jogo_1_5():
    global status, nome_perfil
    return render_template('jogos/Rodada-1/jogo-5.html', status=status, nome_perfil=nome_perfil)

@app.route('/Rodada1-Jogo6')
def jogo_1_6():
    global status, nome_perfil
    return render_template('jogos/Rodada-1/jogo-6.html', status=status, nome_perfil=nome_perfil)

@app.route('/Rodada1-Jogo7')
def jogo_1_7():
    global status, nome_perfil
    return render_template('jogos/Rodada-1/jogo-7.html', status=status, nome_perfil=nome_perfil)

@app.route('/Rodada1-Jogo8')
def jogo_1_8():
    global status, nome_perfil
    return render_template('jogos/Rodada-1/jogo-8.html', status=status, nome_perfil=nome_perfil)

@app.route('/Rodada1-Jogo9')
def jogo_1_9():
    global status, nome_perfil
    return render_template('jogos/Rodada-1/jogo-9.html', status=status, nome_perfil=nome_perfil)

@app.route('/Rodada1-Jogo10')
def jogo_1_10():
    global status, nome_perfil
    return render_template('jogos/Rodada-1/jogo-10.html', status=status, nome_perfil=nome_perfil)

########################### JOGOS DA RODADA 2 ###########################

@app.route('/Rodada2-Jogo1')
def jogo_2_1():
    global status, nome_perfil
    return render_template('jogos/Rodada-2/jogo-1.html', status=status, nome_perfil=nome_perfil)

@app.route('/Rodada2-Jogo2')
def jogo_2_2():
    global status, nome_perfil
    return render_template('jogos/Rodada-2/jogo-2.html', status=status, nome_perfil=nome_perfil)

@app.route('/Rodada2-Jogo3')
def jogo_2_3():
    global status, nome_perfil
    return render_template('jogos/Rodada-2/jogo-3.html', status=status, nome_perfil=nome_perfil)

@app.route('/Rodada2-Jogo4')
def jogo_2_4():
    global status, nome_perfil
    return render_template('jogos/Rodada-2/jogo-4.html', status=status, nome_perfil=nome_perfil)

@app.route('/Rodada2-Jogo5')
def jogo_2_5():
    global status, nome_perfil
    return render_template('jogos/Rodada-2/jogo-5.html', status=status, nome_perfil=nome_perfil)

@app.route('/Rodada2-Jogo6')
def jogo_2_6():
    global status, nome_perfil
    return render_template('jogos/Rodada-2/jogo-6.html', status=status, nome_perfil=nome_perfil)

@app.route('/Rodada2-Jogo7')
def jogo_2_7():
    global status, nome_perfil
    return render_template('jogos/Rodada-2/jogo-7.html', status=status, nome_perfil=nome_perfil)

@app.route('/Rodada2-Jogo8')
def jogo_2_8():
    global status, nome_perfil
    return render_template('jogos/Rodada-2/jogo-8.html', status=status, nome_perfil=nome_perfil)

@app.route('/Rodada2-Jogo9')
def jogo_2_9():
    global status, nome_perfil
    return render_template('jogos/Rodada-2/jogo-9.html', status=status, nome_perfil=nome_perfil)

@app.route('/Rodada2-Jogo10')
def jogo_2_10():
    global status, nome_perfil
    return render_template('jogos/Rodada-2/jogo-10.html', status=status, nome_perfil=nome_perfil)

########################### JOGOS DA RODADA 3 ###########################

@app.route('/Rodada3-Jogo1')
def jogo_3_1():
    global status, nome_perfil
    return render_template('jogos/Rodada-3/jogo-1.html', status=status, nome_perfil=nome_perfil)

@app.route('/Rodada3-Jogo2')
def jogo_3_2():
    global status, nome_perfil
    return render_template('jogos/Rodada-3/jogo-2.html', status=status, nome_perfil=nome_perfil)

@app.route('/Rodada3-Jogo3')
def jogo_3_3():
    global status, nome_perfil
    return render_template('jogos/Rodada-3/jogo-3.html', status=status, nome_perfil=nome_perfil)

@app.route('/Rodada3-Jogo4')
def jogo_3_4():
    global status, nome_perfil
    return render_template('jogos/Rodada-3/jogo-4.html', status=status, nome_perfil=nome_perfil)

@app.route('/Rodada3-Jogo5')
def jogo_3_5():
    global status, nome_perfil
    return render_template('jogos/Rodada-3/jogo-5.html', status=status, nome_perfil=nome_perfil)

@app.route('/Rodada3-Jogo6')
def jogo_3_6():
    global status, nome_perfil
    return render_template('jogos/Rodada-3/jogo-6.html', status=status, nome_perfil=nome_perfil)

@app.route('/Rodada3-Jogo7')
def jogo_3_7():
    global status, nome_perfil
    return render_template('jogos/Rodada-3/jogo-7.html', status=status, nome_perfil=nome_perfil)

@app.route('/Rodada3-Jogo8')
def jogo_3_8():
    global status, nome_perfil
    return render_template('jogos/Rodada-3/jogo-8.html', status=status, nome_perfil=nome_perfil)

@app.route('/Rodada3-Jogo9')
def jogo_3_9():
    global status, nome_perfil
    return render_template('jogos/Rodada-3/jogo-9.html', status=status, nome_perfil=nome_perfil)

@app.route('/Rodada3-Jogo10')
def jogo_3_10():
    global status, nome_perfil
    return render_template('jogos/Rodada-3/jogo-10.html', status=status, nome_perfil=nome_perfil)


################################################################################################################################


@app.route('/registrar', methods=['POST'])
def submit():
    # Define as variáveis globais
    global cadastro

    # Pega os dados digitados no formulário de cadastro de usuário
    nome = request.form['nome']
    cpf = corrigiCPF(request.form['cpf'])
    email = request.form['email']
    ddd = request.form['ddd']
    celular = request.form['celular']
    senha = request.form['senha']

    # Faz o hash na senha digitada
    senha_hash_obj = hashlib.sha1(senha.encode())
    senha_hash = senha_hash_obj.hexdigest()

    # Insere os dados do form na tabela de cadastrados
    cursor.execute("INSERT INTO info_cadastro (nome, cpf, email, ddd, celular, senha) VALUES (%s, %s, %s, %s, %s, %s)", (nome, cpf, email, ddd, celular, senha_hash))
    db.commit()
    cadastro = "Criado"

    # Redericiona o usuário para a página de login
    return redirect(url_for('conta'))

def corrigiCPF(cpf: str):
    # Pega o cpf digitado e coloca em seu formato correto
    cpf = cpf[:3] + "." + cpf[3:]
    cpf = cpf[:7] + "." + cpf[7:]
    cpf = cpf[:11] + "-" + cpf[11:]
    
    return cpf

@app.route('/login', methods=['POST'])
def login():
    # Define as variáveis globais
    global status, email, dados, senha_digitada, email_digitado, nome_perfil, cpf_perfil, email_perfil, ddd_perfil, cel_perfil
    
    # Pega o email digitado no form de login
    email = request.form['email']
    
    # Verifica se o e-mail existe na tabela de cadastrados
    comando1 = "SELECT email FROM info_cadastro WHERE email = %s;"
    cursor.execute(comando1, (email,))
    resultado_email = cursor.fetchone()

    # Se não existir...
    if resultado_email is None:
        email_digitado = "Invalido"
        return redirect(url_for('conta'))
    
    # Se existir...
    else:
        # Pega a senha atribuida ao e-mail digitado
        email_digitado = "Correto"
        comando2 = "SELECT senha FROM info_cadastro WHERE email = %s;"
        cursor.execute(comando2, (email,))
        resultado_senha = cursor.fetchone()
        verifica_senha = resultado_senha[0]

        # Pega a senha digitada no form de login
        input_senha = request.form['senha']

        # Faz o hash da senha digitada
        senha_hash_obj2 = hashlib.sha1(input_senha.encode())
        senha = senha_hash_obj2.hexdigest()

        # Compara a senha digitada com a senha salva na tabela de cadastrados
        if senha == verifica_senha:
            # Credenciais validadas, usuário logado
            status = "Logado"
            senha_digitada = "Correta"

            # Seleciona os dados cadastrados atribuidos ao e-mail do usuário logado atualmente
            comando3 = "SELECT nome, cpf, email, ddd, celular FROM info_cadastro WHERE email = %s"
            cursor.execute(comando3, (email,))
            dados = cursor.fetchone()

            # Define o nome cadastrado pelo usuário
            nome_perfil = dados[0]

            # Cria a tabela das informações extras do perfil do usuário
            cursor.execute("CREATE TABLE IF NOT EXISTS info_extra (id INT AUTO_INCREMENT PRIMARY KEY, nome VARCHAR(255), cpf VARCHAR(255), genero VARCHAR(255), dia VARCHAR(255), mes VARCHAR(255), ano VARCHAR(255), cep VARCHAR(255), cidade VARCHAR(255), bairro VARCHAR(255), rua VARCHAR(255), numero VARCHAR(255), complemento VARCHAR(255))")

            # Redereciona o usuário para a home do site
            return redirect(url_for('index'))

        # Caso a senha não seja validada...
        else:
            status = "deslogado"
            senha_digitada = "Invalida"
            return redirect(url_for('conta'))
        

@app.route('/info_add', methods=['POST'])
def info_extras():
    # Define as variáveis globais
    global email, genero_perfil, cpf_usuario
    
    # Pega as informações adicionais digitadas no formulário do perfil do usuário
    genero = request.form.get('genero')
    dia = request.form.get('dia')
    mes = request.form.get('mes')
    ano = request.form.get('ano')
    cep = request.form['cep']
    cidade = request.form['cidade']
    bairro = request.form['bairro']
    rua = request.form['rua']
    numero = request.form['numero']
    complemento = request.form['complemento']

    # Pega o nome e cpf do usuário que está logado atualmente
    comando = "SELECT nome, cpf FROM info_cadastro WHERE email = %s;"
    cursor.execute(comando, (email,))
    resultado = cursor.fetchone()
    nome = resultado[0]
    cpf = resultado[1]

    # Insere as informações adicionais de perfil na tabela de informações extras
    cursor.execute("INSERT INTO info_extra (nome, cpf, genero, dia, mes, ano, cep, cidade, bairro, rua, numero, complemento) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", (nome, cpf, genero, dia, mes, ano, cep, cidade, bairro, rua, numero, complemento))
    db.commit()

    # Redereciona o usuário para a página de perfil
    return redirect(url_for('perfil'))

@app.route('/logout')
def logout():
    global status, executado

    status = "deslogado"
    executado = False
    session.clear()

    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
