import socket

# Definindo o host alvo e as portas a serem verificadas
target_host = "127.0.0.1"
target_ports = [21, 22, 80, 443, 8080]

# Loop para verificar cada porta
for port in target_ports:
    # Criando o objeto socket
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Definindo o timeout para 1 segundo
    client.settimeout(1)

    try:
        # Tentando conectar à porta
        client.connect((target_host, port))

        # Exibindo uma mensagem caso a porta esteja aberta
        print("Porta {} aberta".format(port))

        # Fechando a conexão
        client.close()

    except:
        # Exibindo uma mensagem caso a porta esteja fechada
        print("Porta {} fechada".format(port))
