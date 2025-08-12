
import requests
import json
import os
import time
import base64

# SERVER_ADDR = ["http://191.52.7.101:5000", "http://191.52.7.100:5000"]
SERVER_ADDR = ["http://191.52.6.114:5000", "http://191.52.7.91:5000","http://191.52.6.62:5000","http://191.52.7.100:5000","http://191.52.6.63:5000"]

FILE_DIR = "./ClientDir/files"

class File:
    # construtor com valor padrão nos parâmetros
    def __init__(self, name="", id="", modified=""):
        self.name = name
        self.id = id
        self.modified = modified

    # expressar a classe em formato texto
    def __str__(self):
        return f'{self.name}, '+\
               f'{self.id}, {self.modified}'

    # expressar a classe em formato json
    def json(self):
        return {
            "name" : self.name,
            "id" : self.id,
            "modified" : self.modified 
        }

class Client:

    def __init__(self, server_addr=SERVER_ADDR, file_dir=FILE_DIR):
        self.server_addr = server_addr
        self.file_dir = file_dir
        self.client_prev_list = None
        self.client_cur_list = None
        self.server_prev_list = None
        self.server_cur_list = None
        self.operation_list = []

    def list_server_files(self, verbose=False):
        for addr in self.server_addr:
            response = requests.get(f'{addr}/listar').json()
            print((response['files']))
            if verbose:
                for n in response['files']:
                    print(n['name'])
            print(response)
            if response:
                #Pode retornar um erro 
                return response['files']

    def list_local_files(self, verbose=False):
        files = []
        json_files = []

        dirEntrys = os.scandir(self.file_dir)
        
        for entry in dirEntrys:
            if entry.is_file() and entry.name != "client.py":
                file = File(entry.name, entry.stat().st_ino, entry.stat().st_mtime)
                #print(file)
                files.append(file)

        for file in files:
            json_files.append(file.json())

        if verbose:
            print(json_files)

        return json_files

    def create_file(self, file_name):
        erro = False
        for addr in self.server_addr:
            response = requests.get(f'{addr}/criar/{file_name}').json()
            if response['header'] == "OK":
                f = open(f"{self.file_dir}/{file_name}", "w")
                f.close()
            else:
                erro = True

        if not erro:
            return True
        
        return False


    def delete_file(self, file_name):
        response = requests.get(f'{self.server_addr}/deletar/{file_name}').json()
        
        if response['header'] == "OK":
            os.remove(f"{self.file_dir}/{file_name}")
            return True
    
        return False

    def write_to_file(self, file_name, content):
        for addr in self.server_addr:
            response = requests.get(f'{addr}/escrever/{file_name}/{content}').json()
            
            if response['header'] == "OK":
                f = open(f"{self.file_dir}/{file_name}", "w")
                f.write(content)
                f.close()
        
        return True
    
    def upload(self, file_name):
        for addr in self.server_addr:

            files = {'files': open(f'{self.file_dir}/{file_name}', 'rb')}
            response = requests.post(f'{addr}/escrever', files=files).json()
            if response['header'] == "OK":
                print(file_name, "uploaded to", addr)

        return response['header'] == "OK"


    def read_from_file(self, file_name):
        for addr in self.server_addr:
            response = requests.get(f'{addr}/ler/{file_name}').json()
            if response['header'] == "OK":
                return response['detail']
        return None

    def update_local_files(self):
        pass

    def install(self):

        # get the servers folder files list
        
        # create locally all files recovered from the server
        pass

    def merge(self):

        # get the servers folder files list

        # load the list of local files, in the FILE_DIR folder      

        # Compares and find the difference from the two dicts  
        # example of comparison results:
        # [('local_remove','praia.png'), 
        # ('remote_create','texto.txt'), 
        # ('remote_write','texto.txt','este-e-o-conteudo-d)]

        pass

    # Tmp methods
    def dump(self):
        server_files = self.list_server_files()
        
        for file in server_files['files']:
            f = open(f"{self.file_dir}/{file['name']}", "w")
            f.close()


def test():
    client_1 = Client()
    file_name = "newFileFromClient.txt"
    content_to_write = "conteudo-para-teste-de-escrita"

    print("Initial files:")
    client_1.list_server_files(verbose=True)
    #client_1.dump()
    
    print(f"*** Creating file {file_name}")
    client_1.create_file(file_name)

    print("*** The file was created?")
    client_1.list_server_files(verbose=True)
    
    print(f"*** Writing {content_to_write} to {file_name}")
    if client_1.write_to_file(file_name, content_to_write):
        print("Success in writing")
    else:
        print("I could not write :-(")
    
    print("The content was written? Testing file reading...")
    content2 = client_1.read_from_file(file_name)
    print(f"Content read from {file_name}: {content2}")

    print(f"Removing file {file_name}")
    client_1.delete_file(file_name)

    print("Final listing")
    client_1.list_server_files(verbose=True)
    
    #client_1.dump()

