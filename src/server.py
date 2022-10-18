import socket as sk
import json as js
from types import NoneType
import myConfig as mc
import tkinter as tk
from tkinter import messagebox

class Server():

    server_socket = None

    def __init__(self) -> None:
        pass

    def close_server(self):
        self.server_socket.close()
        print(f'{__name__}: fin server')
        mc.socket_alive = False

    def check(self, sk_rcv) -> str:
        # print(f'{__name__}: recepcion socket: {sk_rcv}')
        if sk_rcv[0] == '#$' and sk_rcv[2] == '$#':
            res = int(sk_rcv[1])
        else:
            print(f'{__name__}: Error de coordenadas')
            res = -1
        return res

    def create_server(self, x):
        mc.socket_alive = True
        print(f'{__name__}: INICIO server')
        # crear socket INET (IPV4) STREAM (TCP)
        self.server_socket = sk.socket(sk.AF_INET, sk.SOCK_STREAM)
        try:
            # vincular socket a host publico y puerto conocido
            self.server_socket.bind((sk.gethostname(), mc.port))
            # prender servidor, ponerlo a la escucha
            self.server_socket.listen(5)

            print(f'{__name__}: esperando conexion')
            (emulador_socket, address) = self.server_socket.accept()
            print(f'{__name__}: conectado a {emulador_socket}, {address}')
            while mc.main_alive:

                #print(f'{__name__}: escuchando')
                # si esta esperando mensaje y la gui se cierra por la cruz, este thread queda aca
                sk_msg = js.loads(emulador_socket.recv(4096).decode('UTF-8'))
                op = self.check(sk_msg)
                if op != -1:
                    if op == 1: # TECLA PRESIONADA
                        mc.tecla = True
                        print(f'{__name__}: recepcion socket: #$,{1},#$')
                    elif op == 0: # TECLA SOLTADA
                        mc.tecla = False
                    if op == 2: # TECLA SALIR, solo para debug
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
                if not mc.gui_alive:
                    break # por si la gui se cierra inesperadamente o mediante la cruz
        except Exception as err:
            print(f'{__name__}: ERROR: Problema con el servidor: {err}')
            messagebox.showerror("ERROR", "Error con el servidor")
            # este flag hace que en la funcion color() de la gui, se destruya sola
            mc.gui_alive = False
            while mc.mouse_alive:
                pass
            print(f'{__name__}: gui cerrada')


        self.close_server()
