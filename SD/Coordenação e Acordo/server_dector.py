import socket
import config
import threading
from time import sleep
from bully import send_message, start_election, coordinator

nodes_state = {}
nodes_thread = {}

# Inicialização dos estados (1 = suspeito, 0 = não suspeito)
for ip in config.ip_list:
    nodes_state[ip] = 1
for ip in config.ip_list:
    nodes_thread[ip] = [None, threading.Event()]

def timeout(addr):
    """Define o comportamento do timeout"""
    target = config.timeout * 100
    for _ in range(target):
        if nodes_thread[addr][1].is_set():
            nodes_state[addr] = 0
            print(f"[OK] Processo {addr} ativo novamente.")
            nodes_thread[addr][1].clear()
            return
        sleep(0.01)
    print(f"🚨 Processo {addr} ficou suspeito (timeout).")
    nodes_state[addr] = 1

    # Se o suspeito for o coordenador atual, inicia eleição
    if coordinator is None or addr == f"127.0.0.1:{config.port_list[coordinator - 1]}":
        print(f"[ALERTA] Coordenador falhou. Iniciando eleição...")
        start_election()

def run_server():
    ip = config.ip_list[config.pid - 1]
    port = config.port_list[config.pid - 1]
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((ip, port))
        s.listen()
        print(f"🖥️  Servidor P{config.pid} rodando em {ip}:{port}")

        while True:
            conn, addr = s.accept()
            with conn:
                data = conn.recv(1024)
                if not data:
                    continue
                msg = data.decode('utf-8')
                parts = msg.split()
                sender_pid = int(parts[0])
                msg_type = parts[1]
                sender_addr = f"{ip}:{config.port_list[sender_pid - 1]}"

                if msg_type == "PING":
                    if nodes_thread[sender_addr][0] is not None and nodes_thread[sender_addr][0].is_alive():
                        nodes_thread[sender_addr][1].set()
                        nodes_thread[sender_addr][0].join()

                    nodes_thread[sender_addr][0] = threading.Thread(target=timeout, args=[sender_addr])
                    nodes_thread[sender_addr][0].start()
                    print(f"[PING] Recebido de P{sender_pid}")

                elif msg_type == "ELECTION":
                    if config.pid > sender_pid:
                        print(f"[RESPOSTA] P{config.pid} respondeu ELECTION para P{sender_pid}")
                        send_message(sender_pid, "OK")
                        start_election()

                elif msg_type == "COORDINATOR":
                    print(f"📢 Novo coordenador: P{sender_pid}")

if __name__ == "__main__":
    run_server()
