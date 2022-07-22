import socket as sk
import keyboard as kb
import json as js
import myConfig as mc


def sk_send(msg: list):
    # crear socket INET (IPV4) STREAM (TCP)
    client_socket = sk.socket(sk.AF_INET, sk.SOCK_STREAM)
    try:
        # vincular socket a host publico y puerto conocido
        client_socket.connect((sk.gethostname(), mc.port))
        # envio senal y cierro el socket
        client_socket.send(js.dumps(msg).encode('UTF-8'))
        client_socket.shutdown(0)
    except:
        print(f'{__name__}: no se pudo conectar al servidor')

    client_socket.close()


def send_no_key():
    mc.myTecla = 0
    sk_send(list(['#$', 0, '$#']))


def send_action():
    mc.myTecla = 1
    sk_send(list(['#$', 1, '$#']))


def send_exit():
    mc.myTecla = 2
    sk_send(list(['#$', 2, '$#']))

# eligo action con escape porque la tecla de accionar tiene que ser una tecla que no
# genere ninguna accion al prpesionarse
# - shift: el scrolling se inhabilita
# - block mayus: incomodo, nunca se si deje o no la mayuscula
# - ctrl: con scrolling va a hacer zoom en general
# - tab: tabula, o va desplazando selector en las ventanas
if __name__ == '__main__':
    print(f'{__name__}: iniciado')
    while True:
        if mc.myTecla != 0 and not kb.is_pressed(mc.exit_key) and not kb.is_pressed(mc.exit_key):
            send_no_key()
        elif kb.is_pressed(mc.action_key) and mc.myTecla != 1:
            send_action()
        elif kb.is_pressed(mc.exit_key) and mc.myTecla != 2:
            send_exit()
            break
