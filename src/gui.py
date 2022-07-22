from cgitb import text
from time import sleep
import tkinter as tk
from tkinter import ttk
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


class Window_use(tk.Frame):

    idx = list()

    def __init__(self, parent):
        tk.Frame.__init__(self, parent, bg='pink')

        self.coords_clicks_Labels = tk.LabelFrame(self)  # , text='Direcciones'
        self.coords_clicks_Labels.grid(row=0, column=0)

        self.img_ul = {"black": ImageTk.PhotoImage(Image.open("../recursos/up_left_arrow_b.png").resize(
            size_diagonal)), "red": ImageTk.PhotoImage(Image.open("../recursos/up_left_arrow_r.png").resize(size_diagonal))}
        self.lbl_ul = tk.Label(self.coords_clicks_Labels,
                               image=self.img_ul["black"])
        self.lbl_ul.grid(row=0, column=0, padx=2, pady=2, sticky='nesw')

        self.img_u = {"black": ImageTk.PhotoImage(Image.open("../recursos/up_arrow_b.png").resize(
            size_vertical)), "red": ImageTk.PhotoImage(Image.open("../recursos/up_arrow_r.png").resize(size_vertical))}
        self.lbl_u = tk.Label(self.coords_clicks_Labels,
                              image=self.img_u["black"])
        self.lbl_u.grid(row=0, column=1, padx=2, pady=2, sticky='nesw')

        self.img_ur = {"black": ImageTk.PhotoImage(Image.open("../recursos/up_right_arrow_b.png").resize(
            size_diagonal)), "red": ImageTk.PhotoImage(Image.open("../recursos/up_right_arrow_r.png").resize(size_diagonal))}
        self.lbl_ur = tk.Label(self.coords_clicks_Labels,
                               image=self.img_ur["black"])
        self.lbl_ur.grid(row=0, column=2, padx=2, pady=2, sticky='nesw')

        self.img_l = {"black": ImageTk.PhotoImage(Image.open("../recursos/left_arrow_b.png").resize(
            size_vertical)), "red": ImageTk.PhotoImage(Image.open("../recursos/left_arrow_r.png").resize(size_vertical))}
        self.lbl_l = tk.Label(self.coords_clicks_Labels,
                              image=self.img_l["black"])
        self.lbl_l.grid(row=1, column=0, padx=2, pady=2, sticky='nesw')

        self.img_r = {"black": ImageTk.PhotoImage(Image.open("../recursos/right_arrow_b.png").resize(
            size_vertical)), "red": ImageTk.PhotoImage(Image.open("../recursos/right_arrow_r.png").resize(size_vertical))}
        self.lbl_r = tk.Label(self.coords_clicks_Labels,
                              image=self.img_r["black"])
        self.lbl_r.grid(row=1, column=2, padx=2, pady=2, sticky='nesw')

        self.img_dl = {"black": ImageTk.PhotoImage(Image.open("../recursos/down_left_arrow_b.png").resize(
            size_diagonal)), "red": ImageTk.PhotoImage(Image.open("../recursos/down_left_arrow_r.png").resize(size_diagonal))}
        self.lbl_dl = tk.Label(self.coords_clicks_Labels,
                               image=self.img_dl["black"])
        self.lbl_dl.grid(row=2, column=0, padx=2, pady=2, sticky='nesw')

        self.img_d = {"black": ImageTk.PhotoImage(Image.open("../recursos/down_arrow_b.png").resize(
            size_vertical)), "red": ImageTk.PhotoImage(Image.open("../recursos/down_arrow_r.png").resize(size_vertical))}
        self.lbl_d = tk.Label(self.coords_clicks_Labels,
                              image=self.img_d["black"])
        self.lbl_d.grid(row=2, column=1, padx=2, pady=2, sticky='nesw')

        self.img_dr = {"black": ImageTk.PhotoImage(Image.open("../recursos/down_right_arrow_b.png").resize(
            size_diagonal)), "red": ImageTk.PhotoImage(Image.open("../recursos/down_right_arrow_r.png").resize(size_diagonal))}
        self.lbl_dr = tk.Label(self.coords_clicks_Labels,
                               image=self.img_dr["black"])
        self.lbl_dr.grid(row=2, column=2, padx=2, pady=2, sticky='nesw')

        self.clickLabels = tk.LabelFrame(
            self.coords_clicks_Labels)  # , text='clicks'
        self.clickLabels.grid(row=1, column=1, padx=2, pady=2)

        self.img_ci = {"black": ImageTk.PhotoImage(Image.open(
            "../recursos/click_b.png").resize(size_click)), "red": ImageTk.PhotoImage(Image.open("../recursos/click_r.png").resize(size_click))}
        self.lbl_ci = tk.Label(self.clickLabels, image=self.img_ci['black'])
        self.lbl_ci.grid(row=0, column=0, padx=2, pady=2, sticky='nesw')

        self.img_cd = {"black": ImageTk.PhotoImage(Image.open(
            "../recursos/click_b.png").resize(size_click)), "red": ImageTk.PhotoImage(Image.open("../recursos/click_r.png").resize(size_click))}
        self.lbl_cd = tk.Label(self.clickLabels, image=self.img_cd['black'])
        self.lbl_cd.grid(row=0, column=1, padx=2, pady=2, sticky='nesw')

        self.packLabels = tk.LabelFrame(self)
        self.packLabels.grid(row=0, column=1)

        self.ruedaLabels = tk.LabelFrame(self.packLabels, text='Rueda')
        self.ruedaLabels.grid(row=1, column=0)

        self.img_wu = {"black": ImageTk.PhotoImage(Image.open(
            "../recursos/click_b.png").resize(size_rueda)), "red": ImageTk.PhotoImage(Image.open("../recursos/click_r.png").resize(size_rueda))}
        self.lbl_wu = tk.Label(self.ruedaLabels, image=self.img_wu['black'])
        self.lbl_wu.grid(row=0, column=3, padx=2, pady=2, sticky='nesw')

        self.img_wd = {"black": ImageTk.PhotoImage(Image.open(
            "../recursos/click_b.png").resize(size_rueda)), "red": ImageTk.PhotoImage(Image.open("../recursos/click_r.png").resize(size_rueda))}
        self.lbl_wd = tk.Label(self.ruedaLabels, image=self.img_wd['red'])
        self.lbl_wd.grid(row=2, column=3, padx=2, pady=2, sticky='nesw')

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
            'wd':   'r'
        }

        self.color()

    def color(self):
        if mc.color_flag:
            for i in self.idx:
                if self.idx[i] == 'r':
                    if i == 'ul':
                        self.lbl_ul = tk.Label(
                            self.coords_clicks_Labels, image=self.img_ul["black"])
                        self.lbl_ul.grid(
                            row=0, column=0, padx=2, pady=2, sticky='nesw')
                        self.lbl_u = tk.Label(
                            self.coords_clicks_Labels, image=self.img_u["red"])
                        self.lbl_u.grid(row=0, column=1, padx=2,
                                        pady=2, sticky='nesw')
                        self.idx['u'] = 'r'

                    elif i == 'u':
                        self.lbl_u = tk.Label(
                            self.coords_clicks_Labels, image=self.img_u["black"])
                        self.lbl_u.grid(row=0, column=1, padx=2,
                                        pady=2, sticky='nesw')
                        self.lbl_ur = tk.Label(
                            self.coords_clicks_Labels, image=self.img_ur["red"])
                        self.lbl_ur.grid(
                            row=0, column=2, padx=2, pady=2, sticky='nesw')
                        self.idx['ur'] = 'r'

                    elif i == 'ur':
                        self.lbl_ur = tk.Label(
                            self.coords_clicks_Labels, image=self.img_ur["black"])
                        self.lbl_ur.grid(
                            row=0, column=2, padx=2, pady=2, sticky='nesw')
                        self.lbl_l = tk.Label(
                            self.coords_clicks_Labels, image=self.img_l["red"])
                        self.lbl_l.grid(row=1, column=0, padx=2,
                                        pady=2, sticky='nesw')
                        self.idx['l'] = 'r'

                    elif i == 'l':
                        self.lbl_l = tk.Label(
                            self.coords_clicks_Labels, image=self.img_l["black"])
                        self.lbl_l.grid(row=1, column=0, padx=2,
                                        pady=2, sticky='nesw')
                        self.lbl_r = tk.Label(
                            self.coords_clicks_Labels, image=self.img_r["red"])
                        self.lbl_r.grid(row=1, column=2, padx=2,
                                        pady=2, sticky='nesw')
                        self.idx['r'] = 'r'

                    elif i == 'r':
                        self.lbl_r = tk.Label(
                            self.coords_clicks_Labels, image=self.img_r["black"])
                        self.lbl_r.grid(row=1, column=2, padx=2,
                                        pady=2, sticky='nesw')
                        self.lbl_dl = tk.Label(
                            self.coords_clicks_Labels, image=self.img_dl["red"])
                        self.lbl_dl.grid(
                            row=2, column=0, padx=2, pady=2, sticky='nesw')
                        self.idx['dl'] = 'r'

                    elif i == 'dl':
                        self.lbl_dl = tk.Label(
                            self.coords_clicks_Labels, image=self.img_dl["black"])
                        self.lbl_dl.grid(
                            row=2, column=0, padx=2, pady=2, sticky='nesw')
                        self.lbl_d = tk.Label(
                            self.coords_clicks_Labels, image=self.img_d["red"])
                        self.lbl_d.grid(row=2, column=1, padx=2,
                                        pady=2, sticky='nesw')
                        self.idx['d'] = 'r'

                    elif i == 'd':
                        self.lbl_d = tk.Label(
                            self.coords_clicks_Labels, image=self.img_d["black"])
                        self.lbl_d.grid(row=2, column=1, padx=2,
                                        pady=2, sticky='nesw')
                        self.lbl_dr = tk.Label(
                            self.coords_clicks_Labels, image=self.img_dr["red"])
                        self.lbl_dr.grid(
                            row=2, column=2, padx=2, pady=2, sticky='nesw')
                        self.idx['dr'] = 'r'

                    elif i == 'dr':
                        self.lbl_dr = tk.Label(
                            self.coords_clicks_Labels, image=self.img_dr["black"])
                        self.lbl_dr.grid(
                            row=2, column=2, padx=2, pady=2, sticky='nesw')
                        self.lbl_ci = tk.Label(
                            self.clickLabels, image=self.img_ci["red"])
                        self.lbl_ci.grid(
                            row=0, column=0, padx=2, pady=2, sticky='nesw')
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
                        self.lbl_ul = tk.Label(
                            self.coords_clicks_Labels, image=self.img_ul['red'])
                        self.lbl_ul.grid(
                            row=0, column=0, padx=2, pady=2, sticky='nesw')
                        self.idx['ul'] = 'r'

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

    def __init__(self):
        tk.Tk.__init__(self)

        self.title("Ventana Principal")
        self.geometry("200x200")
        #self.resizable(False, False)
        self.configure(background='#F2B33D')
        self.protocol("WM_DELETE_WINDOW", self.finish_gui)
        self.eval('tk::PlaceWindow . center')
        mc.gui_alive = True  # ver si no conviene ponerlo en el cons, de wd_use por flag en mouse

    def open_config(self):
        self.wd_config = tk.Toplevel(self)
        self.wd_config.title("ventana de configuracion")
        self.wd_config.geometry("%dx%d+%d+%d" %
                                (400, 200, self.winfo_x(), self.winfo_y()))
        self.wd_config.resizable(False, False)
        self.wd_config.configure(background='pink')

        # velocidad puntero
        self.wd_config.velocidad_puntero = tk.LabelFrame(
            self.wd_config, text='velocidad del puntero')
        self.wd_config.velocidad_puntero.pack(
            padx=10, pady=10, expand=True, fill='both')

        def set_velocidad_puntero(dumb):
            mc.velocidad_puntero = self.wd_config.combo_velocidad_puntero.get()
            self.wd_config.label_velocidad_puntero[
                'text'] = f'Velocidad puntero: {mc.velocidad_puntero}'

            # label
        self.wd_config.label_velocidad_puntero = tk.Label(
            self.wd_config.velocidad_puntero, text=f'Velocidad puntero: {mc.velocidad_puntero}')
        self.wd_config.label_velocidad_puntero.pack(
            side=tk.LEFT, padx=5, pady=5)
        # combo
        self.wd_config.combo_velocidad_puntero = ttk.Combobox(
            self.wd_config.velocidad_puntero, state='readonly', values=[5, 10, 15, 20])
        self.wd_config.combo_velocidad_puntero.pack(
            side=tk.RIGHT, padx=5, pady=5)
        self.wd_config.combo_velocidad_puntero.set('valor')
        self.wd_config.combo_velocidad_puntero.bind(
            "<<ComboboxSelected>>", set_velocidad_puntero)

        # velocidad barrido
        self.wd_config.velocidad_barrido = tk.LabelFrame(
            self.wd_config, text='velocidad barrido')
        self.wd_config.velocidad_barrido.pack(
            padx=10, pady=10, expand=True, fill='both')

        def set_velocidad_barrido(dumb):
            mc.velocidad_barrido = self.wd_config.combo_velocidad_barrido.get()
            self.wd_config.label_velocidad_barrido[
                'text'] = f'Velocidad barrido: {mc.velocidad_barrido}'

            # label
        self.wd_config.label_velocidad_barrido = tk.Label(
            self.wd_config.velocidad_barrido, text=f'Velocidad barrido [ms]: {mc.velocidad_barrido}')
        self.wd_config.label_velocidad_barrido.pack(
            side=tk.LEFT, padx=5, pady=5)
        # combo
        self.wd_config.combo_velocidad_barrido = ttk.Combobox(
            self.wd_config.velocidad_barrido, state='readonly', values=[750, 1000, 1500, 2000])
        self.wd_config.combo_velocidad_barrido.pack(
            side=tk.RIGHT, padx=5, pady=5)
        self.wd_config.combo_velocidad_barrido.set('valor')
        self.wd_config.combo_velocidad_barrido.bind(
            "<<ComboboxSelected>>", set_velocidad_barrido)

    def open_use(self):
        self.wd_use = tk.Toplevel(self)

        self.wd_use.title("ventana de uso")
        self.wd_use.geometry("%dx%d+%d+%d" %
                             (500, 450, self.winfo_x(), self.winfo_y()))
        #wd_use.resizable(False, False)
        self.wd_use.configure(background='pink')
        self.wd_use.wd = Window_use(self.wd_use)
        self.wd_use.wd.pack()

    def start_gui(self):

        self.btn_config = tk.Button(
            self, text='configuracion', command=partial(self.open_config))
        self.btn_config.pack(padx=5, pady=5, expand=True, fill='both')
        self.btn_use = tk.Button(
            self, text='comenzar', command=partial(self.open_use))
        self.btn_use.pack(padx=5, pady=5, expand=True, fill='both')
        self.mainloop()
