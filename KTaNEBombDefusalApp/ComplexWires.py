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
        self.last_serial_even = (int(self.serial[-1]) % 2) == 0
        self.batteries = batteries
        self.parallel = parallel
        self.emptyComplexWires = PhotoImage(file="Images/EmptyComplexWires.png")
        self.complexWiresWin = Toplevel(self.root)
        self.complexWiresWin.title("Complicated Wires")
        self.complexWiresWin.resizable(False, False)
        self.complexWiresWin.config(bg=back)
        self.lftPos = (self.complexWiresWin.winfo_screenwidth() - 1000) / 2
        self.topPos = (self.complexWiresWin.winfo_screenheight() - 700) / 2
        self.complexWiresWin.geometry("%dx%d+%d+%d" % (1000, 700, self.lftPos, self.topPos))

        self.nameLabel = Label(self.complexWiresWin, font=("Terminal", 25), fg="white", bg=back,
                               text="ON THE SUBJECT OF COMPLICATED\n WIRES")
        self.selectLabel = Label(self.complexWiresWin, font=self.manual_font, fg="white", bg=back,
                                 text="SELECT AND ADD ALL THE SPECIFICATIONS OF THE WIRES")
        self.infoLabel = Label(self.complexWiresWin, font=self.manual_font, fg="white", bg=back)

        self.nameLabel.pack(side=TOP, pady=30)
        self.selectLabel.pack(side=TOP, pady=30)

        self.height = self.emptyComplexWires.height()
        self.width = self.emptyComplexWires.width()

        self.mainFrame = Frame(self.complexWiresWin, bg=back)
        self.firstFrame = Frame(self.mainFrame, bg="#a6a6a6")
        self.secondFrame = Frame(self.mainFrame, bg="#a6a6a6")
        self.thirdFrame = Frame(self.mainFrame, bg="#a6a6a6")
        self.fourthFrame = Frame(self.complexWiresWin, bg=back)
        self.canvas = Canvas(self.complexWiresWin, bg=back, highlightthickness=0, height=self.height + 1,
                             width=self.width + 1)
        self.canvas.create_image(self.width / 2, self.height / 2, image=self.emptyComplexWires)

        self.firstFrame.pack(side=LEFT, padx=100)
        self.secondFrame.pack(side=LEFT, ipady=20)
        self.thirdFrame.pack(side=LEFT, padx=100, ipady=20)

        self.red = IntVar()
        self.blue = IntVar()
        self.white = IntVar()
        self.led = IntVar()
        self.star = IntVar()

        self.redWire = Checkbutton(self.firstFrame, text="RED WIRE", fg="red", selectcolor="#a6a6a6", bg="#a6a6a6",
                                   activebackground="#a6a6a6", font=self.manual_font, variable=self.red,
                                   command=lambda: self.wires_check())
        self.blueWire = Checkbutton(self.firstFrame, text="BLUE WIRE", fg="blue", selectcolor="#a6a6a6", bg="#a6a6a6",
                                    activebackground="#a6a6a6", font=self.manual_font, variable=self.blue,
                                    command=lambda: self.wires_check())
        self.whiteWire = Checkbutton(self.firstFrame, text="WHITE WIRE", fg="white", selectcolor="#a6a6a6",
                                     bg="#a6a6a6",
                                     activebackground="#a6a6a6", font=self.manual_font, variable=self.white,
                                     command=lambda: self.wires_check())

        self.ledOn = Radiobutton(self.secondFrame, text="LED ON", fg="white", selectcolor="#a6a6a6", bg="#a6a6a6",
                                 activebackground="#a6a6a6", font=self.manual_font, variable=self.led, value=1)
        self.ledOff = Radiobutton(self.secondFrame, text="LED OFF", fg="white", selectcolor="#a6a6a6", bg="#a6a6a6",
                                  activebackground="#a6a6a6", font=self.manual_font, variable=self.led, value=0)

        self.yesStar = Radiobutton(self.thirdFrame, text="WITH STAR", fg="white", selectcolor="#a6a6a6", bg="#a6a6a6",
                                   activebackground="#a6a6a6", font=self.manual_font, variable=self.star, value=1)
        self.noStar = Radiobutton(self.thirdFrame, text="WITH NO STAR", fg="white", selectcolor="#a6a6a6", bg="#a6a6a6",
                                  activebackground="#a6a6a6", font=self.manual_font, variable=self.star, value=0)

        self.buttons = [self.redWire, self.whiteWire, self.blueWire, self.ledOn, self.ledOff, self.yesStar, self.noStar]

        for i in range(len(self.buttons)):
            self.buttons[i].pack()

        self.clearButton = Button(self.fourthFrame, text="CLEAR", font=("Terminal", 20),
                                  command=lambda: self.add_wires("clear"))
        self.eraseButton = Button(self.fourthFrame, text="ERASE", font=("Terminal", 20),
                                  command=lambda: self.add_wires("erase"))
        self.addButton = Button(self.fourthFrame, text="ADD", font=("Terminal", 20), state=DISABLED,
                                command=lambda: self.add_wires("add"))
        self.nextButton = Button(self.fourthFrame, text="NEXT", font=("Terminal", 20), state=DISABLED,
                                 command=lambda: self.cut_wires())

        self.backButton = Button(self.complexWiresWin, text="BACK TO\nMODULE SELECT", font=("Terminal", 20),
                                 command=lambda: self.reset(0))
        self.resetButton = Button(self.complexWiresWin, text="RESET", font=("Terminal", 20),
                                  command=lambda: self.reset(1))

        self.clearButton.pack(side=LEFT, padx=10)
        self.eraseButton.pack(side=LEFT, padx=10)
        self.addButton.pack(side=LEFT, padx=10)
        self.nextButton.pack(side=LEFT, padx=10)
        self.backButton.pack(side=BOTTOM)
        self.enable_add = True
        self.wires_info = []
        self.cut_wires_list = []
        # Coordinates of the wires, LEDs and stars in the canvas (x0, y0, x1, y1, ...)
        self.draw_wires = [[33, 50, 20, 75, 45, 97, 27, 132, 60, 134, 36, 165],
                           [54, 50, 48, 66, 74, 92, 53, 124, 90, 144, 64, 165],
                           [75, 50, 55, 70, 102, 90, 77, 132, 120, 154, 92, 165],
                           [98, 50, 80, 65, 128, 95, 102, 120, 150, 148, 120, 165],
                           [120, 50, 114, 68, 149, 93, 121, 118, 170, 154, 148, 165],
                           [142, 50, 128, 70, 171, 92, 150, 124, 180, 154, 175, 165]]
        self.draw_LEDs = [[26, 28, 36, 38],
                          [47, 28, 58, 38],
                          [69, 28, 81, 38],
                          [95, 28, 107, 38],
                          [118, 28, 129, 38],
                          [140, 28, 151, 38]]
        self.draw_stars = [[35, 185, 29, 200, 42, 190, 28, 188, 40, 200],
                           [64, 183, 58, 200, 72, 190, 58, 190, 69, 200],
                           [92, 183, 85, 200, 100, 190, 84, 192, 97, 200],
                           [122, 183, 116, 200, 130, 191, 113, 189, 129, 200],
                           [151, 183, 146, 200, 160, 190, 145, 190, 158, 200],
                           [179, 183, 173, 200, 188, 191, 171, 190, 185, 200]]
        self.draw_cut_circles = [[32, 44, 23, 50, 24, 168, 35, 175, 49, 168, 45, 50],
                                 [53, 44, 45, 50, 49, 168, 64, 175, 78, 168, 63, 50],
                                 [74, 44, 63, 50, 78, 167, 92, 175, 106, 168, 87, 50],
                                 [98, 44, 87, 50, 106, 168, 122, 175, 136, 168, 109, 50],
                                 [120, 44, 109, 50, 136, 168, 148, 175, 159, 168, 131, 50],
                                 [142, 44, 131, 50, 159, 158, 175, 175, 186, 168, 150, 50]]

        self.mainFrame.pack()
        self.fourthFrame.pack(pady=10)
        self.canvas.pack(pady=10)

    def wires_check(self):
        if len(self.wires_info) == 6:
            self.enable_add = False
            self.addButton.config(state=DISABLED)
            self.nextButton.config(state=NORMAL)

        else:
            self.enable_add = True
            if (self.red.get() and not self.blue.get()) or (self.blue.get() and not self.white.get()) \
                    or (not self.red.get() and self.white.get()):
                if self.enable_add:
                    self.addButton.config(state=NORMAL)
            else:
                self.addButton.config(state=DISABLED)
            self.nextButton.config(state=DISABLED)

    def cut_circles(self):
        self.resetButton.place(x=0, y=0)
        self.infoLabel.pack()
        self.mainFrame.pack_forget()
        self.fourthFrame.pack_forget()

        self.selectLabel.config(text='CUT ALL THE WIRES CIRCLED IN GREEN')
        cut_list = []
        for cut in range(len(self.cut_wires_list)):
            if self.cut_wires_list[cut]:
                cut_list.append("CUT")
            else:
                cut_list.append("DONT CUT")
        self.infoLabel.config(text='\n'.join(cut_list))

        for circle in range(len(self.cut_wires_list)):
            if self.cut_wires_list[circle]:
                self.canvas.create_polygon(self.draw_cut_circles[circle], outline="lime", fill="", width=2, smooth=1)

    def cut_wires(self):
        for wire in range(6):
            index = [i for i, e in enumerate(self.wires_info[wire][0]) if e == 1]
            if not self.wires_info[wire][1] and not self.wires_info[wire][2]:  # wire w/ no LED-star
                if sum(self.wires_info[wire][0]) == 1 or not (index[0] == 0 and index[1] == 1):  # Only pass if the
                    # wire is 1 color only OR if it is a multicolored w/ white (Red-White or Blue-White)
                    if self.wires_info[wire][0].index(1) == 0:  # Red Wire
                        if self.last_serial_even:
                            self.cut_wires_list.append(True)
                        else:
                            self.cut_wires_list.append(False)

                    elif self.wires_info[wire][0].index(1) == 1:  # Blue Wire
                        if self.last_serial_even:
                            self.cut_wires_list.append(True)
                        else:
                            self.cut_wires_list.append(False)

                    else:  # White Wire
                        self.cut_wires_list.append(True)

                else:  # Only pass if the wire is Red and Blue
                    if self.last_serial_even:
                        self.cut_wires_list.append(True)
                    else:
                        self.cut_wires_list.append(False)

            elif not self.wires_info[wire][1] and self.wires_info[wire][2]:  # Wire w/ no LED and star
                if sum(self.wires_info[wire][0]) == 1 or not (index[0] == 0 and index[1] == 1):  # Only pass if the
                    # wire is 1 color only OR if it is a multicolored w/ white (Red-White or Blue-White)
                    if self.wires_info[wire][0].index(1) == 0:  # Red Wire
                        self.cut_wires_list.append(True)

                    elif self.wires_info[wire][0].index(1) == 1:  # Blue Wire
                        self.cut_wires_list.append(False)

                    else:  # White Wire
                        self.cut_wires_list.append(True)

                else:  # Only pass if the wire is Red and Blue
                    if self.parallel:
                        self.cut_wires_list.append(True)
                    else:
                        self.cut_wires_list.append(False)

            else:  # Wire w/ LED and no star or Wire w/ both LED and star
                if sum(self.wires_info[wire][0]) == 1 or not (index[0] == 0 and index[1] == 1):  # Only pass if the
                    # wire is 1 color only OR if it is a multicolored w/ white (Red-White or Blue-White)
                    if self.wires_info[wire][0].index(1) == 0:  # Red Wire
                        if self.batteries >= 2:
                            self.cut_wires_list.append(True)
                        else:
                            self.cut_wires_list.append(False)

                    elif self.wires_info[wire][0].index(1) == 1:  # Blue Wire
                        if self.parallel:
                            self.cut_wires_list.append(True)
                        else:
                            self.cut_wires_list.append(False)

                    else:  # White Wire
                        if self.wires_info[wire][1] and not self.wires_info[wire][2]:  # Wire w/ LED and no star
                            self.cut_wires_list.append(False)
                        else:  # Wire w/ both LED and star
                            if self.batteries >= 2:
                                self.cut_wires_list.append(True)
                            else:
                                self.cut_wires_list.append(False)

                else:  # Only pass if the wire is Red and Blue
                    if self.wires_info[wire][1] and self.wires_info[wire][2]:  # Wire w/ both LED and star
                        self.cut_wires_list.append(False)
                    else:  # Wire w/ LED and no star
                        if self.last_serial_even:
                            self.cut_wires_list.append(True)
                        else:
                            self.cut_wires_list.append(False)

        self.cut_circles()

    def add_wires(self, command):
        var_list = [[self.red.get(), self.blue.get(), self.white.get()], self.led.get(), self.star.get()]

        if command != "clear" and command != "erase":
            if sum(var_list[0]) == 1:
                if var_list[0].index(1) == 0:
                    color = "red"
                elif var_list[0].index(1) == 1:
                    color = "blue"
                else:
                    color = "white"
                self.canvas.create_line(self.draw_wires[len(self.wires_info)], fill=color, width=4, smooth=1,
                                        tags=("wire {}".format(len(self.wires_info)), "wires"))
            else:
                index = [i for i, e in enumerate(var_list[0]) if e == 1]
                if index[0] == 0 and index[1] == 1:
                    col1 = "red"
                    col2 = "blue"
                elif index[0] == 0 and index[1] == 2:
                    col1 = "red"
                    col2 = "white"
                else:
                    col1 = "blue"
                    col2 = "white"
                self.canvas.create_line(self.draw_wires[len(self.wires_info)], fill=col1, width=4, smooth=1,
                                        tags=("wire {}".format(len(self.wires_info)), "wires"))
                self.canvas.create_line(self.draw_wires[len(self.wires_info)], fill=col2, width=4, dash=(1, 1),
                                        smooth=1,
                                        tags=("wire {}".format(len(self.wires_info)), "wires"))

            if var_list[1]:
                self.canvas.create_oval(self.draw_LEDs[len(self.wires_info)], outline="white", fill="white",
                                        tags=("LED {}".format(len(self.wires_info)), "LEDs"))
            if var_list[2]:
                self.canvas.create_polygon(self.draw_stars[len(self.wires_info)], outline="black", width=1,
                                           tags=("star {}".format(len(self.wires_info)), "stars"))

            self.wires_info.append(var_list)
        elif command == "erase":
            self.wires_info = self.wires_info[:-1]
            self.canvas.delete("wire {}".format(len(self.wires_info)))
            self.canvas.delete("LED {}".format(len(self.wires_info)))
            self.canvas.delete("star {}".format(len(self.wires_info)))
        else:
            self.canvas.delete("wires")
            self.canvas.delete("LEDs")
            self.canvas.delete("stars")
            self.wires_info.clear()

        self.wires_check()
