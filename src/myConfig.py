###################### variables globales para sincronizacion
tecla = bool(False) # simula entrada activo alto
myTecla = int(0) # esto no iria, de esto se encarga el hw casco

# al presionar la tecla de exit, el cliente envia por socket, y el
# modulo server recibe la senal, pone en False este flag por lo que el mouse muere
# y luego el server mata la GUI con su handler. 
gui_alive = False
in_window = 'None'
main_alive = True
color_flag = bool(True)


##################### variables globales para setup
# sockets
port = 8101

#interfaz grafica
velocidad_barrido = 1000 #ms

#movimiento del mouse
velocidad_puntero = 20

# teclado - envio de senales
action_key = 'esc'
exit_key = 'shift'
no_key_cod = 0
action_code = 1
exit_code = 2

#modos de uso
    # 0 = avanzado
    # 1 = simple
use_mod = 0

# tamanos imagenes
size_diagonal = (67, 67)
size_vertical = (80, 80)
size_click = (25, 45)
size_rueda = (20, 33)
size_salir = (66, 40)