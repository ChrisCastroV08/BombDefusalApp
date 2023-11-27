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
                               text="RED WIRE OCCURRENCES : 0\n"
                                    "BLUE WIRE OCCURRENCES: 0\n"
                                    "BLACK WIRES OCCURRENCES: 0")

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
        self.fourthButton = Button(self.bottomButtons, font=self.manual_font, text="BACK")

        self.backButton = Button(self.wireSequencesWin, text="BACK TO\nMODULE SELECT", font=("Terminal", 20),
                                 command=lambda: self.reset(0))
        self.resetButton = Button(self.wireSequencesWin, text="RESET", font=("Terminal", 20),
                                  command=lambda: self.reset(1))
        self.red = -1
        self.blue = -1
        self.black = -1
        self.occurrences = [
            [[False, False, True],
             [False, True, False],
             [True, False, False],
             [True, False, True],
             [False, True, False],
             [True, False, True],
             [True, True, True],
             [True, True, False],
             [False, True, False]],

            [[False, True, False],
             [True, False, True],
             [False, True, False],
             [True, False, False],
             [False, True, False],
             [False, True, True],
             [False, False, True],
             [True, False, True],
             [True, False, False]],

            [[True, True, True],
             [True, False, True],
             [False, True, False],
             [True, False, True],
             [False, True, False],
             [False, True, True],
             [True, True, False],
             [False, False, True],
             [False, False, True]]
        ]

        self.backButton.pack(side=BOTTOM)
        self.ask_wires("FIRST", "", "")

    def ask_wires(self, wire, color, letter):
        if letter == "BACK":
            if color == "red":
                self.red -= 1
            elif color == "blue":
                self.blue -= 1
            else:
                self.black -= 1
            self.infoLabel.config(text="RED WIRE OCCURRENCES : {}\n"
                                       "BLUE WIRE OCCURRENCES: {}\n"
                                       "BLACK WIRES OCCURRENCES: {}".format(self.red + 1,
                                                                            self.blue + 1,
                                                                            self.black + 1))
            self.ask_wires(wire, "", "")

        elif wire == "CUT":
            self.secondButton.pack_forget()
            self.thirdButton.pack_forget()
            self.fourthButton.pack_forget()
            self.firstButton.config(text="NEXT", fg="black", command=lambda: self.ask_wires("NEXT", "", ""))
            if color:
                self.selectLabel.config(text="CUT THE WIRE")
            else:
                self.selectLabel.config(text="DO NOT CUT THE WIRE")

        elif color == "":
            self.selectLabel.config(text="WHAT COLOR IS THE " + wire + " WIRE?")
            self.firstButton.config(text="RED", fg="red",
                                    command=lambda: self.ask_wires(wire, "red", ""))
            self.secondButton.config(text="BLUE", fg="blue",
                                     command=lambda: self.ask_wires(wire, "blue", "", ))
            self.thirdButton.config(text="BLACK", fg="black",
                                    command=lambda: self.ask_wires(wire, "black", ""))

            self.firstButton.pack(side=LEFT, padx=10)
            self.secondButton.pack(side=LEFT, padx=10)
            self.thirdButton.pack(side=LEFT, padx=10)
            self.fourthButton.pack_forget()

        elif letter == "":
            if color == "red":
                self.red += 1
            elif color == "blue":
                self.blue += 1
            else:
                self.black += 1
            if wire == "FIRST":
                self.resetButton.place(x=0, y=0)
            self.infoLabel.config(text="RED WIRE OCCURRENCES : {}\n"
                                       "BLUE WIRE OCCURRENCES: {}\n"
                                       "BLACK WIRES OCCURRENCES: {}".format(self.red + 1,
                                                                            self.blue + 1,
                                                                            self.black + 1))
            self.selectLabel.config(text="WHAT IS THAT WIRE CONNECTED TO?")
            self.firstButton.config(text="A", fg=color, command=lambda: self.ask_wires(wire, color, 0))
            self.secondButton.config(text="B", fg=color,
                                     command=lambda: self.ask_wires(wire, color, 1))
            self.thirdButton.config(text="C", fg=color, command=lambda: self.ask_wires(wire, color, 2))
            self.fourthButton.config(command=lambda: self.ask_wires(wire, color, "BACK"))
            self.fourthButton.pack()

        else:
            if color == "red":
                col_selected = 0
                self.ask_wires("CUT", self.occurrences[col_selected][self.red][letter], letter)
            elif color == "blue":
                col_selected = 1
                self.ask_wires("CUT", self.occurrences[col_selected][self.blue][letter], letter)
            else:
                col_selected = 2
                self.ask_wires("CUT", self.occurrences[col_selected][self.black][letter], letter)
