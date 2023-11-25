from tkinter import *


class Wires:

    def reset(self, num):
        if num == 0:
            self.wiresWin.destroy()
        elif num == 1:
            self.wiresWin.destroy()
            self.__init__(self.root, self.back, self.manual_font, self.serial)

    def __init__(self, root, back, font, serial):
        self.root = root
        self.back = back
        self.emptyWires = PhotoImage(file="Images/EmptyWires.png")
        self.manual_font = font
        self.serial = serial
        self.wiresWin = Toplevel(self.root)
        self.wiresWin.title("Wires")
        self.wiresWin.resizable(False, False)
        self.wiresWin.config(bg=back)
        self.lftPos = (self.wiresWin.winfo_screenwidth() - 1000) / 2
        self.topPos = (self.wiresWin.winfo_screenheight() - 700) / 2
        self.wiresWin.geometry("%dx%d+%d+%d" % (1000, 700, self.lftPos, self.topPos))

        self.nameLabel = Label(self.wiresWin, font=("Terminal", 25), fg="white", bg=back,
                               text="ON THE SUBJECT OF WIRES")
        self.selectLabel = Label(self.wiresWin, font=("Terminal", 20), fg="white", bg=back,
                                 text="SELECT THE COLOR ORDER " + "FROM TOP TO BOTTOM OF THE WIRES")

        self.height = self.emptyWires.height()
        self.width = self.emptyWires.width()

        self.topButtons = Frame(self.wiresWin, bg=back)
        self.bottomButtons = Frame(self.wiresWin, bg=back)
        self.bottomButtons2 = Frame(self.wiresWin, bg=back)
        self.canvas = Canvas(self.wiresWin, bg=back, highlightthickness=0, height=self.height + 1,
                             width=self.width + 1)
        self.canvas.create_image(self.width / 2, self.height / 2, image=self.emptyWires)
        self.cutLabel = Label(self.wiresWin, font=("Terminal", 20), fg="white", bg=back)

        self.nameLabel.pack(side=TOP, pady=30)
        self.selectLabel.pack(side=TOP, pady=30)
        self.topButtons.pack()
        self.bottomButtons.pack(pady=10)
        self.bottomButtons2.pack(pady=10)
        self.canvas.pack(pady=10)
        self.cutLabel.pack(pady=10)

        self.firstButton = Button(self.topButtons, font=self.manual_font,
                                  text="YELLOW", command=lambda: self.place_wires("yellow"), fg="#cca002")
        self.secondButton = Button(self.topButtons, font=self.manual_font,
                                   text="RED", command=lambda: self.place_wires("red"), fg="red")
        self.thirdButton = Button(self.bottomButtons, font=self.manual_font,
                                  text="BLUE", command=lambda: self.place_wires("blue"), fg="blue")
        self.fourthButton = Button(self.bottomButtons, font=self.manual_font,
                                   text="BLACK", command=lambda: self.place_wires("black"))
        self.fifthButton = Button(self.bottomButtons, font=self.manual_font,
                                  text="WHITE", command=lambda: self.place_wires("white"), fg="white", bg="#a6a6a6")

        self.sixthButton = Button(self.bottomButtons2, font=self.manual_font,
                                  text="CLEAR", command=lambda: self.place_wires("clear"))
        self.seventhButton = Button(self.bottomButtons2, font=self.manual_font,
                                    text="ERASE", command=lambda: self.place_wires("erase"))
        self.eightButton = Button(self.bottomButtons2, font=self.manual_font,
                                  text="NEXT", command=lambda: self.check_wires(), state=DISABLED)

        self.firstButton.pack(side=LEFT, padx=10)
        self.secondButton.pack(side=LEFT, padx=10)
        self.thirdButton.pack(side=LEFT, padx=10)
        self.fourthButton.pack(side=LEFT, padx=10)
        self.fifthButton.pack(side=LEFT, padx=10)
        self.sixthButton.pack(side=LEFT, padx=10)
        self.seventhButton.pack(side=LEFT, padx=10)
        self.eightButton.pack(side=LEFT, padx=10)

        self.backButton = Button(self.wiresWin, text="BACK TO\nMODULE SELECT", font=("Terminal", 20),
                                 command=lambda: self.reset(0))
        self.resetButton = Button(self.wiresWin, text="RESET", font=("Terminal", 20),
                                  command=lambda: self.reset(1))

        self.backButton.pack(side=BOTTOM)
        # Coordinates of the wires in the canvas (x0, y0, x1, y1, ...)
        self.draw_wires = [[38, 30, 75, 20, 97, 65, 132, 47, 154, 80, 188, 75],
                           [38, 63, 66, 48, 92, 94, 124, 73, 144, 110, 188, 100],
                           [38, 95, 70, 75, 90, 122, 132, 97, 154, 140, 188, 123],
                           [38, 127, 65, 100, 95, 148, 120, 122, 148, 170, 188, 148],
                           [38, 158, 68, 134, 93, 169, 118, 141, 154, 190, 188, 171],
                           [38, 192, 70, 168, 92, 201, 124, 170, 154, 200, 188, 196]]
        self.wire_list = []

    def place_wires(self, string):
        self.resetButton.place(x=0, y=0)
        if string != "clear" and string != "erase":
            self.canvas.create_line(self.draw_wires[len(self.wire_list)], fill=string, width=4, smooth=1,
                                    tags=("wire {}".format(len(self.wire_list)), "wires"))
            self.wire_list.append(string)

        elif string == "erase":
            self.wire_list = self.wire_list[:-1]
            self.canvas.delete("wire {}".format(len(self.wire_list)))

        else:
            self.canvas.delete("wires")
            self.wire_list.clear()

        if len(self.wire_list) < 3:
            self.eightButton.config(state=DISABLED)
        else:
            self.eightButton.config(state=NORMAL)

        if len(self.wire_list) == 6:
            self.firstButton.config(state=DISABLED)
            self.secondButton.config(state=DISABLED)
            self.thirdButton.config(state=DISABLED)
            self.fourthButton.config(state=DISABLED)
            self.fifthButton.config(state=DISABLED)
        else:
            self.firstButton.config(state=NORMAL)
            self.secondButton.config(state=NORMAL)
            self.thirdButton.config(state=NORMAL)
            self.fourthButton.config(state=NORMAL)
            self.fifthButton.config(state=NORMAL)

    def cut_wire(self, wire):
        self.topButtons.pack_forget()
        self.bottomButtons.pack_forget()
        self.bottomButtons2.pack_forget()
        self.cutLabel.config(text="CUT THE {} WIRE".format(wire))

    def check_wires(self):
        wires = len(self.wire_list)
        if wires == 3:
            if "red" not in self.wire_list:
                self.cut_wire("SECOND")
            elif self.wire_list[-1] == "white" or self.wire_list.count("blue") <= 1:
                self.cut_wire("LAST")
            else:
                self.cut_wire("LAST BLUE")

        elif wires == 4:
            if self.wire_list.count("red") >= 2 and (int(self.serial[-1]) % 2) != 0:
                self.cut_wire("LAST RED")
            elif self.wire_list[-1] == "yellow" and "red" not in self.wire_list \
                    or self.wire_list.count("blue") == 1 and self.wire_list.count("blue") == 1 \
                    or self.wire_list.count("blue") == 1:
                self.cut_wire("FIRST")
            elif self.wire_list.count("yellow") >= 2 and self.wire_list.count("blue") != 1:
                self.cut_wire("LAST")
            else:
                self.cut_wire("SECOND")

        elif wires == 5:
            if self.wire_list[-1] == "black" and (int(self.serial[-1]) % 2) != 0:
                self.cut_wire("FOURTH")
            elif self.wire_list.count("red") == 1 and self.wire_list.count("yellow") >= 2 \
                    or (int(self.serial[-1]) % 2) == 0 or self.wire_list.count("black") >= 1:
                self.cut_wire("FIRST")
            elif "black" not in self.wire_list:
                self.cut_wire("SECOND")

        else:
            if "yellow" not in self.wire_list and (int(self.serial[-1]) % 2) != 0:
                self.cut_wire("THIRD")
            elif self.wire_list.count("yellow") == 1 and self.wire_list.count("white") >= 2 \
                    or self.wire_list.count("red") >= 1 and self.wire_list.count("yellow") >= 2 \
                    or self.wire_list.count("white") >= 1 and self.wire_list.count("red") >= 1:
                self.cut_wire("FOURTH")
            else:
                self.cut_wire("LAST")
