import threading as td
from time import sleep
import server as sv
import audio as ad
from gui import Gui
import mouse as ms
import myConfig as mc

if __name__ == "__main__":

# comento por comodidad al probar
#    td_bienvenida = td.Thread(target=ad.tss, args=['Hola! bienvenido al mouse controlado'])
#    td_bienvenida.daemon = True
#    td_bienvenida.start()

    root = Gui()
    # las imagenes son lo que mas tardan en cargar. Las cargo antes de arrancar los threads, asi lo hace mucho mas rapido,
    # y aparte ya quedan cargadas hasta que se finalice el programa
    print("CARGANDO FOTOS")
    mc.cargar_fotos()
    print("FIN CARGA FOTOS")

    td_socket = td.Thread(target=sv.create_server, args=[root])
    td_socket.daemon = True
    td_socket.start()

    mouseObject = ms.Mouse()
    td_mouse = td.Thread(target=mouseObject.mouse, args=[root])
    td_mouse.daemon = True
    td_mouse.start()

    print(f'{__name__}: por abrir interfaz')
    root.start_gui()
    print(f'{__name__}: interfaz cerrada')

# comento por comodidad al probar
#    ad.tss('Hasta luego!')

    mc.main_alive = False
    # margen de tiempo para que mueran threads
    sleep(1)
