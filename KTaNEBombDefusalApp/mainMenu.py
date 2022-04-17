from KTaNEBombDefusalApp.Wires import Wires
from KTaNEBombDefusalApp.TheButton import TheButton
from KTaNEBombDefusalApp.Keypad import Keypad
from KTaNEBombDefusalApp.SimonSays import SimonSays
from KTaNEBombDefusalApp.WhosOnFirst import WhosOnFirst
from KTaNEBombDefusalApp.Memory import Memory
from KTaNEBombDefusalApp.MorseCode import MorseCode
from KTaNEBombDefusalApp.ComplexWires import ComplexWires
from KTaNEBombDefusalApp.WireSequences import WireSequences
from KTaNEBombDefusalApp.Mazes import Mazes
from KTaNEBombDefusalApp.Passwords import Passwords
from KTaNEBombDefusalApp.Knob import Knob
from tkinter import *
from tkinter.font import Font

back = "#8f1c0a"


class MainMenu:

    def reset(self):
        self.master.destroy()
        self.__init__()

    def __init__(self):
        self.master = Tk()
        self.master.title("BombDefuseApp")
        self.master.resizable(False, False)
        self.master.config(bg=back)
        self.lftPos = (self.master.winfo_screenwidth() - 1000) / 2
        self.topPos = (self.master.winfo_screenheight() - 700) / 2
        self.master.geometry("%dx%d+%d+%d" % (1000, 700, self.lftPos, self.topPos))

        self.manual_font = Font(family="Terminal", size=20)
        self.serial = ""
        self.batteries = -1
        self.parallel = IntVar()

        self.wires = PhotoImage(file="Images/Wires.png")
        self.theButton = PhotoImage(file="Images/TheButton.png")
        self.keypad = PhotoImage(file="Images/Keypad.png")
        self.simonSays = PhotoImage(file="Images/SimonSays.png")
        self.whosOnFirst = PhotoImage(file="Images/WhosOnFirst.png")
        self.memory = PhotoImage(file="Images/Memory.png")
        self.morseCode = PhotoImage(file="Images/MorseCode.png")
        self.complexWires = PhotoImage(file="Images/ComplexWires.png")
        self.wireSequences = PhotoImage(file="Images/WireSequences.png")
        self.maze = PhotoImage(file="Images/Maze.png")
        self.password = PhotoImage(file="Images/Passwords.png")
        self.knob = PhotoImage(file="Images/Knob.png")

        self.nameLabel = Label(self.master, font=("Terminal", 25), fg="white", bg=back,
                               text="KEEP TALKING AND NOBODY EXPLODES\n BOMB DEFUSAL APP")
        self.selectLabel = Label(self.master, font=("Terminal", 20), fg="white", bg=back,
                                 text='''
WELCOME TO THE 
KEEP TALKING AND NOBODY EXPLODES BOMB DEFUSAL APP,
WHERE YOU CAN DEFUSE ANY VANILLA BOMB FROM THE GAME 
'KEEP TALKING AND NOBODY EXPLODES'.
TO START, SIMPLY PRESS THE 'START' BUTTON BELOW. 
THE APP WILL THEN FIRST ASK FOR
IMPORTANT INFO OF THE BOMB, SUCH AS THE SERIAL NUMBER, 
NUMBER OF BATTERIES AND IF THE BOMB HAS A PARALLEL PORT. 
THESE WILL HELP WITH DEFUSING
THE MODULES THAT REQUIRE THAT INFORMATION.
                                      ''')

        self.entryFrame = Frame(self.master, bg=back)
        self.serial_frame = Frame(self.entryFrame, bg=back)
        self.batteries_frame = Frame(self.entryFrame, bg=back)
        self.parallel_frame = Frame(self.entryFrame, bg=back)

        self.mainFrame = Frame(self.master, bg=back)
        self.firstFrame = Frame(self.mainFrame, bg=back)
        self.secondFrame = Frame(self.mainFrame, bg=back)
        self.thirdFrame = Frame(self.mainFrame, bg=back)
        self.fourthFrame = Frame(self.mainFrame, bg=back)
        self.fifthFrame = Frame(self.mainFrame, bg=back)
        self.sixthFrame = Frame(self.mainFrame, bg=back)

        self.nameLabel.pack(side=TOP, pady=30)
        self.selectLabel.pack(side=TOP, pady=30)
        pad = 20
        self.firstFrame.pack(side=LEFT, padx=5, ipadx=20)
        self.secondFrame.pack(side=LEFT, padx=pad)
        self.thirdFrame.pack(side=LEFT, padx=pad)
        self.fourthFrame.pack(side=LEFT, padx=pad)
        self.fifthFrame.pack(side=LEFT, padx=pad)
        self.sixthFrame.pack(side=LEFT, padx=pad)

        self.var = StringVar()
        self.var.trace("w", lambda name, index, mode, var=self.var: self.check_serial(var))
        self.serial_entry = Entry(self.serial_frame, textvariable=self.var, font=self.manual_font, width=10)
        self.serial_label = Label(self.serial_frame, font=self.manual_font, text="SERIAL NUMBER", bg=back, fg="white")
        self.batteries_entry = Spinbox(self.batteries_frame, from_=0, to=10, font=self.manual_font, width=2,
                                       state='readonly')
        self.batteries_label = Label(self.batteries_frame, font=self.manual_font, text="BATTERIES", bg=back, fg="white")

        self.parallel_port = Radiobutton(self.parallel_frame, text="BOMB HAS\nA PARALLEL PORT", fg="white",
                                         selectcolor=back, bg=back,
                                         activebackground=back, font=self.manual_font, variable=self.parallel, value=1)
        self.no_parallel_port = Radiobutton(self.parallel_frame, text="BOMB DOESN'T HAVE\nA PARALLEL PORT", fg="white",
                                            selectcolor=back, bg=back,
                                            activebackground=back, font=self.manual_font, variable=self.parallel,
                                            value=0)

        self.serial_entry.pack()
        self.serial_label.pack()
        self.batteries_entry.pack()
        self.batteries_label.pack()
        self.parallel_port.pack()
        self.no_parallel_port.pack()

        self.serial_frame.pack(side=LEFT)
        self.batteries_frame.pack(side=LEFT, padx=10)
        self.parallel_frame.pack(padx=10)
        self.nextButton = Button(self.master, text="START", font=("Terminal", 20),
                                 command=lambda: self.place_entries())
        self.nextButton.pack()
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
            ("label", self.firstFrame, "MORSE\nCODE\n", TOP),
            ("button", self.secondFrame, self.complexWires, lambda: self.module(7), TOP),
            ("label", self.secondFrame, "COMPLEX\nWIRES\n", TOP),
            ("button", self.thirdFrame, self.wireSequences, lambda: self.module(8), TOP),
            ("label", self.thirdFrame, "WIRE\nSEQUENCES\n", TOP),
            ("button", self.fourthFrame, self.maze, lambda: self.module(9), TOP),
            ("label", self.fourthFrame, "MAZES\n\n", TOP),
            ("button", self.fifthFrame, self.password, lambda: self.module(10), TOP),
            ("label", self.fifthFrame, "PASSWORDS\n\n", TOP),
            ("button", self.sixthFrame, self.knob, lambda: self.module(11), TOP),
            ("label", self.sixthFrame, "KNOB\n\n", TOP)
        ]

        for info in button_info:
            if info[0] == "button":
                Button(info[1], image=info[2], command=info[3]).pack(side=info[4])
            else:
                Label(info[1], text=info[2], fg='white', font=self.manual_font, bg=back).pack(side=info[3])

    def place_entries(self):
        self.nextButton.pack_forget()
        self.entryFrame.pack()
        self.nextButton.pack()
        self.selectLabel.config(text="WRITE DOWN ALL THE INFORMATION OF THE BOMB\n")
        self.nextButton.config(text="NEXT", command=lambda: self.place_modules(), state=DISABLED)

    def check_serial(self, var):
        if len(var.get()) == 6:
            self.nextButton.config(state=NORMAL)
        else:
            self.nextButton.config(state=DISABLED)

    def place_modules(self):
        entry = str(self.serial_entry.get().translate({ord(i): None for i in '-._/ "' + "'"}).upper())
        self.serial = entry
        self.batteries = int(self.batteries_entry.get())
        if len(entry) < 6:
            self.serial = self.serial + "s"
        try:
            int(self.serial[-1])
        except ValueError:
            self.selectLabel.config(text="WRITE ALL THE NECESSARY SPECIFICATIONS OF THE BOMB\n"
                                         "MAKE SURE YOU WROTE THE SERIAL NUMBER CORRECTLY")
            return None
        if self.parallel.get() == 1:
            self.parallel = True
        else:
            self.parallel = False
        self.entryFrame.pack_forget()
        self.selectLabel.config(text="-BOMB SPECIFICATIONS-\n"
                                     "SERIAL NUMBER: {}\n"
                                     "BATTERIES: {}\n"
                                     "PARALLEL PORT: {}\n\n"
                                     "SELECT A MODULE TO DEFUSE".format(self.serial, self.batteries, self.parallel))
        self.mainFrame.pack()
        self.nextButton.config(text="RESET", command=lambda: self.reset())
        self.nextButton.place(x=0, y=0)

    def module(self, num):
        if num == 0:
            Wires(self.master, back, self.manual_font, self.serial)
        elif num == 1:
            TheButton(self.master, back, self.manual_font, self.batteries)
        elif num == 2:
            Keypad(self.master, back)
        elif num == 3:
            SimonSays(self.master, back, self.manual_font, self.serial)
        elif num == 4:
            WhosOnFirst(self.master, back, self.manual_font)
        elif num == 5:
            Memory(self.master, back, self.manual_font)
        elif num == 6:
            MorseCode(self.master, back, self.manual_font)
        elif num == 7:
            ComplexWires(self.master, back, self.manual_font, self.serial, self.batteries, self.parallel)
        elif num == 8:
            WireSequences(self.master, back, self.manual_font)
        elif num == 9:
            Mazes(self.master, back, self.manual_font)
        elif num == 10:
            Passwords(self.master, back, self.manual_font)
        elif num == 11:
            Knob(self.master, back, self.manual_font)
        else:
            print("No valid module")

    def start(self):
        self.master.mainloop()
