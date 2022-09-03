import pyautogui as ag
import math as mt
from time import sleep
import myConfig as mc
import gui

# ag tiene una funcion que tira un error si ag mueve el mouse a una
# esquina del monitor, la desactivo. Verificar que el main incluya todo "mouse.py"
# para que se corra esta linea
ag.FAILSAFE = False


class Mouse():

    val = mc.velocidad_puntero
    # para que la velocidad de movimiento no cambie al mover en diagonal
    # hago que el modulo del vector movimiento en diagonal sea igual a
    # cuando el movimiento es horizontal o vertical
    raiz_val = int(mt.sqrt(2*(val**2)))

    def __init__(self) -> None:
        pass

    def actualizar_velocidad(self):
        self.val = mc.velocidad_puntero
        self.raiz_val = int(mt.sqrt(2*(self.val**2)))

    def mv_mouse(self, coord: list):
        while mc.tecla:
            ag.move(coord)

    def sc_mouse(self, cant: int):
        while mc.tecla:
            ag.scroll(clicks=cant)

    def mouse(self, x: gui.Gui):
        # como trabajamos con threads, al no hacer el sleep() para dar un margen de
        # tiempo de inicializacion de los otros threads, esta funcion trata de usar
        # la 'x' antes de que esta tenga algo cargado. Debemos dar tiempo al thread
        # principal de generar la ventana si no, me tira que 'x' es 'None'.
        while(mc.gui_alive == False):
            pass
        sleep(0.5)
        # ver si esto va aca o en la funcion mouse

        # las lineas que dicen "mc.tecla = False" es porque por ejemplo, cerraba una ventana con exit, pero
        # al volver al main, si sigo por unos isntantes presionando el boton, se volvia a abrir
        while mc.gui_alive:
            if mc.tecla:
                if mc.in_window == 'main':
                    if x.idx['settings'] == 'r':
                        mc.tecla = False
                        x.open_config()
                    elif x.idx['simple'] == 'r':
                        mc.tecla = False
                        mc.use_advanced_mod = 0
                        x.open_use()
                    elif x.idx['avanzado'] == 'r':
                        mc.tecla = False
                        mc.use_advanced_mod = 1
                        x.open_use()

                elif mc.in_window == 'config':
                    mc.tecla = False
                    # los valores divididos por 5 es para que visualmente hayan 4 velocidades
                    if x.wd_config.btn_5.cget('background') == 'red':
                        x.wd_config.label_velocidad_puntero['text'] = f'Velocidad puntero: {5/5}'
                        mc.velocidad_puntero = 5
                    elif x.wd_config.btn_10.cget('background') == 'red':
                        x.wd_config.label_velocidad_puntero['text'] = f'Velocidad puntero: {10/5}'
                        mc.velocidad_puntero = 10
                    elif x.wd_config.btn_15.cget('background') == 'red':
                        x.wd_config.label_velocidad_puntero['text'] = f'Velocidad puntero: {15/5}'
                        mc.velocidad_puntero = 15
                    elif x.wd_config.btn_20.cget('background') == 'red':
                        x.wd_config.label_velocidad_puntero['text'] = f'Velocidad puntero: {20/5}'
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
                    elif x.wd_config.btn_aplicar.cget('background') == 'red':
                        self.actualizar_velocidad()
                        x.config_on_closing()

                elif mc.in_window == 'use':
                    if x.wd_use.wd.idx['pausa'] == 'r':
                        mc.tecla = False  # para que no entre en este if por el tiempo que tarda en soltar la tecla
                        if mc.color_flag:
                            mc.color_flag = False
                        else:
                            mc.color_flag = True
                    else:
                        mc.color_flag = False
                        if x.wd_use.wd.idx['ul'] == 'r':
                            self.mv_mouse([-self.raiz_val, -self.raiz_val])
                        elif x.wd_use.wd.idx['u'] == 'r':
                            self.mv_mouse([0, -self.val])
                        elif x.wd_use.wd.idx['ur'] == 'r':
                            self.mv_mouse([self.raiz_val, -self.raiz_val])
                        elif x.wd_use.wd.idx['l'] == 'r':
                            self.mv_mouse([-self.val, 0])
                        elif x.wd_use.wd.idx['r'] == 'r':
                            self.mv_mouse([self.val, 0])
                        elif x.wd_use.wd.idx['dl'] == 'r':
                            self.mv_mouse([-self.raiz_val, self.raiz_val])
                        elif x.wd_use.wd.idx['d'] == 'r':
                            self.mv_mouse([0, self.val])
                        elif x.wd_use.wd.idx['dr'] == 'r':
                            self.mv_mouse([self.raiz_val, self.raiz_val])
                        elif x.wd_use.wd.idx['ci'] == 'r':
                            if mc.tecla:  # para que estane stos if? esta condicion ya esta chequeada
                                ag.click(button=ag.LEFT)
                        elif x.wd_use.wd.idx['cd'] == 'r':
                            if mc.tecla:
                                ag.click(button=ag.RIGHT)
                        elif x.wd_use.wd.idx['wu'] == 'r':
                            self.sc_mouse(10)
                        elif x.wd_use.wd.idx['wd'] == 'r':
                            self.sc_mouse(-10)
                        elif x.wd_use.wd.idx['salir'] == 'r':
                            mc.tecla = False
                            x.use_on_closing()
                        mc.color_flag = True

                        sleep(0.05)
        print(f'{__name__}: murio la gui')
