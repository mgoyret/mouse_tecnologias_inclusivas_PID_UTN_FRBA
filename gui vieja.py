from cgitb import text
from pickle import HIGHEST_PROTOCOL
from time import sleep
import tkinter as tk
from tkinter import ttk
from tkinter import font
import myConfig as mc
from PIL import ImageTk, Image
from functools import partial

# se define la clase de la ventana principal, con un frame dentro
# con los labes deseados

# tamanos de las imagenes
size_diagonal = (100, 100)
size_vertical = (120, 120)
size_click = (40, 70)
size_rueda = (30, 50)
size_exit = (50, 30)


class Window_use(tk.Frame):

    idx = list()
    # cada 50ms trae la app al frente
    def on_top(self):
        self.lift()
        self.after(50, self.on_top)

    def __init__(self, parent):
        tk.Frame.__init__(self, parent, bg='pink')
        self.coords_clicks_Labels = tk.LabelFrame(self)  # , text='Direcciones'
        self.coords_clicks_Labels.grid(row=0, column=0)
        # mod=avanzado --> mod=0
        if not mc.use_mod:
            print('DEBUG 1')
            self.img_ul = {"black": ImageTk.PhotoImage(Image.open("../recursos/up_left_arrow_b.png").resize(
                size_diagonal)), "red": ImageTk.PhotoImage(Image.open("../recursos/up_left_arrow_r.png").resize(size_diagonal))}
            self.lbl_ul = tk.Label(self.coords_clicks_Labels,
                                image=self.img_ul["black"])
            self.lbl_ul.grid(row=0, column=0, padx=2, pady=2, sticky='nesw')

        print('DEBUG 2')
        self.img_u = {"black": ImageTk.PhotoImage(Image.open("../recursos/up_arrow_b.png").resize(
            size_vertical)), "red": ImageTk.PhotoImage(Image.open("../recursos/up_arrow_r.png").resize(size_vertical))}
        self.lbl_u = tk.Label(self.coords_clicks_Labels,
                              image=self.img_u["black"])
        self.lbl_u.grid(row=0, column=1, padx=2, pady=2, sticky='nesw')

        if not mc.use_mod:
            print('DEBUG 3')
            self.img_ur = {"black": ImageTk.PhotoImage(Image.open("../recursos/up_right_arrow_b.png").resize(
                size_diagonal)), "red": ImageTk.PhotoImage(Image.open("../recursos/up_right_arrow_r.png").resize(size_diagonal))}
            self.lbl_ur = tk.Label(self.coords_clicks_Labels,
                                image=self.img_ur["black"])
            self.lbl_ur.grid(row=0, column=2, padx=2, pady=2, sticky='nesw')

        print('DEBUG 4')
        self.img_l = {"black": ImageTk.PhotoImage(Image.open("../recursos/left_arrow_b.png").resize(
            size_vertical)), "red": ImageTk.PhotoImage(Image.open("../recursos/left_arrow_r.png").resize(size_vertical))}
        self.lbl_l = tk.Label(self.coords_clicks_Labels,
                              image=self.img_l["black"])
        self.lbl_l.grid(row=1, column=0, padx=2, pady=2, sticky='nesw')

        print('DEBUG 5')
        self.img_r = {"black": ImageTk.PhotoImage(Image.open("../recursos/right_arrow_b.png").resize(
            size_vertical)), "red": ImageTk.PhotoImage(Image.open("../recursos/right_arrow_r.png").resize(size_vertical))}
        self.lbl_r = tk.Label(self.coords_clicks_Labels,
                              image=self.img_r["black"])
        self.lbl_r.grid(row=1, column=2, padx=2, pady=2, sticky='nesw')

        if not mc.use_mod:
            print('DEBUG 6')
            self.img_dl = {"black": ImageTk.PhotoImage(Image.open("../recursos/down_left_arrow_b.png").resize(
                size_diagonal)), "red": ImageTk.PhotoImage(Image.open("../recursos/down_left_arrow_r.png").resize(size_diagonal))}
            self.lbl_dl = tk.Label(self.coords_clicks_Labels,
                                image=self.img_dl["black"])
            self.lbl_dl.grid(row=2, column=0, padx=2, pady=2, sticky='nesw')

        print('DEBUG 7')
        self.img_d = {"black": ImageTk.PhotoImage(Image.open("../recursos/down_arrow_b.png").resize(
            size_vertical)), "red": ImageTk.PhotoImage(Image.open("../recursos/down_arrow_r.png").resize(size_vertical))}
        self.lbl_d = tk.Label(self.coords_clicks_Labels,
                              image=self.img_d["black"])
        self.lbl_d.grid(row=2, column=1, padx=2, pady=2, sticky='nesw')

        if not mc.use_mod:
            print('DEBUG 8')
            self.img_dr = {"black": ImageTk.PhotoImage(Image.open("../recursos/down_right_arrow_b.png").resize(
                size_diagonal)), "red": ImageTk.PhotoImage(Image.open("../recursos/down_right_arrow_r.png").resize(size_diagonal))}
            self.lbl_dr = tk.Label(self.coords_clicks_Labels,
                                image=self.img_dr["black"])
            self.lbl_dr.grid(row=2, column=2, padx=2, pady=2, sticky='nesw')

        self.clickLabels = tk.LabelFrame(
            self.coords_clicks_Labels)  # , text='clicks'
        self.clickLabels.grid(row=1, column=1, padx=2, pady=2)

        print('DEBUG 9')
        self.img_ci = {"black": ImageTk.PhotoImage(Image.open(
            "../recursos/click_b.png").resize(size_click)), "red": ImageTk.PhotoImage(Image.open("../recursos/click_r.png").resize(size_click))}
        self.lbl_ci = tk.Label(self.clickLabels, image=self.img_ci['black'])
        self.lbl_ci.grid(row=0, column=0, padx=2, pady=2, sticky='nesw')

        print('DEBUG 10')
        self.img_cd = {"black": ImageTk.PhotoImage(Image.open(
            "../recursos/click_b.png").resize(size_click)), "red": ImageTk.PhotoImage(Image.open("../recursos/click_r.png").resize(size_click))}
        self.lbl_cd = tk.Label(self.clickLabels, image=self.img_cd['black'])
        self.lbl_cd.grid(row=0, column=1, padx=2, pady=2, sticky='nesw')

        self.packLabels = tk.LabelFrame(self)
        self.packLabels.grid(row=0, column=1)

        self.ruedaLabels = tk.LabelFrame(self.packLabels, text='Rueda')
        self.ruedaLabels.grid(row=1, column=0)

        print('DEBUG 11')
        self.img_wu = {"black": ImageTk.PhotoImage(Image.open(
            "../recursos/click_b.png").resize(size_rueda)), "red": ImageTk.PhotoImage(Image.open("../recursos/click_r.png").resize(size_rueda))}
        self.lbl_wu = tk.Label(self.ruedaLabels, image=self.img_wu['black'])
        self.lbl_wu.grid(row=0, column=3, padx=2, pady=2, sticky='nesw')

        print('DEBUG 12')
        self.img_wd = {"black": ImageTk.PhotoImage(Image.open(
            "../recursos/click_b.png").resize(size_rueda)), "red": ImageTk.PhotoImage(Image.open("../recursos/click_r.png").resize(size_rueda))}
        self.lbl_wd = tk.Label(self.ruedaLabels, image=self.img_wd['black'])
        self.lbl_wd.grid(row=2, column=3, padx=2, pady=2, sticky='nesw')

        self.img_exit = {"black": ImageTk.PhotoImage(Image.open(
            "../recursos/click_b.png").resize(size_exit)), "red": ImageTk.PhotoImage(Image.open("../recursos/click_r.png").resize(size_exit))}
        self.lbl_exit = tk.Label(self, image=self.img_exit['red'], text='exit', borderwidth=0, highlightthickness=0)
        self.lbl_exit.grid(row=1, column=0, padx=2, pady=2, sticky='nesw')

        self.idx = {
            "ul":   "b",
            "u":    "b",
            "ur":   "b",
            "l":    "b",
            "r":    "b",
            "dl":   "b",
            "d":    "b",
            "dr":   "b",
            'ci':   'b',
            'cd':   'b',
            'wu':   'b',
            'wd':   'b',
            'exit': 'r'
        }

        self.color()
        self.on_top() #CHEQUEAR SI ESTO FUNCAAAAA!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

    # en la funcion color no hace fata verificar el modo. Ver los "if i == 'ul':". Si estamos
    # en modo simple, directamente nunca se dara que 'i' sea igual a una diagonal
    def color(self):
        if mc.color_flag:
            for i in self.idx:
                if self.idx[i] == 'r':
                    if i == 'ul':
                        self.lbl_ul = tk.Label(self.coords_clicks_Labels, image=self.img_ul["black"])
                        self.lbl_ul.grid(row=0, column=0, padx=2, pady=2, sticky='nesw')
                        self.lbl_u = tk.Label(self.coords_clicks_Labels, image=self.img_u["red"])
                        self.lbl_u.grid(row=0, column=1, padx=2,pady=2, sticky='nesw')
                        self.idx['u'] = 'r'

                    elif i == 'u':
                        self.lbl_u = tk.Label(
                            self.coords_clicks_Labels, image=self.img_u["black"])
                        self.lbl_u.grid(row=0, column=1, padx=2,pady=2, sticky='nesw')
                        if not mc.use_mod:
                            self.lbl_ur = tk.Label(self.coords_clicks_Labels, image=self.img_ur["red"])
                            self.lbl_ur.grid(row=0, column=2, padx=2, pady=2, sticky='nesw')
                            self.idx['ur'] = 'r'
                        else:
                            self.lbl_l = tk.Label(self.coords_clicks_Labels, image=self.img_l["red"])
                            self.lbl_l.grid(row=1, column=0, padx=2,pady=2, sticky='nesw')
                            self.idx['l'] = 'r'

                    elif i == 'ur':
                        self.lbl_ur = tk.Label(self.coords_clicks_Labels, image=self.img_ur["black"])
                        self.lbl_ur.grid(row=0, column=2, padx=2, pady=2, sticky='nesw')
                        self.lbl_l = tk.Label(self.coords_clicks_Labels, image=self.img_l["red"])
                        self.lbl_l.grid(row=1, column=0, padx=2,pady=2, sticky='nesw')
                        self.idx['l'] = 'r'

                    elif i == 'l':
                        self.lbl_l = tk.Label(self.coords_clicks_Labels, image=self.img_l["black"])
                        self.lbl_l.grid(row=1, column=0, padx=2,pady=2, sticky='nesw')
                        self.lbl_r = tk.Label(self.coords_clicks_Labels, image=self.img_r["red"])
                        self.lbl_r.grid(row=1, column=2, padx=2,pady=2, sticky='nesw')
                        self.idx['r'] = 'r'

                    elif i == 'r':
                        self.lbl_r = tk.Label(self.coords_clicks_Labels, image=self.img_r["black"])
                        self.lbl_r.grid(row=1, column=2, padx=2,pady=2, sticky='nesw')
                        if not mc.use_mod:
                            self.lbl_dl = tk.Label(self.coords_clicks_Labels, image=self.img_dl["red"])
                            self.lbl_dl.grid(row=2, column=0, padx=2, pady=2, sticky='nesw')
                            self.idx['dl'] = 'r'
                        else:
                            self.lbl_d = tk.Label(self.coords_clicks_Labels, image=self.img_d["red"])
                            self.lbl_d.grid(row=2, column=1, padx=2,pady=2, sticky='nesw')
                            self.idx['d'] = 'r'

                    elif i == 'dl':
                        self.lbl_dl = tk.Label(self.coords_clicks_Labels, image=self.img_dl["black"])
                        self.lbl_dl.grid(row=2, column=0, padx=2, pady=2, sticky='nesw')
                        self.lbl_d = tk.Label(self.coords_clicks_Labels, image=self.img_d["red"])
                        self.lbl_d.grid(row=2, column=1, padx=2,pady=2, sticky='nesw')
                        self.idx['d'] = 'r'

                    elif i == 'd':
                        self.lbl_d = tk.Label(self.coords_clicks_Labels, image=self.img_d["black"])
                        self.lbl_d.grid(row=2, column=1, padx=2,pady=2, sticky='nesw')
                        if not mc.use_mod:
                            self.lbl_dr = tk.Label(self.coords_clicks_Labels, image=self.img_dr["red"])
                            self.lbl_dr.grid(row=2, column=2, padx=2, pady=2, sticky='nesw')
                            self.idx['dr'] = 'r'
                        else:
                            self.lbl_ci = tk.Label(self.clickLabels, image=self.img_ci["red"])
                            self.lbl_ci.grid(row=0, column=0, padx=2, pady=2, sticky='nesw')
                            self.idx['ci'] = 'r'

                    elif i == 'dr':
                        self.lbl_dr = tk.Label(self.coords_clicks_Labels, image=self.img_dr["black"])
                        self.lbl_dr.grid(row=2, column=2, padx=2, pady=2, sticky='nesw')
                        self.lbl_ci = tk.Label(self.clickLabels, image=self.img_ci["red"])
                        self.lbl_ci.grid(row=0, column=0, padx=2, pady=2, sticky='nesw')
                        self.idx['ci'] = 'r'

                    elif i == 'ci':
                        self.lbl_ci = tk.Label(
                            self.clickLabels, image=self.img_ci['black'])
                        self.lbl_ci.grid(
                            row=0, column=0, padx=2, pady=2, sticky='nesw')
                        self.lbl_cd = tk.Label(
                            self.clickLabels, image=self.img_cd['red'])
                        self.lbl_cd.grid(
                            row=0, column=1, padx=2, pady=2, sticky='nesw')
                        self.idx['cd'] = 'r'

                    elif i == 'cd':
                        self.lbl_cd = tk.Label(
                            self.clickLabels, image=self.img_cd['black'])
                        self.lbl_cd.grid(
                            row=0, column=1, padx=2, pady=2, sticky='nesw')
                        self.lbl_wu = tk.Label(
                            self.ruedaLabels, image=self.img_wu['red'])
                        self.lbl_wu.grid(
                            row=0, column=3, padx=2, pady=2, sticky='nesw')
                        self.idx['wu'] = 'r'

                    elif i == 'wu':
                        self.lbl_wu = tk.Label(
                            self.ruedaLabels, image=self.img_wu['black'])
                        self.lbl_wu.grid(
                            row=0, column=3, padx=2, pady=2, sticky='nesw')
                        self.lbl_wd = tk.Label(
                            self.ruedaLabels, image=self.img_wd['red'])
                        self.lbl_wd.grid(
                            row=2, column=3, padx=2, pady=2, sticky='nesw')
                        self.idx['wd'] = 'r'

                    elif i == 'wd':
                        self.lbl_wd = tk.Label(
                            self.ruedaLabels, image=self.img_wd['black'])
                        self.lbl_wd.grid(
                            row=2, column=3, padx=2, pady=2, sticky='nesw')
                        self.lbl_exit = tk.Label(
                            self, image=self.img_exit['red'])
                        self.lbl_exit.grid(
                            row=1, column=0, padx=2, pady=2, sticky='nesw')
                        self.idx['exit'] = 'r'

                    elif i == 'exit':
                        self.lbl_exit = tk.Label(self, image=self.img_exit['black'])
                        self.lbl_exit.grid(row=1, column=0, padx=2, pady=2, sticky='nesw')
                        if not mc.use_mod:
                            self.lbl_ul = tk.Label(self.coords_clicks_Labels, image=self.img_ul['red'])
                            self.lbl_ul.grid(row=0, column=0, padx=2, pady=2, sticky='nesw')
                            self.idx['ul'] = 'r'
                        else:
                            self.lbl_u = tk.Label(self.coords_clicks_Labels, image=self.img_u["red"])
                            self.lbl_u.grid(row=0, column=1, padx=2,pady=2, sticky='nesw')
                            self.idx['u'] = 'r'

                    self.idx[i] = 'b'
                    break
        self.after(mc.velocidad_barrido, self.color)


