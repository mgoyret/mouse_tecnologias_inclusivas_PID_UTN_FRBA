from time import sleep
import tkinter as tk
import myConfig as mc
from PIL import ImageTk, Image

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

        self.img = ImageTk.PhotoImage(Image.open("../recursos/minion.jpg"))
        self.labelIm = tk.Label(coordsLabels, image = self.img)
        self.labelIm.grid(row=0, column=1, padx=2, pady=2, sticky='nesw')




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


if __name__=="__main__":
    root = Gui()
    root.start_gui()