# client paratemers for execution:
# install - load all files from server
# merge - compare files between client and server, and do the actions required to make them equals

def run():
    client = Client()
    # Repita:
    while True:
        
        # Se não existir lista local:
        if client.client_prev_list == None:

            # Pegar lista do servidor
            client.server_prev_list = client.list_server_files()
            
            # Para cada item da lista:
            for file in client.server_prev_list:
                # Solicitar arquivo para o servidor e criar no local
                f = open(f"{client.file_dir}/{file['name']}", "w")
                content = client.read_from_file(file['name'])
                if content is not None:
                    f.write(content)
                    f.close()
            
            # Salvar lista local 
            client.client_prev_list = client.server_prev_list
    
        # Inicias sincronismo entre local e remoto:
        else:
            # Obter as listas atuais - local e servidor
            client.client_cur_list = client.list_local_files()
            client.server_cur_list = client.list_server_files()

            # CASO 1- Novo arquivo no local
            # percorre a lista local atual
            for cur_file in client.client_cur_list:
                # Supor que o arquivo não existe
                exists = False
                # procurar arquivo atual na lista anterior
                for prev_file in client.client_prev_list:
                    # se o elemento não existe na anteiror
                    if prev_file['name'] == cur_file['name']:
                        # encontrou o arquivo, sinalizar e interromper busca
                        exists = True
                        break

                # Se o arquivo não existe
                if not exists:
                    # ler conteudo do arquivo
                    #openedFile = open("./files/" + cur_file['name'], "r")
                    #conteudo = openedFile.read()
                    # adiciona na lista de execução (add_server, name_arquivo)
                    client.operation_list.append(('add_server',cur_file['name']))

    # -- -- # CASO 2- Novo arquivo no servidor
    # -- -- percorre a lista do servidor atual
    # -- -- -- se o elemento não existe na anteiror
    # -- -- -- -- adiciona na lista de execução (add_local, name_arquivo)
            for cur_file in client.server_cur_list:
                # Supor que o arquivo não existe
                exists = False
                # procurar arquivo atual na lista anterior
                for file in client.client_cur_list:
                    # se o elemento não existe na anteiror
                    if cur_file['name'] == file['name']:
                        # encontrou o arquivo, sinalizar e interromper busca
                        exists = True
                # Se o arquivo não existe
                if not exists:
                    # ler conteudo do arquivo
                    content = client.read_from_file(cur_file['name'])
                    # adiciona na lista de execução (add_local (operation[0]), name_arquivo (operation[1]), conteudo (operation[2]))
                    client.operation_list.append(('add_local',cur_file['name'],content))
               

    # -- -- # CASO 3 - arquivo removido no local
    # -- -- percorre a lista do local anterior
    # -- -- -- se o elemento não existe na atual
    # -- -- -- -- adiciona na lista de execução (remove_server, name_arquivo)

    # -- -- # CASO 4 - arquivo removido no servidor
    # -- -- percorre a lista do servidor anterior
    # -- -- -- se o elemento não existe na atual
    # -- -- -- -- adiciona na lista de execução (remove_local, name_arquivo)

    # -- -- Executar ações na lista
    
            for operation in client.operation_list:
                if(operation[0] == 'add_server'):
                    # cria arquivo no servidor
                    #client.create_file(operation[1])
                    #client.write_to_file(operation[1], operation[2])
                    client.upload(operation[1])
                    print(f"Novo arquivo local enviado para o servidor - {operation[1]}")
                
                elif(operation[0] == 'add_local'):
                    # cria arquivo local
                    file = os.path.join(client.file_dir, operation[1])
                    # abre o arquivo para escrita binária
                    with open(file, "wb") as file:
                        # escreve o conteudo decodificado no arquivo
                        if operation[2] is not None:
                            file.write(base64.b64decode(operation[2]))
                    print(f"Arquivo {operation[1]} baixado do servidor para o cliente.")
                
                elif(operation[0] == 'remove_server'):
                    # remove arquivo do servidor
                    client.remove_file(operation[1])
                
                elif(operation[0] == 'remove_local'):
                    # remove arquivo local
                    os.remove(f"{client.file_dir}/{operation[1]}")

    # -- -- limpa lista de operações
            client.operation_list = []
            
                    
    # -- -- Listas atuais agora são as anteriores
            client.client_prev_list = client.client_cur_list
            client.server_prev_list = client.server_cur_list 

            time.sleep(5) 

if __name__ == "__main__":
    #test()
    run()
