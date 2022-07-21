from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image
import os 

#Attributes for the window
root = Tk()
root.title('4 Dry Out | Main Menu')
root.geometry("275x75")
root['bg']='blue'

class Menu:
    def __init__(self):
        # Creates the frame for the new window
        self.win = Toplevel()
        self.frameFit = Frame(self.win)
        self.frameFit.pack()

        # Label that creates a title
        self.TitleLabel = Label(self.frameFit, text="e-Rental Portal").pack()

        # A comboBox that contains five types of equipment
        self.Equipment = ["Air Movers/Fans", "Dehumifiers", "Air Filtration", "Generators", "Extractors/Cleaners"]
        self.equipCombo = ttk.Combobox(self.frameFit, value=self.Equipment)
        self.equipCombo.current(0)
        self.equipCombo.bind("<<ComboboxSelected>>")
        self.equipCombo.pack()

        # Asks the user for days for rental
        self.dayLabel = Label(self.frameFit, text="# Days to Rent: ").pack()
        self.dayTxt = Entry(self.frameFit, width=5)
        self.dayTxt.pack()

        # Asks the user for Equip Amt
        Label(self.frameFit, text="Amount of equipment: ").pack()
        self.equipAmt = Entry(self.frameFit, width=5)
        self.equipAmt.pack()


     # Submits the information to a module called calcTotal
        self.recordBtn = Button(self.frameFit, text="Calculate Total", command=self.calcTotal)
        self.recordBtn.pack()

        # This calculates the total amount due for renting equipment for # many days

    def calcTotal(self):
        # Creates variables to be used in this module
        self.Equipment = self.equipCombo.get()
        self.dayAmount = float(self.dayTxt.get())
        self.EquipAmt = float(self.equipAmt.get())

        # FAN RENTAL CALCULATION & PRINTS RESULT (TOTAL DUE)
        if self.Equipment == "Air Movers/Fans":
            self.fanTotal = 25 * self.dayAmount * self.EquipAmt
            self.totalLbl = Label(self.frameFit, text=f"Total Amount Due: ${round(int(self.fanTotal), 2)}").pack()
        elif self.Equipment == "Dehumifiers":
            self.dehuTotal = 50 * self.dayAmount * self.EquipAmt
            self.totalLbl = Label(self.frameFit, text=f"Total Amount Due: ${round(int(self.dehuTotal), 2)}").pack()
        elif self.Equipment == "Air Filtration":
            self.filtTotal = 175 * self.dayAmount * self.EquipAmt
            self.totalLbl = Label(self.frameFit, text=f"Total Amount Due: ${round(int(self.filtTotal), 2)}").pack()
        elif self.Equipment == "Generators":
            self.genTotal = 200 * self.dayAmount * self.EquipAmt
            self.totalLbl = Label(self.frameFit, text=f"Total Amount Due: ${round(int(self.genTotal), 2)}").pack()
        elif self.Equipment == "Extractors/Cleaners":
            self.extrTotal = 75 * self.dayAmount * self.EquipAmt
            self.totalLbl = Label(self.frameFit, text=f"Total Amount Due: ${round(int(self.extrTotal), 2)}").pack()
            

class MainWindow:
    # Creates the frame for the main window
    def __init__(self, master):
        mainFrame = Frame(master)
        mainFrame.pack()

        self.titleLabel = Label(master, text="4 Dry Out e-Rental", bg = "blue", fg = "white", font =("Montserrat", 20))
        self.titleLabel.pack()
        self.Btn = Button(master, text="Water Damage Equipment", command=self.MenuWindow, bg = "navy", fg = "white").pack()

    #Button opens a new window
    def MenuWindow(self):
        self.record = Menu()
        self.record.win.mainloop()

#Starts the main window
winStart = MainWindow(root)
root.mainloop()