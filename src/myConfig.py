###################### variables globales para sincronizacion
tecla = bool(False) # simula entrada activo alto
myTecla = int(0) # esto no iria, de esto se encarga el hw casco

# al presionar la tecla de exit, el cliente envia por socket, y el
# modulo server recibe la senal, pone en False este flag por lo que el mouse muere
# y luego el server mata la GUI con su handler. 
gui_alive = False



##################### variables globales para setup
# sockets
port = 8000

#interfaz grafica
velocidad_barrido = 1000 #ms

#movimiento del mouse
velocidad_puntero = 20

# teclado - envio de senales
action_key = 'esc'
exit_key = 'shift'