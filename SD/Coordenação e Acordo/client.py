import socket
import config
from time import sleep

def run_client():
    while True:
        for i in range(len(config.ip_list)):
            if i + 1 != config.pid:
                ip = config.ip_list[i]
                port = config.port_list[i]
                with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                    try:
                        s.connect((ip, port))
                        s.sendall(f"{config.pid} PING".encode())
                        print(f"[PING] Enviado de P{config.pid} → P{i+1}")
                    except:
                        print(f"[ERRO] P{config.pid} não conseguiu enviar para P{i+1}")
        sleep(config.sleep_time)

if __name__ == "__main__":
    run_client()
