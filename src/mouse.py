import pyautogui as ag
import math as mt
from time import sleep
import myConfig as mc
import gui

# ag tiene una funcion que tira un error si ag mueve el mouse a una
# esquina del monitor, la desactivo. Verificar que el main incluya todo "mouse.py"
# para que se corra esta linea
ag.FAILSAFE = False

def mv_mouse(coord:list):
    while mc.tecla:
        ag.move(coord)

def sc_mouse(cant:int):
    while mc.tecla:
        ag.scroll(clicks=cant)

def mouse(x:gui.Gui):

    val = mc.velocidad_puntero
    # para que la velocidad de movimiento no cambie al mover en diagonal
    # hago que el modulo del vector movimiento en diagonal sea igual a
    # cuando el movimiento es horizontal o vertical
    raiz_val = int(mt.sqrt(2*(val**2)))

    # como trabajamos con threads, al no hacer el sleep() para dar un margen de
    # tiempo de inicializacion de los otros threads, esta funcion trata de usar
    # la 'x' antes de que esta tenga algo cargado. Debemos dar tiempo al thread
    # principal de generar la ventana si no, me tira que 'x' es 'None'.
    while( mc.gui_alive == False):
        pass
    sleep(0.5)
    

    # las lineas que dicen "mc.tecla = False" es porque por ejemplo, cerraba una ventana con exit, pero
    # al volver al main, si sigo por unos isntantes presionando el boton, se volvia a abrir
    while mc.gui_alive:
        if mc.tecla:
            if mc.in_window == 'main':
                if x.btn_config.cget('background') == 'red':
                    mc.tecla = False
                    x.open_config()
                elif x.btn_use_avanzado.cget('background') == 'red':
                    mc.tecla = False
                    mc.use_mod = 0
                    x.open_use()
                elif x.btn_use_simple.cget('background') == 'red':
                    mc.tecla = False
                    mc.use_mod = 1
                    x.open_use()

            elif mc.in_window == 'config':
                mc.tecla = False
                if x.wd_config.btn_5.cget('background') == 'red':
                    x.wd_config.label_velocidad_puntero['text'] = f'Velocidad puntero: {5}'
                    mc.velocidad_puntero = 5
                elif x.wd_config.btn_10.cget('background') == 'red':
                    x.wd_config.label_velocidad_puntero['text'] = f'Velocidad puntero: {10}'
                    mc.velocidad_puntero = 10
                elif x.wd_config.btn_15.cget('background') == 'red':
                    x.wd_config.label_velocidad_puntero['text'] = f'Velocidad puntero: {15}'
                    mc.velocidad_puntero = 15
                elif x.wd_config.btn_20.cget('background') == 'red':
                    x.wd_config.label_velocidad_puntero['text'] = f'Velocidad puntero: {20}'
                    mc.velocidad_puntero = 20
                elif x.wd_config.btn_750.cget('background') == 'red':
                    x.wd_config.label_velocidad_barrido['text'] = f'Velocidad barrido [ms]: {750}'
                    mc.velocidad_barrido = 750
                elif x.wd_config.btn_1000.cget('background') == 'red':
                    x.wd_config.label_velocidad_barrido['text'] = f'Velocidad barrido [ms]: {1000}'
                    mc.velocidad_barrido = 1000
                elif x.wd_config.btn_1500.cget('background') == 'red':
                    x.wd_config.label_velocidad_barrido['text'] = f'Velocidad barrido [ms]: {1500}'
                    mc.velocidad_barrido = 1500
                elif x.wd_config.btn_2000.cget('background') == 'red':
                    x.wd_config.label_velocidad_barrido['text'] = f'Velocidad barrido [ms]: {2000}'
                    mc.velocidad_barrido = 2000
                elif x.wd_config.btn_ok.cget('background') == 'red':
                    x.config_on_closing()
           
            elif mc.in_window == 'use':
                mc.color_flag = False
                if x.wd_use.wd.idx['ul'] == 'r':
                    mv_mouse([-raiz_val, -raiz_val])
                elif x.wd_use.wd.idx['u'] == 'r':
                    mv_mouse([0, -val])
                elif x.wd_use.wd.idx['ur'] == 'r':
                    mv_mouse([raiz_val, -raiz_val])
                elif x.wd_use.wd.idx['l'] == 'r':
                    mv_mouse([-val, 0])
                elif x.wd_use.wd.idx['r'] == 'r':
                    mv_mouse([val, 0])
                elif x.wd_use.wd.idx['dl'] == 'r':
                    mv_mouse([-raiz_val, raiz_val])
                elif x.wd_use.wd.idx['d'] == 'r':
                    mv_mouse([0, val])
                elif x.wd_use.wd.idx['dr'] == 'r':
                    mv_mouse([raiz_val, raiz_val])
                elif x.wd_use.wd.idx['ci'] == 'r':
                    if mc.tecla:
                        ag.click(button=ag.LEFT)
                elif x.wd_use.wd.idx['cd'] == 'r':
                    if mc.tecla:
                        ag.click(button=ag.RIGHT)
                elif x.wd_use.wd.idx['wu'] == 'r':
                    sc_mouse(10)
                elif x.wd_use.wd.idx['wd'] == 'r':
                    sc_mouse(-10)
                elif x.wd_use.wd.idx['salir'] == 'r':
                    mc.tecla = False
                    x.use_on_closing()
                mc.color_flag = True

                sleep(0.05)
    print(f'{__name__}: murio la gui')
