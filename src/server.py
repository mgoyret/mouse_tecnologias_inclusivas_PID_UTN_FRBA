import socket as sk
import json as js
from types import NoneType
import myConfig as mc

def check(sk_rcv) -> str:
    # print(f'{__name__}: recepcion socket: {sk_rcv}')
    if sk_rcv[0] == '#$' and sk_rcv[2] == '$#':
        res = int(sk_rcv[1])
    else:
        print(f'{__name__}: Error de coordenadas')
        res = -1
    return res

def create_server(x):
    mc.socket_alive = True
    print(f'{__name__}: INICIO server')
    # crear socket INET (IPV4) STREAM (TCP)
    server_socket = sk.socket(sk.AF_INET, sk.SOCK_STREAM)
    try:
        # vincular socket a host publico y puerto conocido
        server_socket.bind((sk.gethostname(), mc.port))
        # prender servidor, ponerlo a la escucha
        server_socket.listen(5)

        print(f'{__name__}: esperando conexion')
        (client_socket, address) = server_socket.accept()
        print(f'{__name__}: conectado a {client_socket}, {address}')
        while mc.main_alive:
            # print(f'{__name__}: escuchando')
            sk_msg = js.loads(client_socket.recv(4096).decode('UTF-8'))
            op = check(sk_msg)
            if op != -1:
                if op == 1:
                    mc.tecla = True
                    print(f'{__name__}: recepcion socket: #$,{1},#$')
                elif op == 0:
                    mc.tecla = False
                if op == 2:
                    if type(x.wd_use) != NoneType:
                        x.use_on_closing()
                    if type(x.wd_config) != NoneType:
                        x.config_on_closing()
                    print(f'{__name__}: cerrando gui')
                    # este flag hace que en la funcion color() de la gui, se destruya sola
                    mc.gui_alive = False
                    while mc.mouse_alive:
                        pass
                    print(f'{__name__}: gui cerrada')
                    break
    except OSError:
        print(f'{__name__}: ERROR: Servidor tomado')
    except Exception as err:
        print(f'{__name__}: ERROR: Problema con el servidor: {err}')

    server_socket.close()
    print(f'{__name__}: fin server')
    mc.socket_alive = False
