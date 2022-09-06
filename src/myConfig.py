# variables globales para sincronizacion
from PIL import ImageTk, Image
tecla = bool(False)  # simula entrada activo alto
myTecla = int(0)  # esto no iria, de esto se encarga el hw casco

# al presionar la tecla de exit, el cliente envia por socket, y el
# modulo server recibe la senal, pone en False este flag por lo que el mouse muere
# y luego el server mata la GUI con su handler.
main_alive = True
gui_alive = False
mouse_alive = False
socket_alive = False
in_window = 'None'
color_flag = bool(True)


# variables globales para setup
# sockets
port = 8000

# los valores indicados aca son los iniciales
# interfaz grafica
velocidad_barrido = 1000  # ms
# movimiento del mouse
velocidad_puntero = 20

# teclado - envio de senales
action_key = 'esc'
exit_key = 'shift'
no_key_cod = 0
action_code = 1
exit_code = 2

# modos de uso
# 0 = simple
# 1 = avansado
use_advanced_mod = 1

# tamanos imagenes
size_diagonal = (67, 67)
size_vertical = (80, 80)
size_click = (25, 45)
size_rueda = (20, 33)
size_salir = (40, 40)
size_pausa = (40, 40)
size_settings = (100, 100)
size_modo = (120, 100)

# Imagenes - Recursos
img_ul = img_u = img_ur = img_l = img_r = img_dl = img_d = img_dr = img_ci = img_cd = img_wu = img_wd = img_pausa = img_salir = None
def cargar_fotos():
    global img_ul, img_u, img_ur, img_l, img_r, img_dl, img_d, img_dr, img_ci, img_cd, img_wu, img_wd, img_pausa, img_salir, img_simple, img_avanzado, img_settings
    img_ul = {"black": ImageTk.PhotoImage(Image.open("../recursos/up_left_arrow_b.png").resize(size_diagonal)), "red": ImageTk.PhotoImage(Image.open("../recursos/up_left_arrow_r.png").resize(size_diagonal))}
    img_u = {"black": ImageTk.PhotoImage(Image.open("../recursos/up_arrow_b.png").resize(size_vertical)), "red": ImageTk.PhotoImage(Image.open("../recursos/up_arrow_r.png").resize(size_vertical))}
    img_ur = {"black": ImageTk.PhotoImage(Image.open("../recursos/up_right_arrow_b.png").resize(size_diagonal)), "red": ImageTk.PhotoImage(Image.open("../recursos/up_right_arrow_r.png").resize(size_diagonal))}
    img_l = {"black": ImageTk.PhotoImage(Image.open("../recursos/left_arrow_b.png").resize(size_vertical)), "red": ImageTk.PhotoImage(Image.open("../recursos/left_arrow_r.png").resize(size_vertical))}
    img_r = {"black": ImageTk.PhotoImage(Image.open("../recursos/right_arrow_b.png").resize(size_vertical)), "red": ImageTk.PhotoImage(Image.open("../recursos/right_arrow_r.png").resize(size_vertical))}
    img_dl = {"black": ImageTk.PhotoImage(Image.open("../recursos/down_left_arrow_b.png").resize(size_diagonal)), "red": ImageTk.PhotoImage(Image.open("../recursos/down_left_arrow_r.png").resize(size_diagonal))}
    img_d = {"black": ImageTk.PhotoImage(Image.open("../recursos/down_arrow_b.png").resize(size_vertical)), "red": ImageTk.PhotoImage(Image.open("../recursos/down_arrow_r.png").resize(size_vertical))}
    img_dr = {"black": ImageTk.PhotoImage(Image.open("../recursos/down_right_arrow_b.png").resize(size_diagonal)), "red": ImageTk.PhotoImage(Image.open("../recursos/down_right_arrow_r.png").resize(size_diagonal))}
    img_ci = {"black": ImageTk.PhotoImage(Image.open("../recursos/click_b.png").resize(size_click)), "red": ImageTk.PhotoImage(Image.open("../recursos/click_r.png").resize(size_click))}
    img_cd = {"black": ImageTk.PhotoImage(Image.open("../recursos/click_b.png").resize(size_click)), "red": ImageTk.PhotoImage(Image.open("../recursos/click_r.png").resize(size_click))}
    img_wu = {"black": ImageTk.PhotoImage(Image.open("../recursos/click_b.png").resize(size_rueda)), "red": ImageTk.PhotoImage(Image.open("../recursos/click_r.png").resize(size_rueda))}
    img_wd = {"black": ImageTk.PhotoImage(Image.open("../recursos/click_b.png").resize(size_rueda)), "red": ImageTk.PhotoImage(Image.open("../recursos/click_r.png").resize(size_rueda))}
    img_pausa = {"black": ImageTk.PhotoImage(Image.open("../recursos/pausa_b.png").resize(size_pausa)), "red": ImageTk.PhotoImage(Image.open("../recursos/pausa_r.png").resize(size_pausa))}
    img_salir = {"black": ImageTk.PhotoImage(Image.open("../recursos/salir_b.png").resize(size_salir)), "red": ImageTk.PhotoImage(Image.open("../recursos/salir_r.png").resize(size_salir))}
