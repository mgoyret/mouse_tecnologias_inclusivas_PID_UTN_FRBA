import socket as sk
from time import sleep
import keyboard as kb
import json as js
import myConfig as mc
from tkinter import messagebox

def sk_send(msg: list):
    try:
        generador_socket.send(js.dumps(msg).encode('UTF-8'))
        print(f'{__name__}: envio socket: {js.dumps(msg)}\n')
    except Exception:
        print(f'{__name__}: Error enviando mensaje: {Exception}')


def send_no_key():
    mc.myTecla = mc.no_key_cod
    sk_send(list(['#$', 0, '$#']))


def send_action():
    mc.myTecla = mc.action_code
    sk_send(list(['#$', 1, '$#']))


def send_exit():
    mc.myTecla = mc.exit_code
    sk_send(list(['#$', 2, '$#']))

# eligo action con escape porque la tecla de accionar tiene que ser una tecla que no
# genere ninguna accion al prpesionarse
# - shift: el scrolling se inhabilita
# - block mayus: incomodo, nunca se si deje o no la mayuscula
# - ctrl: con scrolling va a hacer zoom en general
# - tab: tabula, o va desplazando selector en las ventanas
if __name__ == '__main__':
    messagebox.showinfo("Emulador", "El generador a sido iniciado, corre en segundo plano")
    print(f'{__name__}: iniciado')
    try:
        # crear socket INET (IPV4) STREAM (TCP)
        generador_socket = sk.socket(sk.AF_INET, sk.SOCK_STREAM)
        print(f'{__name__}: socket creado')
        # vincular socket a host publico y puerto conocido
        generador_socket.connect((sk.gethostname(), mc.port))
        print(f'{__name__}: socket conectado a {sk.gethostname()}')
        messagebox.showinfo("Emulador", "El generador a sido iniciado, corre en segundo plano")
        while True:
            sleep(0.100) # para ahorrar procesamiento
            if mc.myTecla != mc.no_key_cod and not kb.is_pressed(mc.exit_key) and not kb.is_pressed(mc.action_key):
                send_no_key()
            elif kb.is_pressed(mc.action_key) and mc.myTecla != 1:
                send_action()
            elif kb.is_pressed(mc.exit_key) and mc.myTecla != 2:
                send_exit()
                break
        generador_socket.shutdown(0)
        generador_socket.close()
    except:
        print(f'{__name__}: no se pudo conectar al servidor')
        messagebox.showerror("ERROR", "Probablemente no haya encendido la aplicacion principal\nEnciéndala y vuelva a intentarlo")


    print(f'{__name__}: FIN')
    messagebox.showinfo("Emulador", "Finaliza la ejecucion del generador")
