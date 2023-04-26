# Port-Scan
Port Scan - Python3

Nesse exemplo, definimos um host alvo (127.0.0.1) e uma lista de portas a serem verificadas (21, 22, 80, 443 e 8080). Em seguida, usamos um loop para verificar cada uma dessas portas. Para cada porta, criamos um objeto socket, definimos um timeout de 1 segundo e tentamos conectar à porta usando o método connect(). Se a conexão for bem-sucedida, exibimos uma mensagem dizendo que a porta está aberta e fechamos a conexão. Se a conexão falhar, exibimos uma mensagem dizendo que a porta está fechada.
