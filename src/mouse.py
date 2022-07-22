import pyautogui as ag
import math as mt
from time import sleep
import myConfig as mc
import gui

def mv_mouse(x:gui.Gui, coord:list):
    x.wd.color_flag = False
    while mc.tecla:
        ag.move(coord)
    x.wd.color_flag = True

def sc_mouse(x:gui.Gui, cant:int):
    x.wd.color_flag = False
    while mc.tecla:
        ag.scroll(clicks=cant)
    x.wd.color_flag = True

def mouse(x:gui.Gui):

    val = mc.velocidad_puntero
    # para que la velocidad de movimiento no cambie al mover en diagonal
    # hago que el modulo del vector movimiento en diagonal sea igual a
    # cuando el movimiento es horizontal o vertical
    raiz_val = int(mt.sqrt(2*(val**2)))

    # como trabajamos con threads, al no hacer el sleep() para dar un margen de
    # tiempo de inicializacion de los otros threads, esta funcion trata de usar
    # la 'x' antes de que esta tenga algo cargado. Debemos dar tiempo al thread
    # principal de generar la ventana si no, me tira que 'x' es 'None'
    sleep(2)
    
    while mc.gui_alive:
        if mc.tecla:
            if x.wd.idx['ul'] == 'r':
                mv_mouse(x, [-raiz_val, -raiz_val])
            elif x.wd.idx['u'] == 'r':
                mv_mouse(x, [0, -val])
            elif x.wd.idx['ur'] == 'r':
                mv_mouse(x, [raiz_val, -raiz_val])
            elif x.wd.idx['l'] == 'r':
                mv_mouse(x, [-val, 0])
            elif x.wd.idx['r'] == 'r':
                mv_mouse(x, [val, 0])
            elif x.wd.idx['dl'] == 'r':
                mv_mouse(x, [-raiz_val, raiz_val])
            elif x.wd.idx['d'] == 'r':
                mv_mouse(x, [0, val])
            elif x.wd.idx['dr'] == 'r':
                mv_mouse(x, [raiz_val, raiz_val])
            elif x.wd.idx['ci'] == 'r':
                if mc.tecla:
                    ag.click(button=ag.LEFT)
            elif x.wd.idx['cd'] == 'r':
                if mc.tecla:
                    ag.click(button=ag.RIGHT)
            elif x.wd.idx['wu'] == 'r':
                sc_mouse(x, 10)
            elif x.wd.idx['wd'] == 'r':
                sc_mouse(x, -10)


            sleep(0.05)
    print(f'{__name__}: murio la gui')

############################## OLD
#            if x.wd.lb_N.cget('background') == 'pink': # color modificable
#                mv_mouse(x, [0, -val])
#            elif x.wd.lb_S.cget('background') == 'pink':
#                mv_mouse(x, [0, val])
#            elif x.wd.lb_E.cget('background') == 'pink':
#                mv_mouse(x, [val, 0])
#            elif x.wd.lb_O.cget('background') == 'pink':
#                mv_mouse(x, [-val, 0])
#            elif x.wd.lb_NE.cget('background') == 'pink':
#                mv_mouse(x, [raiz_val, -raiz_val])
#            elif x.wd.lb_NO.cget('background') == 'pink':
#                mv_mouse(x, [-raiz_val, -raiz_val])
#            elif x.wd.lb_SE.cget('background') == 'pink':
#                mv_mouse(x, [raiz_val, raiz_val])
#            elif x.wd.lb_SO.cget('background') == 'pink':
#                mv_mouse(x, [-raiz_val, raiz_val])

#            elif x.wd.lb_CI.cget('background') == 'pink':
#                if mc.tecla:
#                    ag.click(button=ag.LEFT)
#            elif x.wd.lb_CD.cget('background') == 'pink':
#                if mc.tecla:
#                    ag.click(button=ag.RIGHT)

#            elif x.wd.lb_rueda_N.cget('background') == 'pink':
#                sc_mouse(x, 10)
#            elif x.wd.lb_rueda_S.cget('background') == 'pink':
#                sc_mouse(x, -10)
#            elif x.wd.lb_rueda_C.cget('background') == 'pink':
#                if mc.tecla:
#                    ag.click(ag.MIDDLE)