class Gui(tk.Tk):

    # defino esta variable para que sea miembro y luego
    # igualarla a la ventana principal de la gui
    wd_use = None
    wd_config = None

    def finish_gui(self):
        mc.gui_alive = False
        # damos tiempo a que muera "mouse" que usa la gui
        sleep(0.5)
        self.destroy()

    # cada 50ms trae la app al frente
    def on_top(self):
        self.lift()
        self.after(50, self.on_top)

    def __init__(self):
        tk.Tk.__init__(self)
        self.title("Ventana Principal")
        self.geometry("300x300")
        self.resizable(False, False)
        self.configure(background='#F2B33D')
        self.protocol("WM_DELETE_WINDOW", self.finish_gui)
        self.eval('tk::PlaceWindow . center')
        # ICONO
        self.img_icon = ImageTk.PhotoImage(Image.open("../recursos/logo.jpg"))
        self.tk.call('wm', 'iconphoto', self._w, self.img_icon)




        self.btn_config = tk.Button(self, text='configuracion', command=partial(self.open_config), background='white')  # partial por defecto manda self como argumento
        self.btn_config.pack(padx=20, pady=(20, 10), expand=True, fill='both')

        # frame modos
        self.frame_modos = tk.LabelFrame(self, text='modos de uso', background='white')
        self.frame_modos.pack(padx=20, pady=(10, 20), expand=True, fill='both')
            # modo avanzado
        self.btn_use_avanzado = tk.Button(self.frame_modos, text='avanzado', command=partial(self.open_use), background='white')
        self.btn_use_avanzado.pack(side=tk.LEFT, padx=5, pady=5, expand=True, fill='both')
            # modos simple
        self.btn_use_simple = tk.Button(self.frame_modos, text='simple', command=partial(self.open_use), background='red')
        self.btn_use_simple.pack(side=tk.RIGHT, padx=5, pady=5, expand=True, fill='both')

        mc.in_window = 'main'
        self.idx = [self.btn_config, self.btn_use_avanzado, self.btn_use_simple]
        self.color()

        self.on_top()


    # esta funcion miembro analiza cuando un label tiene color rosa
    # y lo pone el azul, para luego poner el siguiente en rosa
    def color(self):
        for i in range(len(self.idx)):
            if self.idx[i].cget('background') == 'red':
                self.idx[i].configure(bg='white')
                self.idx[(i+1) % len(self.idx)].configure(bg='red')
                break
        self.after(1000, self.color)

    def config_on_closing(self):
        mc.in_window = 'main'    
        self.deiconify()  # muestra nuevamente mainwindow
        self.wd_config.destroy()

    def use_on_closing(self):
        mc.in_window = 'main'
        self.deiconify()  # muestra nuevamente mainwindow
        self.wd_use.destroy()

    def open_config(self):
        self.wd_config = tk.Toplevel(self)
        self.wd_config.title("ventana de configuracion")
        self.wd_config.geometry("%dx%d+%d+%d" %
                                (400, 300, self.winfo_x()-100, self.winfo_y()-0))
        self.wd_config.resizable(False, False)
        self.wd_config.configure(background='pink')
        # ICONO
        self.img_icon = ImageTk.PhotoImage(Image.open("../recursos/logo.jpg"))
        self.wd_config.tk.call('wm', 'iconphoto', self.wd_config._w, self.img_icon)
        self.withdraw()  # esconde mainwindow


        self.wd_config.protocol('WM_DELETE_WINDOW', self.config_on_closing)
        mc.in_window = 'config'

        # velocidad puntero
        self.wd_config.velocidad_puntero = tk.LabelFrame(
            self.wd_config, text='velocidad del puntero', background='white')
        self.wd_config.velocidad_puntero.pack(
            padx=10, pady=(20, 10), expand=True, fill='both')
        # label
        self.wd_config.label_velocidad_puntero = tk.Label(
            self.wd_config.velocidad_puntero, text=f'Velocidad puntero: {mc.velocidad_puntero}', background='white')
        self.wd_config.label_velocidad_puntero.pack(
            side=tk.LEFT, padx=5, pady=5)

        # valores
        self.wd_config.frame_valores_puntero = tk.LabelFrame(self.wd_config.velocidad_puntero, background='white', borderwidth=0, highlightthickness=0)
        self.wd_config.frame_valores_puntero.pack(
            side=tk.RIGHT, padx=50, pady=5)

        self.wd_config.btn_5 = tk.Button(
            self.wd_config.frame_valores_puntero, text='5', background='white')
        self.wd_config.btn_5.grid(
            row=0, column=0, padx=2, pady=2, sticky='nesw')

        self.wd_config.btn_10 = tk.Button(
            self.wd_config.frame_valores_puntero, text='10', background='white')
        self.wd_config.btn_10.grid(
            row=0, column=1, padx=2, pady=2, sticky='nesw')

        self.wd_config.btn_15 = tk.Button(
            self.wd_config.frame_valores_puntero, text='15', background='white')
        self.wd_config.btn_15.grid(
            row=1, column=0, padx=2, pady=2, sticky='nesw')

        self.wd_config.btn_20 = tk.Button(
            self.wd_config.frame_valores_puntero, text='20', background='white')
        self.wd_config.btn_20.grid(
            row=1, column=1, padx=2, pady=2, sticky='nesw')

        # combo
