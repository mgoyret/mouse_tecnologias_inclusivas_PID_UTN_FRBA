from time import sleep
import tkinter as tk
import myConfig as mc

# se define la clase de la ventana principal, con un frame dentro
# con los labes deseados


class Window(tk.Frame):

    idx = list()

    def __init__(self, parent):

        tk.Frame.__init__(self, parent, bg='white')

        self.color_flag = bool(True)

        coordsLabels = tk.LabelFrame(self, text='Direcciones')
        coordsLabels.grid(row=0, column=0)

        self.lb_N = tk.Label(coordsLabels, text='norte',
                             bg='light blue', font=('bold', 20))
        self.lb_N.grid(row=0, column=1, padx=2, pady=2, sticky='nesw')

        self.lb_S = tk.Label(coordsLabels, text='sur',
                             bg='light blue', font=('bold', 20))
        self.lb_S.grid(row=2, column=1, padx=2, pady=2, sticky='nesw')

        self.lb_E = tk.Label(coordsLabels, text='este',
                             bg='light blue', font=('bold', 20))
        self.lb_E.grid(row=1, column=2, padx=2, pady=2, sticky='nesw')

        self.lb_O = tk.Label(coordsLabels, text='oeste',
                             bg='light blue', font=('bold', 20))
        self.lb_O.grid(row=1, column=0, padx=2, pady=2, sticky='nesw')

        self.lb_NE = tk.Label(coordsLabels, text='noreste',
                              bg='light blue', font=('bold', 20))
        self.lb_NE.grid(row=0, column=2, padx=2, pady=2, sticky='nesw')

        self.lb_NO = tk.Label(coordsLabels, text='noroeste',
                              bg='light blue', font=('bold', 20))
        self.lb_NO.grid(row=0, column=0, padx=2, pady=2, sticky='nesw')

        self.lb_SE = tk.Label(coordsLabels, text='sudeste',
                              bg='light blue', font=('bold', 20))
        self.lb_SE.grid(row=2, column=2, padx=2, pady=2, sticky='nesw')

        self.lb_SO = tk.Label(coordsLabels, text='sudoeste',
                              bg='light blue', font=('bold', 20))
        self.lb_SO.grid(row=2, column=0, padx=2, pady=2, sticky='nesw')

        packLabels = tk.LabelFrame(self)
        packLabels.grid(row=0, column=1)

        clickLabels = tk.LabelFrame(packLabels, text='clicks')
        clickLabels.grid(row=0, column=0)

        self.lb_CI = tk.Label(clickLabels, text='ci',
                              bg='light blue', font=('bold', 20))
        self.lb_CI.grid(row=0, column=0, padx=2, pady=2, sticky='nesw')

        self.lb_CD = tk.Label(clickLabels, text='cd',
                              bg='light blue', font=('bold', 20))
        self.lb_CD.grid(row=0, column=1, padx=2, pady=2, sticky='nesw')

        ruedaLabels = tk.LabelFrame(packLabels, text='Rueda')
        ruedaLabels.grid(row=1, column=0)

        self.lb_rueda_N = tk.Label(
            ruedaLabels, text='rueda_N', bg='light blue', font=('bold', 12))
        self.lb_rueda_N.grid(row=0, column=3, padx=2, pady=2, sticky='nesw')

        self.lb_rueda_S = tk.Label(
            ruedaLabels, text='rueda_S', bg='light blue', font=('bold', 12))
        self.lb_rueda_S.grid(row=2, column=3, padx=2, pady=2, sticky='nesw')

        # SE es el ultimo boton, lo pongo pink para que en la primera
        # ejecucion de color() se cambie a NO
        self.lb_rueda_C = tk.Label(
            ruedaLabels, text='rueda_C', bg='pink', font=('bold', 12))
        self.lb_rueda_C.grid(row=1, column=3, padx=2, pady=2, sticky='nesw')

        self.idx = [self.lb_NO, self.lb_N, self.lb_NE, self.lb_O, self.lb_E, self.lb_SO, self.lb_S,
                    self.lb_SE, self.lb_CI, self.lb_CD, self.lb_rueda_N, self.lb_rueda_S, self.lb_rueda_C]
        self.color()

    # esta funcion miembro analiza cuando un label tiene color rosa
    # y lo pone el azul, para luego poner el siguiente en rosa
    def color(self):
        if self.color_flag:
            for i in range(len(self.idx)):
                if self.idx[i].cget('background') == 'pink':
                    self.idx[i].configure(bg='light blue')
                    self.idx[(i+1) % 13].configure(bg='pink')
                    break
        self.after(1000, self.color)


class Gui(tk.Tk):

    # defino esta variable para que sea iembro y luego
    # igualarla a la ventana principal de la gui
    wd = None

    def finish_gui(self):
        mc.gui_alive = False
        # damos tiempo a que muera "mouse" que usa la gui
        sleep(0.5)
        self.destroy()

    def __init__(self):
        tk.Tk.__init__(self)

        self.title("Controlador de mouse")
        self.geometry("400x300")
        self.minsize(450, 350)
        self.maxsize(450, 350)
        self.configure(background='#F2B33D')

        self.protocol("WM_DELETE_WINDOW", self.finish_gui)

    def start_gui(self):
        self.eval('tk::PlaceWindow . center')
        self.wd = Window(self)
        self.wd.pack(expand=True)
        self.mainloop()
