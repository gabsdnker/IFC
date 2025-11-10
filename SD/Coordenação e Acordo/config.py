# config.py — configuração da simulação automática Bully

# Número total de nós
NODES = 4

# Todos os nós simulados no localhost (127.0.0.1)
ip_list = ["127.0.0.1"] * NODES
port_list = [5001 + i for i in range(NODES)]

# Tempo entre pings ao coordenador (segundos)
PING_INTERVAL = 3

# Tempo máximo para considerar o coordenador falho (segundos)
PING_TIMEOUT = 4

# Tempo limite para esperar mensagens OK e COORDINATOR
OK_TIMEOUT = 3
COORD_WAIT = 4
