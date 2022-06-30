import socket as sk
import json as js
import myConfig as mc
from time import sleep

def check(sk_rcv) -> str:
    print(f'{__name__}: recepcion socket: {sk_rcv}')
    if sk_rcv[0] == '#$' and sk_rcv[2] == '$#':
        res = int(sk_rcv[1])
    else:
        print(f'{__name__}: Error de coordenadas')
        res = -1
    return res

def create_server(x):
    # crear socket INET (IPV4) STREAM (TCP)
    server_socket = sk.socket(sk.AF_INET, sk.SOCK_STREAM)
    # vincular socket a host publico y puerto conocido
    server_socket.bind((sk.gethostname(), mc.port))
    # prender servidor, ponerlo a la escucha
    server_socket.listen(5)

    while True:
#        print(f'{__name__}: esperando conexion')
        (client_socket, address) = server_socket.accept()
#        print(f'{__name__}: socket conectado: escuchando')
        sk_msg = js.loads(client_socket.recv(4096).decode('UTF-8'))
        op = check(sk_msg)
        if op != -1:
#            print(f'{__name__}: antes {mc.tecla}')
            if op == 1:
                mc.tecla = True
            elif op == 0:
                mc.tecla = False
            if op == 2:
                break
#            print(f'{__name__}: despues {mc.tecla}')
    
    # en este caso, se debe matar la interfaz grafica, ya que se recibio comando de finalizacion
    # El problema es que el thread "mv_mouse" ejecutado desde el main, tiene relacion a la interfaz
    # grafica, y por como funciona tkinter, debe morir si o si antes de que lo haga la GUI. Por lo tanto
    # desde aca mato al mouse mediante el flag "", y luego procedo a finalizar la GUI
    mc.gui_alive = False
    # doy tiempo a que muera el thread "mv_mouse"
    sleep(1)

    x.destroy()
    server_socket.close()
