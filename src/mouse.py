import pyautogui as ag
import math as mt
from time import sleep
import myConfig as mc
import gui

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
    sleep(1)
    
    while mc.gui_alive:
        if mc.tecla:
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
            mc.color_flag = True


            sleep(0.05)
    print(f'{__name__}: murio la gui')
