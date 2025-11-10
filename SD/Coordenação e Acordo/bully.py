import socket
import threading
import time
import config
from datetime import datetime

def now(): return datetime.now().strftime("%H:%M:%S")

pid = int(input(f"Digite o PID deste processo (1 a {config.NODES}): "))
if not (1 <= pid <= config.NODES):
    raise SystemExit("PID inválido.")

local_ip = config.ip_list[pid - 1]
local_port = config.port_list[pid - 1]

coordinator_lock = threading.Lock()
coordinator = None
participating = False
got_ok_event = threading.Event()
got_coord_event = threading.Event()

def log(*msg): print(f"[{now()}] ", *msg)

def send_message(target_pid, message, timeout=1.5):
    ip = config.ip_list[target_pid - 1]
    port = config.port_list[target_pid - 1]
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(timeout)
            s.connect((ip, port))
            s.sendall(message.encode())
        return True
    except Exception:
        return False

def announce_coordinator(new_coord):
    global coordinator, participating
    with coordinator_lock:
        coordinator = new_coord
    log(f" P{new_coord} é o novo coordenador!")
    for t in range(1, config.NODES + 1):
        if t == pid:
            continue
        send_message(t, f"COORDINATOR:{new_coord}")
    participating = False

def start_election():
    global participating
    if participating:
        return
    participating = True
    got_ok_event.clear()
    got_coord_event.clear()

    log(f" P{pid} iniciou uma eleição...")
    higher = [i+1 for i in range(pid, config.NODES)]
    for h in higher:
        sent = send_message(h, f"ELECTION:{pid}")
        log(f"→ Enviado ELECTION para P{h} (ok={sent})")

    # Espera OK
    if not got_ok_event.wait(config.OK_TIMEOUT):
        announce_coordinator(pid)
        return
    else:
        log("⏳ Aguardando anúncio do novo coordenador...")
        if got_coord_event.wait(config.COORD_WAIT):
            log(f"Coordenador agora é P{coordinator}")
        else:
            log(" Nenhum coordenador anunciado — reiniciando eleição.")
            start_election()
    participating = False

def handle_message(msg):
    global coordinator
    if msg.startswith("ELECTION:"):
        sender = int(msg.split(":")[1])
        log(f" Recebido ELECTION de P{sender}")
        if pid > sender:
            send_message(sender, f"OK:{pid}")
            start_election()
    elif msg.startswith("OK:"):
        got_ok_event.set()
    elif msg.startswith("COORDINATOR:"):
        new_coord = int(msg.split(":")[1])
        with coordinator_lock:
            coordinator = new_coord
        got_coord_event.set()
        log(f" P{new_coord} anunciado como coordenador.")
    elif msg.startswith("PING:"):
        sender = int(msg.split(":")[1])
        send_message(sender, f"PONG:{pid}")
    elif msg.startswith("PONG:"):
        sender = int(msg.split(":")[1])
        if sender == coordinator:
            last_ping[0] = time.time()

def server_loop():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s.bind((local_ip, local_port))
        s.listen(10)
        log(f" P{pid} iniciado em {local_ip}:{local_port}")
        while True:
            conn, _ = s.accept()
            data = conn.recv(1024).decode()
            conn.close()
            if data:
                handle_message(data)

# PING monitor
last_ping = [time.time()]

def ping_monitor():
    global coordinator
    while True:
        time.sleep(config.PING_INTERVAL)
        with coordinator_lock:
            coord = coordinator

        if coord is None:
            continue
        if coord == pid:
            continue

        if not send_message(coord, f"PING:{pid}"):
            log(f"Coordenador P{coord} não respondeu — iniciando eleição.")
            with coordinator_lock:
                coordinator = None
            start_election()
            continue

        # Detecta timeout do coordenador
        if time.time() - last_ping[0] > config.PING_TIMEOUT:
            log(f" Coordenador P{coord} falhou (timeout). Iniciando eleição.")
            with coordinator_lock:
                coordinator = None
            start_election()

def initial_coordinator():
    """Define coordenador inicial como o nó de menor PID ativo."""
    time.sleep(2)
    if pid == 1:
        announce_coordinator(1)

if __name__ == "__main__":
    threading.Thread(target=server_loop, daemon=True).start()
    threading.Thread(target=ping_monitor, daemon=True).start()
    threading.Thread(target=initial_coordinator, daemon=True).start()

    while True:
        time.sleep(1)