#        self.wd_config.combo_velocidad_puntero = ttk.Combobox(
#            self.wd_config.velocidad_puntero, state='readonly', values=[5, 10, 15, 20], foreground='black')
#        self.wd_config.combo_velocidad_puntero.pack(
#            side=tk.RIGHT, padx=5, pady=5)
#        self.wd_config.combo_velocidad_puntero.set('valor')

        # velocidad barrido
        self.wd_config.velocidad_barrido = tk.LabelFrame(
            self.wd_config, text='velocidad barrido', background='white')
        self.wd_config.velocidad_barrido.pack(
            padx=10, pady=10, expand=True, fill='both')
        # label
        self.wd_config.label_velocidad_barrido = tk.Label(
            self.wd_config.velocidad_barrido, text=f'Velocidad barrido [ms]: {mc.velocidad_barrido}', background='white')
        self.wd_config.label_velocidad_barrido.pack(
            side=tk.LEFT, padx=5, pady=5)

        # valores
        self.wd_config.frame_valores_barrido = tk.LabelFrame(
            self.wd_config.velocidad_barrido, background='white', borderwidth=0, highlightthickness=0)
        self.wd_config.frame_valores_barrido.pack(
            side=tk.RIGHT, padx=50, pady=5)

        self.wd_config.btn_750 = tk.Button(
            self.wd_config.frame_valores_barrido, text='750', background='white')
        self.wd_config.btn_750.grid(
            row=0, column=0, padx=2, pady=2, sticky='nesw')

        self.wd_config.btn_1000 = tk.Button(
            self.wd_config.frame_valores_barrido, text='1000', background='white')
        self.wd_config.btn_1000.grid(
            row=0, column=1, padx=2, pady=2, sticky='nesw')

        self.wd_config.btn_1500 = tk.Button(
            self.wd_config.frame_valores_barrido, text='1500', background='white')
        self.wd_config.btn_1500.grid(
            row=1, column=0, padx=2, pady=2, sticky='nesw')

        self.wd_config.btn_2000 = tk.Button(
            self.wd_config.frame_valores_barrido, text='2000', background='white')
        self.wd_config.btn_2000.grid(
            row=1, column=1, padx=2, pady=2, sticky='nesw')

        # combo
