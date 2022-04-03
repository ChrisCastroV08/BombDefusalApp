from KTaNEBombDefusalApp.Wires import *
from KTaNEBombDefusalApp.theButton import *
from KTaNEBombDefusalApp.Keypad import *
from KTaNEBombDefusalApp.SimonSays import *
from KTaNEBombDefusalApp.WhosOnFirst import *
from KTaNEBombDefusalApp.Memory import *
from KTaNEBombDefusalApp.ComplexWires import *

back = "#8f1c0a"


class MainMenu:
    def __init__(self):
        self.master = Tk()
        self.master.title("BombDefuseApp")
        self.master.resizable(False, False)
        self.master.config(bg=back)
        self.lftPos = (self.master.winfo_screenwidth() - 1150) / 2
        self.topPos = (self.master.winfo_screenheight() - 700) / 2
        self.master.geometry("%dx%d+%d+%d" % (1150, 700, self.lftPos, self.topPos))

        self.manual_font = Font(family="Terminal", size=20)
        self.wires = PhotoImage(file="Images/Wires.png")
        self.theButton = PhotoImage(file="Images/TheButton.png")
        self.keypad = PhotoImage(file="Images/Keypad.png")
        self.simonSays = PhotoImage(file="Images/SimonSays.png")
        self.whosOnFirst = PhotoImage(file="Images/WhosOnFirst.png")
        self.memory = PhotoImage(file="Images/Memory.png")
        self.morseCode = PhotoImage(file="Images/MorseCode.png")
        self.complexWires = PhotoImage(file="Images/ComplexWires.png")

        self.nameLabel = Label(self.master, font=("Terminal", 25), fg="white", bg=back,
                               text="KEEP TALKING AND NOBODY EXPLODES\n BOMB DEFUSE APP")
        self.selectLabel = Label(self.master, font=("Terminal", 20), fg="white", bg=back,
                                 text="SELECT A MODULE TO DEFUSE")
        self.topButtons = Frame(self.master, bg=back)
        self.topLabels = Frame(self.master, bg=back)
        self.bottomButtons = Frame(self.master, bg=back)
        self.bottomLabels = Frame(self.master, bg=back)

        self.nameLabel.pack(side=TOP, pady=30)
        self.selectLabel.pack(side=TOP, pady=30)

        self.topButtons.pack()
        self.topLabels.pack(pady=5)
        self.bottomButtons.pack()
        self.bottomLabels.pack()

        Button(self.topButtons, image=self.wires, text="", font=("Terminal", 20), command=lambda: self.module(0)).pack(
            padx=10, side=LEFT)
        Button(self.topButtons, image=self.theButton, text="", font=("Terminal", 20),
               command=lambda: self.module(1)).pack(padx=10, side=LEFT)
        Button(self.topButtons, image=self.keypad, text="", font=("Terminal", 20),
               command=lambda: self.module(2)).pack(padx=10, side=LEFT)
        Button(self.topButtons, image=self.simonSays, text="", font=("Terminal", 20),
               command=lambda: self.module(3)).pack(padx=10, side=LEFT)
        Button(self.topButtons, image=self.whosOnFirst, text="", font=("Terminal", 20),
               command=lambda: self.module(4)).pack(padx=15, side=LEFT)
        Button(self.topButtons, image=self.memory, text="", font=("Terminal", 20),
               command=lambda: self.module(5)).pack(padx=10, side=LEFT)
        Button(self.topButtons, image=self.morseCode, text="", font=("Terminal", 20),
               command=lambda: self.module(6)).pack(padx=10, side=LEFT)
        Button(self.topButtons, image=self.complexWires, text="", font=("Terminal", 20),
               command=lambda: self.module(7)).pack(padx=25, side=LEFT)

        Label(self.topLabels, text="WIRES", fg='white', font=self.manual_font, bg=back).pack(padx=30, side=LEFT)
        Label(self.topLabels, text="THE\nBUTTON", fg='white', font=self.manual_font, bg=back).pack(padx=15, side=LEFT)
        Label(self.topLabels, text="KEYPAD", fg='white', font=self.manual_font, bg=back).pack(padx=20, side=LEFT)
        Label(self.topLabels, text="SIMON\nSAYS", fg='white', font=self.manual_font, bg=back).pack(padx=10, side=LEFT)
        Label(self.topLabels, text="WHO'S ON\nFIRST", fg='white',
              font=self.manual_font, bg=back).pack(padx=0, side=LEFT)
        Label(self.topLabels, text="MEMORY", fg='white', font=self.manual_font, bg=back).pack(padx=20, side=LEFT)
        Label(self.topLabels, text="MORSE\nCODE", fg='white', font=self.manual_font, bg=back).pack(padx=10, side=LEFT)
        Label(self.topLabels, text="COMPLICATED\nWIRES", fg='white',
              font=self.manual_font, bg=back).pack(padx=10, side=LEFT)

    def module(self, num):
        if num == 0:
            Wires(self.master, back)
        elif num == 1:
            TheButton(self.master, back)
        elif num == 2:
            Keypad(self.master, back)
        elif num == 3:
            SimonSays(self.master, back, self.manual_font)
        elif num == 4:
            WhosOnFirst(self.master, back, self.manual_font)
        elif num == 5:
            Memory(self.master, back, self.manual_font)
        elif num == 7:
            ComplexWires(self.master, back, self.manual_font)
        else:
            print("No valid module")

    def start(self):
        self.master.mainloop()
