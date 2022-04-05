from KTaNEBombDefusalApp.Wires import *
from KTaNEBombDefusalApp.theButton import *
from KTaNEBombDefusalApp.Keypad import *
from KTaNEBombDefusalApp.SimonSays import *
from KTaNEBombDefusalApp.WhosOnFirst import *
from KTaNEBombDefusalApp.Memory import *
from KTaNEBombDefusalApp.MorseCode import *
from KTaNEBombDefusalApp.ComplexWires import *
from KTaNEBombDefusalApp.WireSequences import *

back = "#8f1c0a"


class MainMenu:
    def __init__(self):
        self.master = Tk()
        self.master.title("BombDefuseApp")
        self.master.resizable(False, False)
        self.master.config(bg=back)
        self.lftPos = (self.master.winfo_screenwidth() - 1000) / 2
        self.topPos = (self.master.winfo_screenheight() - 700) / 2
        self.master.geometry("%dx%d+%d+%d" % (1000, 700, self.lftPos, self.topPos))

        self.manual_font = Font(family="Terminal", size=20)

        self.wires = PhotoImage(file="Images/Wires.png")
        self.theButton = PhotoImage(file="Images/TheButton.png")
        self.keypad = PhotoImage(file="Images/Keypad.png")
        self.simonSays = PhotoImage(file="Images/SimonSays.png")
        self.whosOnFirst = PhotoImage(file="Images/WhosOnFirst.png")
        self.memory = PhotoImage(file="Images/Memory.png")
        self.morseCode = PhotoImage(file="Images/MorseCode.png")
        self.complexWires = PhotoImage(file="Images/ComplexWires.png")
        self.wireSequences = PhotoImage(file="Images/WireSequences.png")

        self.nameLabel = Label(self.master, font=("Terminal", 25), fg="white", bg=back,
                               text="KEEP TALKING AND NOBODY EXPLODES\n BOMB DEFUSE APP")
        self.selectLabel = Label(self.master, font=("Terminal", 20), fg="white", bg=back,
                                 text="SELECT A MODULE TO DEFUSE")

        self.firstFrame = Frame(self.master, bg=back)
        self.secondFrame = Frame(self.master, bg=back)
        self.thirdFrame = Frame(self.master, bg=back)
        self.fourthFrame = Frame(self.master, bg=back)
        self.fifthFrame = Frame(self.master, bg=back)
        self.sixthFrame = Frame(self.master, bg=back)

        self.nameLabel.pack(side=TOP, pady=30)
        self.selectLabel.pack(side=TOP, pady=30)
        pad = 20
        self.firstFrame.pack(ipadx=20)
        self.firstFrame.pack(side=LEFT, padx=5)
        self.secondFrame.pack(side=LEFT, padx=pad)
        self.thirdFrame.pack(side=LEFT, padx=pad)
        self.fourthFrame.pack(side=LEFT, padx=pad)
        self.fifthFrame.pack(side=LEFT, padx=pad)
        self.sixthFrame.pack(side=LEFT, padx=pad)

        button_info = [
            ("button", self.firstFrame, self.wires, lambda: self.module(0), TOP),
            ("label", self.firstFrame, "WIRES\n ", TOP),
            ("button", self.secondFrame, self.theButton, lambda: self.module(1), TOP),
            ("label", self.secondFrame, "THE\nBUTTON", TOP),
            ("button", self.thirdFrame, self.keypad, lambda: self.module(2), TOP),
            ("label", self.thirdFrame, "KEYPAD\n ", TOP),
            ("button", self.fourthFrame, self.simonSays, lambda: self.module(3), TOP),
            ("label", self.fourthFrame, "SIMON\nSAYS", TOP),
            ("button", self.fifthFrame, self.whosOnFirst, lambda: self.module(4), TOP),
            ("label", self.fifthFrame, "WHO'S ON\nFIRST", TOP),
            ("button", self.sixthFrame, self.memory, lambda: self.module(5), TOP),
            ("label", self.sixthFrame, "MEMORY\n ", TOP),
            ("button", self.firstFrame, self.morseCode, lambda: self.module(6), TOP),
            ("label", self.firstFrame, "MORSE\nCODE", TOP),
            ("button", self.secondFrame, self.complexWires, lambda: self.module(7), TOP),
            ("label", self.secondFrame, "COMPLEX\nWIRES", TOP),
            ("button", self.thirdFrame, self.wireSequences, lambda: self.module(8), TOP),
            ("label", self.thirdFrame, "WIRE\nSEQUENCES", TOP)
        ]

        for info in button_info:
            if info[0] == "button":
                Button(info[1], image=info[2], command=info[3]).pack(side=info[4])
            else:
                Label(info[1], text=info[2], fg='white', font=self.manual_font, bg=back).pack(side=info[3])

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
        elif num == 6:
            MorseCode(self.master, back, self.manual_font)
        elif num == 7:
            ComplexWires(self.master, back, self.manual_font)
        elif num == 8:
            WireSequences(self.master, back, self.manual_font)
        else:
            print("No valid module")

    def start(self):
        self.master.mainloop()