#        self.wd_config.combo_velocidad_barrido = ttk.Combobox(
#            self.wd_config.velocidad_barrido, state='readonly', values=[750, 1000, 1500, 2000], foreground='red')
#        self.wd_config.combo_velocidad_barrido.pack(
#            side=tk.RIGHT, padx=5, pady=5)
#        self.wd_config.combo_velocidad_barrido.set('valor')

        # buttons
        self.wd_config.buttons = tk.LabelFrame(
            self.wd_config, background='pink', borderwidth=0, highlightthickness=0)
        self.wd_config.buttons.pack(padx=50, pady=10, expand=True, fill='y')
        # ok button

#        def set_vals():
#            mc.velocidad_barrido = self.wd_config.combo_velocidad_barrido.get()
#            mc.velocidad_puntero = self.wd_config.combo_velocidad_puntero.get()
#            self.wd_config.label_velocidad_puntero[
#                'text'] = f'Velocidad puntero: {mc.velocidad_puntero}'
#            self.wd_config.label_velocidad_barrido[
#                'text'] = f'Velocidad barrido [ms]: {mc.velocidad_barrido}'
        self.wd_config.btn_ok = tk.Button(
            self.wd_config.buttons, text='aplicar', command=self.config_on_closing, width=10, height=2, background='red')
        self.wd_config.btn_ok.pack(side=tk.RIGHT, padx=(10, 5), pady=10)
