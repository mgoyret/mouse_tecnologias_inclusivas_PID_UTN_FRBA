import threading as td
from time import sleep
import server as sv
import audio as ad
from gui import Gui
import mouse as ms
import myConfig as mc

if __name__ == "__main__":


    td_bienvenida = td.Thread(target=ad.tss, args=['Hola! bienvenido al mouse controlado'])
    td_bienvenida.daemon = True
    td_bienvenida.start()

    root = Gui()
    # el siguiente flag se mata desde el server_socket, ver nota alli
    mc.gui_alive = True

    td_socket = td.Thread(target=sv.create_server, args=[root])
    td_socket.daemon = True
    td_socket.start()


    td_mouse = td.Thread(target=ms.mouse, args=[root])
    td_mouse.daemon = True
    td_mouse.start()

    print(f'{__name__}: por abrir interfaz')
    root.start_gui()
    print(f'{__name__}: interfaz cerrada')

    ad.tss('Hasta luego!')

    mc.main_alive = False
    # margen de tiempo para que mueran threads
    sleep(1)
