from tkinter import *


class WireSequences:

    def reset(self, num):
        if num == 0:
            self.wireSequencesWin.destroy()
        elif num == 1:
            self.wireSequencesWin.destroy()
            self.__init__(self.root, self.back, self.manual_font)

    def __init__(self, root, back, font):
        self.root = root
        self.back = back
        self.manual_font = font
        self.wireSequencesWin = Toplevel(self.root)
        self.wireSequencesWin.title("Wire Sequences")
        self.wireSequencesWin.resizable(False, False)
        self.wireSequencesWin.config(bg=back)
        self.lftPos = (self.wireSequencesWin.winfo_screenwidth() - 1000) / 2
        self.topPos = (self.wireSequencesWin.winfo_screenheight() - 700) / 2
        self.wireSequencesWin.geometry("%dx%d+%d+%d" % (1000, 700, self.lftPos, self.topPos))

        self.nameLabel = Label(self.wireSequencesWin, font=("Terminal", 25), fg="white", bg=back,
                               text="ON THE SUBJECT OF WIRE SEQUENCES")
        self.selectLabel = Label(self.wireSequencesWin, font=self.manual_font, fg="white", bg=back)
        self.infoLabel = Label(self.wireSequencesWin, font=self.manual_font, fg="white", bg=back,
                               text="RED WIRE OCURRENCES : 0\n"
                                    "BLUE WIRE OCURRENCES: 0\n"
                                    "BLACK WIRES OCURRENCES: 0")

        self.topButtons = Frame(self.wireSequencesWin, bg=back)
        self.bottomButtons = Frame(self.wireSequencesWin, bg=back)
        self.nameLabel.pack(side=TOP, pady=30)
        self.selectLabel.pack(side=TOP, pady=30)

        self.topButtons.pack()
        self.bottomButtons.pack(pady=10)
        self.infoLabel.pack()

        self.firstButton = Button(self.topButtons, font=self.manual_font)
        self.secondButton = Button(self.topButtons, font=self.manual_font)
        self.thirdButton = Button(self.topButtons, font=self.manual_font)

        self.backButton = Button(self.wireSequencesWin, text="BACK TO\nMODULE SELECT", font=("Terminal", 20),
                                 command=lambda: self.reset(0))
        self.resetButton = Button(self.wireSequencesWin, text="RESET", font=("Terminal", 20),
                                  command=lambda: self.reset(1))

        self.backButton.pack(side=BOTTOM)
        self.wire_stage("FIRST", 0, 0, 0)

    def wire_stage(self, wire, red, blue, black):
        self.selectLabel.config(text="WHAT COLOR IS THE " + wire + " WIRE?")
        self.firstButton.config(text="RED", command=lambda: self.ask_wires("red", "", red + 1, blue, black))
        self.secondButton.config(text="BLUE", command=lambda: self.ask_wires("blue", "", red, blue + 1, black))
        self.thirdButton.config(text="BLACK", command=lambda: self.ask_wires("black", "", red, blue, black + 1))

        self.firstButton.pack(side=LEFT, padx=10)
        self.secondButton.pack(side=LEFT, padx=10)
        self.thirdButton.pack(side=LEFT, padx=10)

    def ask_wires(self, color, letter, red, blue, black):
        self.infoLabel.config(text="RED WIRE OCURRENCES : {}\n"
                                   "BLUE WIRE OCURRENCES: {}\n"
                                   "BLACK WIRES OCURRENCES: {}".format(red, blue, black))
        self.resetButton.place(x=0, y=0)
        if letter == "":
            self.selectLabel.config(text="WHAT IS THAT WIRE CONNECTED TO?")
            self.firstButton.config(text="A", command=lambda: self.ask_wires(color, "A", red, blue, black))
            self.secondButton.config(text="B", command=lambda: self.ask_wires(color, "B", red, blue, black))
            self.thirdButton.config(text="C", command=lambda: self.ask_wires(color, "C", red, blue, black))
        elif color == "red":
            if red == 1 and letter == "C":
                self.cut_wire(True, red, blue, black)
            elif red == 2 and letter == "B":
                self.cut_wire(True, red, blue, black)
            elif red == 3 and letter == "A":
                self.cut_wire(True, red, blue, black)
            elif red == 4 and letter != "B":
                self.cut_wire(True, red, blue, black)
            elif red == 5 and letter == "B":
                self.cut_wire(True, red, blue, black)
            elif red == 6 and letter != "B":
                self.cut_wire(True, red, blue, black)
            elif red == 7:
                self.cut_wire(True, red, blue, black)
            elif red == 8 and letter != "C":
                self.cut_wire(True, red, blue, black)
            elif red == 9 and letter == "B":
                self.cut_wire(True, red, blue, black)
            else:
                self.cut_wire(False, red, blue, black)
        elif color == "blue":
            if blue == 1 and letter == "B":
                self.cut_wire(True, red, blue, black)
            elif blue == 2 and letter != "B":
                self.cut_wire(True, red, blue, black)
            elif blue == 3 and letter == "B":
                self.cut_wire(True, red, blue, black)
            elif blue == 4 and letter == "A":
                self.cut_wire(True, red, blue, black)
            elif blue == 5 and letter == "B":
                self.cut_wire(True, red, blue, black)
            elif blue == 6 and letter != "A":
                self.cut_wire(True, red, blue, black)
            elif blue == 7 and letter == "C":
                self.cut_wire(True, red, blue, black)
            elif blue == 8 and letter != "B":
                self.cut_wire(True, red, blue, black)
            elif blue == 9 and letter == "A":
                self.cut_wire(True, red, blue, black)
            else:
                self.cut_wire(False, red, blue, black)
        elif color == "black":
            if black == 1:
                self.cut_wire(True, red, blue, black)
            elif black == 2 and letter != "B":
                self.cut_wire(True, red, blue, black)
            elif black == 3 and letter == "B":
                self.cut_wire(True, red, blue, black)
            elif black == 4 and letter != "B":
                self.cut_wire(True, red, blue, black)
            elif black == 5 and letter == "B":
                self.cut_wire(True, red, blue, black)
            elif black == 6 and letter != "A":
                self.cut_wire(True, red, blue, black)
            elif black == 7 and letter != "C":
                self.cut_wire(True, red, blue, black)
            elif black == 8 and letter == "C":
                self.cut_wire(True, red, blue, black)
            elif black == 9 and letter == "C":
                self.cut_wire(True, red, blue, black)
            else:
                self.cut_wire(False, red, blue, black)

    def cut_wire(self, cut, red, blue, black):
        self.secondButton.pack_forget()
        self.thirdButton.pack_forget()
        self.firstButton.config(text="NEXT", command=lambda: self.wire_stage("NEXT", red, blue, black))
        if cut:
            self.selectLabel.config(text="CUT THE WIRE")
        else:
            self.selectLabel.config(text="DO NOT CUT THE WIRE")
