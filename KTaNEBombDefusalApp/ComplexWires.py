from tkinter import *


class ComplexWires:

    def reset(self, num):
        if num == 0:
            self.complexWiresWin.destroy()
        elif num == 1:
            self.complexWiresWin.destroy()
            self.__init__(self.root, self.back, self.manual_font)

    def __init__(self, root, back, font):
        self.root = root
        self.back = back
        self.manual_font = font
        self.complexWiresWin = Toplevel(self.root)
        self.complexWiresWin.title("Complicated Wires")
        self.complexWiresWin.resizable(False, False)
        self.complexWiresWin.config(bg=back)
        self.lftPos = (self.complexWiresWin.winfo_screenwidth() - 1000) / 2
        self.topPos = (self.complexWiresWin.winfo_screenheight() - 700) / 2
        self.complexWiresWin.geometry("%dx%d+%d+%d" % (1000, 700, self.lftPos, self.topPos))

        self.nameLabel = Label(self.complexWiresWin, font=("Terminal", 25), fg="white", bg=back,
                               text="ON THE SUBJECT OF COMPLICATED\n WIRES")
        self.selectLabel = Label(self.complexWiresWin, font=self.manual_font, fg="white", bg=back)
        self.topButtons = Frame(self.complexWiresWin, bg=back)
        self.bottomButtons = Frame(self.complexWiresWin, bg=back)
        self.nameLabel.pack(side=TOP, pady=30)
        self.selectLabel.pack(side=TOP, pady=30)

        self.topButtons.pack()
        self.bottomButtons.pack(pady=10)

        self.firstButton = Button(self.topButtons, font=self.manual_font)
        self.secondButton = Button(self.topButtons, font=self.manual_font)
        self.thirdButton = Button(self.bottomButtons, font=self.manual_font)
        self.fourthButton = Button(self.bottomButtons, font=self.manual_font)

        self.backButton = Button(self.complexWiresWin, text="BACK TO\nMODULE SELECT", font=("Terminal", 20),
                                 command=lambda: self.reset(0))
        self.resetButton = Button(self.complexWiresWin, text="RESET", font=("Terminal", 20),
                                  command=lambda: self.reset(1))

        self.backButton.pack(side=BOTTOM)
        self.wire_info("", -1, -1)

    def wire_info(self, color, led, star):
        self.firstButton.pack(side=LEFT, padx=10)
        self.secondButton.pack(side=LEFT, padx=10)
        self.thirdButton.pack(side=LEFT, padx=10)
        self.fourthButton.pack(side=LEFT, padx=10)

        if color == "":
            self.selectLabel.config(text="DOES THE WIRE HAVE ANY OF THESE COLORINGS?")
            self.firstButton.config(image='', text="BLUE COLORING", font=self.manual_font,
                                    command=lambda: self.wire_info("b", led, star))
            self.secondButton.config(image='', text="RED COLORING", font=self.manual_font,
                                     command=lambda: self.wire_info("r", led, star))
            self.thirdButton.config(image='', text="BLUE AND RED\nCOLORING", font=self.manual_font,
                                    command=lambda: self.wire_info("br", led, star))
            self.fourthButton.config(image='', text="OTHER", font=self.manual_font,
                                     command=lambda: self.wire_info("o", led, star))
        elif led == -1:
            self.resetButton.place(x=0, y=0)
            self.selectLabel.config(text="WHAT IS THE STATE OF THE LED\nON TOP OF THE WIRE?")
            self.fourthButton.pack_forget()
            self.thirdButton.pack_forget()
            self.firstButton.config(image='', text="ON", font=self.manual_font,
                                    command=lambda: self.wire_info(color, True, star))
            self.secondButton.config(image='', text="OFF", font=self.manual_font,
                                     command=lambda: self.wire_info(color, False, star))
        elif star == -1:
            self.selectLabel.config(text="IS THERE A STAR ON THE\nBOTTOM OF THE WIRE?")
            self.fourthButton.pack_forget()
            self.thirdButton.pack_forget()
            self.firstButton.config(image='', text="YES", font=self.manual_font,
                                    command=lambda: self.wire_info(color, led, True))
            self.secondButton.config(image='', text="NO", font=self.manual_font,
                                     command=lambda: self.wire_info(color, led, False))
        else:
            self.ask_wires(color, led, star)

    def cut_wire(self, cut):
        self.secondButton.pack_forget()
        self.thirdButton.pack_forget()
        self.fourthButton.pack_forget()
        self.firstButton.config(text="NEXT", command=lambda: self.wire_info("", -1, -1))
        if cut:
            self.selectLabel.config(text="CUT THE WIRE")
        else:
            self.selectLabel.config(text="DO NOT CUT THE WIRE")

    def ask_batteries(self):
        self.firstButton.pack(side=LEFT, padx=10)
        self.secondButton.pack(side=LEFT, padx=10)
        self.thirdButton.pack(side=LEFT, padx=10)
        self.fourthButton.pack_forget()

        self.selectLabel.config(text="HOW MANY BATTERIES ARE IN THE BOMB?")
        self.firstButton.config(text="NONE", font=self.manual_font,
                                command=lambda: self.cut_wire(False))
        self.secondButton.config(text="1 BATTERY", font=self.manual_font,
                                 command=lambda: self.cut_wire(False))
        self.thirdButton.config(text="2 OR MORE BATTERIES", font=self.manual_font,
                                command=lambda: self.cut_wire(True))

    def ask_serial(self):
        self.firstButton.pack(side=LEFT, padx=10)
        self.secondButton.pack(side=LEFT, padx=10)
        self.thirdButton.pack_forget()
        self.fourthButton.pack_forget()

        self.selectLabel.config(text="IS THE SERIAL NUMBER ODD OR EVEN?")
        self.firstButton.config(text="ODD", font=self.manual_font,
                                command=lambda: self.cut_wire(False))
        self.secondButton.config(text="EVEN", font=self.manual_font,
                                 command=lambda: self.cut_wire(True))

    def ask_parallel(self):
        self.firstButton.pack(side=LEFT, padx=10)
        self.secondButton.pack(side=LEFT, padx=10)
        self.thirdButton.pack_forget()
        self.fourthButton.pack_forget()

        self.selectLabel.config(text="DOES THE BOMB HAS A PARALLEL PORT?")
        self.firstButton.config(text="YES", font=self.manual_font,
                                command=lambda: self.cut_wire(True))
        self.secondButton.config(text="NO", font=self.manual_font,
                                 command=lambda: self.cut_wire(False))

    def ask_wires(self, color, led, star):
        if color == "o":
            if not led and not star or star and not led:
                self.cut_wire(True)
            elif star and led:
                self.ask_batteries()
            elif not star and led:
                self.cut_wire(False)
        elif color == "r":
            if not led and not star:
                self.ask_serial()
            elif not led and star:
                self.cut_wire(True)
            elif led and not star or led and star:
                self.ask_batteries()
        elif color == "b":
            if not led and not star:
                self.ask_serial()
            elif not led and star:
                self.cut_wire(False)
            elif led and not star or led and star:
                self.ask_parallel()
        elif color == "br":
            if not led and not star or led and not star:
                self.ask_serial()
            elif not led and star:
                self.ask_parallel()
            elif led and star:
                self.cut_wire(False)