#        # cancel button
#        self.wd_config.btn_cancel = tk.Button(
#            self.wd_config.buttons, text='cancelar', command=config_on_closing, width=10, height=2)
#        self.wd_config.btn_cancel.pack(side=tk.LEFT, padx=(5, 10), pady=10)

        self.wd_config.idx = [self.wd_config.btn_5, self.wd_config.btn_10, self.wd_config.btn_15, self.wd_config.btn_20, self.wd_config.btn_750,
                    self.wd_config.btn_1000, self.wd_config.btn_1500, self.wd_config.btn_2000, self.wd_config.btn_ok]#self.wd_config.btn_cancel self.wd_config.btn_ok
        self.config_color()
    
    def config_color(self):
        if mc.in_window == 'config':
            for i in range(len(self.wd_config.idx)):
                if self.wd_config.idx[i].cget('background') == 'red':
                    self.wd_config.idx[i].configure(bg='white')
                    self.wd_config.idx[(i+1) % len(self.wd_config.idx)].configure(bg='red')
                    break
            self.after(1000, self.config_color)

    def open_use(self):
        self.wd_use = tk.Toplevel(self)
        self.wd_use.title("ventana de uso")
        self.wd_use.geometry("%dx%d+%d+%d" %(500, 450, self.winfo_x()-100, self.winfo_y()-100))
        #wd_use.resizable(False, False)
        self.wd_use.configure(background='pink')
        # ICONO
        self.img_icon = ImageTk.PhotoImage(Image.open("../recursos/logo.jpg"))
        self.wd_use.tk.call('wm', 'iconphoto', self.wd_use._w, self.img_icon)

        self.wd_use.wd = Window_use(self.wd_use)  # tapon
        self.wd_use.wd.pack()

        self.wd_use.protocol('WM_DELETE_WINDOW', self.use_on_closing)
        mc.in_window = 'use'
        self.withdraw()  # esconde mainwindow

    def start_gui(self):
        mc.gui_alive = True  # ver si no conviene ponerlo en el cons, de wd_use por flag en mouse
        mc.in_window = 'main'
        self.mainloop()
