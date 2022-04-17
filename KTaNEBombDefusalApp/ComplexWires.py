from tkinter import *


class ComplexWires:

    def reset(self, num):
        if num == 0:
            self.complexWiresWin.destroy()
        elif num == 1:
            self.complexWiresWin.destroy()
            self.__init__(self.root, self.back, self.manual_font, self.serial, self.batteries, self.parallel)

    def __init__(self, root, back, manual_font, serial, batteries, parallel):
        self.root = root
        self.back = back
        self.manual_font = manual_font
        self.serial = serial
        self.batteries = batteries
        self.parallel = parallel
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
        self.nameLabel.pack(side=TOP, pady=30)
        self.selectLabel.pack(side=TOP, pady=30)

        self.mainFrame = Frame(self.complexWiresWin, bg=back)
        self.firstFrame = Frame(self.mainFrame, bg=back)
        self.secondFrame = Frame(self.mainFrame, bg=back)
        self.thirdFrame = Frame(self.mainFrame, bg=back)

        self.topButtons = Frame(self.complexWiresWin, bg=back)
        self.bottomButtons = Frame(self.complexWiresWin, bg=back)

        self.firstButton = Button(self.topButtons, font=self.manual_font)
        self.secondButton = Button(self.topButtons, font=self.manual_font)
        self.thirdButton = Button(self.bottomButtons, font=self.manual_font)

        self.red = IntVar()
        self.blue = IntVar()
        self.white = IntVar()
        self.led = IntVar()
        self.star = IntVar()

        self.redWire = Checkbutton(self.firstFrame, text="RED WIRE", fg="white", selectcolor=back, bg=self.back,
                                   activebackground=back, font=self.manual_font, variable=self.red,
                                   command=lambda: self.wire_info())
        self.blueWire = Checkbutton(self.firstFrame, text="BLUE WIRE", fg="white", selectcolor=back, bg=back,
                                    activebackground=back, font=self.manual_font, variable=self.blue,
                                    command=lambda: self.wire_info())
        self.whiteWire = Checkbutton(self.firstFrame, text="WHITE WIRE", fg="white", selectcolor=back, bg=back,
                                     activebackground=back, font=self.manual_font, variable=self.white,
                                     command=lambda: self.wire_info())

        self.ledOn = Radiobutton(self.secondFrame, text="LED ON", fg="white", selectcolor=back, bg=self.back,
                                 activebackground=back, font=self.manual_font, variable=self.led, value=1)
        self.ledOff = Radiobutton(self.secondFrame, text="LED OFF", fg="white", selectcolor=back, bg=self.back,
                                  activebackground=back, font=self.manual_font, variable=self.led, value=0)

        self.yesStar = Radiobutton(self.thirdFrame, text="WITH STAR", fg="white", selectcolor=back, bg=self.back,
                                   activebackground=back, font=self.manual_font, variable=self.star, value=1)
        self.noStar = Radiobutton(self.thirdFrame, text="WITH NO STAR", fg="white", selectcolor=back, bg=self.back,
                                  activebackground=back, font=self.manual_font, variable=self.star, value=0)

        self.buttons = [self.redWire, self.blueWire, self.whiteWire, self.ledOn, self.ledOff, self.yesStar, self.noStar]

        for i in range(len(self.buttons)):
            self.buttons[i].pack()

        self.nextButton = Button(self.complexWiresWin, text="NEXT", font=("Terminal", 20),
                                 command=lambda: self.ask_wires())
        self.backButton = Button(self.complexWiresWin, text="BACK TO\nMODULE SELECT", font=("Terminal", 20),
                                 command=lambda: self.reset(0))
        self.resetButton = Button(self.complexWiresWin, text="RESET", font=("Terminal", 20),
                                  command=lambda: self.reset(1))

        self.backButton.pack(side=BOTTOM)
        self.wire_info()

    def wire_info(self):
        self.selectLabel.config(text="SELECT ALL THE SPECIFICATIONS OF THE WIRE")
        self.topButtons.pack_forget()
        self.bottomButtons.pack_forget()
        self.mainFrame.pack()
        self.firstFrame.pack(side=LEFT, padx=100, ipady=120)
        self.secondFrame.pack(side=LEFT, ipady=140)
        self.thirdFrame.pack(side=LEFT, padx=100, ipady=140)

        self.nextButton.place(x=450, y=350)

        if self.white.get() or self.red.get() or self.blue.get():
            self.nextButton.config(state=NORMAL)
        else:
            self.nextButton.config(state=DISABLED)

    def ask_wires(self):
        self.mainFrame.pack_forget()
        self.nextButton.place_forget()
        self.resetButton.place(x=0, y=0)
        if self.white.get() and not self.red.get() and not self.blue.get():
            if (not self.led.get() and not self.star.get()) or (self.star.get() and not self.led.get()):
                self.cut_wire(True)
            elif self.star.get() and self.led.get():
                if self.batteries >= 2:
                    self.cut_wire(True)
                else:
                    self.cut_wire(False)
            elif not self.star.get() and self.led.get():
                self.cut_wire(False)

        elif self.red.get() and not self.blue.get():
            if not self.led.get() and not self.star.get():
                if (int(self.serial[-1]) % 2) == 0:
                    self.cut_wire(True)
                else:
                    self.cut_wire(False)

            elif not self.led.get() and self.star.get():
                self.cut_wire(True)
            elif (self.led.get() and not self.star.get()) or (self.led.get() and self.star.get()):
                if self.batteries >= 2:
                    self.cut_wire(True)
                else:
                    self.cut_wire(False)

        elif self.blue.get() and not self.red.get():
            if not self.led.get() and not self.star.get():
                if (int(self.serial[-1]) % 2) == 0:
                    self.cut_wire(True)
                else:
                    self.cut_wire(False)
            elif not self.led.get() and self.star.get():
                self.cut_wire(False)
            elif (self.led.get() and not self.star.get()) or (self.led and self.star.get()):
                if self.parallel:
                    self.cut_wire(True)
                else:
                    self.cut_wire(False)

        elif self.blue.get() and self.red.get():
            if not self.led.get() and self.star.get():
                if self.parallel:
                    self.cut_wire(True)
                else:
                    self.cut_wire(False)
            elif self.led.get() and self.star.get():
                self.cut_wire(False)
            elif (not self.led.get() and not self.star.get()) or (self.led.get() and not self.star.get()):
                if (int(self.serial[-1]) % 2) == 0:
                    self.cut_wire(True)
                else:
                    self.cut_wire(False)

    def cut_wire(self, cut):
        self.firstFrame.pack_forget()
        self.secondFrame.pack_forget()
        self.thirdFrame.pack_forget()

        self.topButtons.pack()
        self.bottomButtons.pack_forget()
        self.secondButton.pack_forget()
        self.firstButton.pack(side=LEFT, padx=10)
        self.firstButton.config(text="NEXT", command=lambda: self.wire_info())

        for i in range(0, 3):
            self.buttons[i].deselect()
        if cut:
            self.selectLabel.config(text="CUT THE WIRE")
        else:
            self.selectLabel.config(text="DO NOT CUT THE WIRE")
