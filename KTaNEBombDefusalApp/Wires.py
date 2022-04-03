from tkinter import *
from tkinter.font import Font


class Wires:

    def reset(self, num):
        if num == 0:
            self.wiresWin.destroy()
        elif num == 1:
            self.wiresWin.destroy()
            self.__init__(self.root, self.back)

    def __init__(self, root, back):
        self.root = root
        self.back = back
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
                                 text="HOW MANY WIRES ARE THERE?")
        self.topButtons = Frame(self.wiresWin, bg=back)
        self.bottomButtons = Frame(self.wiresWin, bg=back)
        self.nameLabel.pack(side=TOP, pady=30)
        self.selectLabel.pack(side=TOP, pady=30)

        self.topButtons.pack()
        self.bottomButtons.pack(pady=10)

        self.firstButton = Button(self.topButtons)
        self.secondButton = Button(self.topButtons)
        self.thirdButton = Button(self.bottomButtons)
        self.fourthButton = Button(self.bottomButtons)

        self.firstButton.pack(side=LEFT, padx=10)
        self.secondButton.pack(side=LEFT, padx=10)
        self.thirdButton.pack(side=LEFT, padx=10)
        self.fourthButton.pack(side=LEFT, padx=10)

        self.backButton = Button(self.wiresWin, text="BACK TO\nMODULE SELECT", font=("Terminal", 20),
                                 command=lambda: self.reset(0))
        self.resetButton = Button(self.wiresWin, text="RESET", font=("Terminal", 20),
                                  command=lambda: self.reset(1))

        self.backButton.pack(side=BOTTOM)

        self.wires_com(0)

    def wires_com(self, num_wires):
        manual_font = Font(
            family="Terminal",
            size=20)
        if num_wires == 0:
            self.selectLabel.config(text="HOW MANY WIRES ARE THERE?")
            self.thirdButton.pack(side=LEFT, padx=10)
            self.fourthButton.pack(side=LEFT, padx=10)
            self.firstButton.config(text="3 WIRES", font=manual_font, command=lambda: self.wires_com(3))
            self.secondButton.config(text="4 WIRES", font=manual_font, command=lambda: self.wires_com(4))
            self.thirdButton.config(text="5 WIRES", font=manual_font, command=lambda: self.wires_com(5))
            self.fourthButton.config(text="6 WIRES", font=manual_font, command=lambda: self.wires_com(6))

        else:
            self.resetButton.place(x=0, y=0)
            self.thirdButton.pack_forget()
            self.fourthButton.pack_forget()
            if num_wires == 3 or num_wires == 4:
                self.selectLabel.config(text="ARE THERE ANY RED WIRES?")
                self.firstButton.config(image='', text="YES", font=manual_font,
                                        command=lambda: self.yes_no_wires(True, num_wires, 1))
                if num_wires == 3:
                    self.secondButton.config(image='', text="NO", font=manual_font,
                                             command=lambda: self.cut_wire("SECOND"))
                if num_wires == 4:
                    self.secondButton.config(image='', text="NO", font=manual_font,
                                             command=lambda: self.yes_no_wires(False, num_wires, 1))
            elif num_wires == 5:
                self.selectLabel.config(text="IS THE LAST WIRE BLACK?")
                self.firstButton.config(image='', text="YES", font=manual_font,
                                        command=lambda: self.yes_no_wires(True, num_wires, 1))
                self.secondButton.config(image='', text="NO", font=manual_font,
                                         command=lambda: self.yes_no_wires(False, num_wires, 1))
            elif num_wires == 6:
                self.selectLabel.config(text="ARE THERE ANY YELLOW WIRES?")
                self.firstButton.config(image='', text="YES", font=manual_font,
                                        command=lambda: self.yes_no_wires(True, num_wires, 1))
                self.secondButton.config(image='', text="NO", font=manual_font,
                                         command=lambda: self.yes_no_wires(False, num_wires, 1))

    def yes_no_wires(self, answer, wires, num):
        if answer:
            # THREE WIRES
            if wires == 3:
                if num == 1:
                    self.selectLabel.config(text="IS THE LAST WIRE WHITE?")
                    self.firstButton.config(command=lambda: self.cut_wire("LAST"))
                    self.secondButton.config(command=lambda: self.yes_no_wires(False, 3, 1))

                elif num == 2:
                    self.selectLabel.config(text="IS THERE MORE THAN 1 BLUE WIRE?")
                    self.firstButton.config(command=lambda: self.cut_wire("LAST BLUE"))
                    self.secondButton.config(command=lambda: self.cut_wire("LAST"))

            # FOUR WIRES
            elif wires == 4:
                if num == 1:
                    self.selectLabel.config(text="IS THERE MORE THAN 1 RED WIRE?")
                    self.firstButton.config(command=lambda: self.yes_no_wires(True, 4, num + 1))
                    self.secondButton.config(command=lambda: self.yes_no_wires(False, 4, num + 1))

                elif num == 2:
                    self.selectLabel.config(text="IS THE LAST DIGIT OF THE SERIAL NUMBER ODD?")
                    self.firstButton.config(command=lambda: self.cut_wire("LAST RED"))
                    self.secondButton.config(command=lambda: self.yes_no_wires(False, 4, num))

            # FIVE WIRES
            elif wires == 5:
                if num == 1:
                    self.selectLabel.config(text="IS THE LAST DIGIT OF THE SERIAL NUMBER ODD?")
                    self.firstButton.config(command=lambda: self.cut_wire("FOURTH"))
                    self.secondButton.config(command=lambda: self.yes_no_wires(False, 5, 1))
                if num == 2:
                    self.selectLabel.config(text="IS THERE MORE THAN 1 YELLOW WIRE?")
                    self.firstButton.config(command=lambda: self.cut_wire("FIRST"))
                    self.secondButton.config(command=lambda: self.yes_no_wires(False, 5, 2))

            # SIX WIRES
            elif wires == 6:
                if num == 1:
                    self.selectLabel.config(text="IS THERE EXACTLY ONE YELLOW WIRE?")
                    self.firstButton.config(command=lambda: self.yes_no_wires(True, 6, 2))
                    self.secondButton.config(command=lambda: self.yes_no_wires(False, 6, 2))

                elif num == 2:
                    self.selectLabel.config(text="IS THERE MORE THAN 1 WHITE WIRE?")
                    self.firstButton.config(command=lambda: self.cut_wire("FOURTH"))
                    self.secondButton.config(command=lambda: self.yes_no_wires(False, 6, 2))

        elif not answer:
            # THREE WIRES
            if wires == 3:
                if num == 1:
                    self.selectLabel.config(text="ARE THERE ANY BLUE WIRES?")
                    self.firstButton.config(command=lambda: self.yes_no_wires(True, 3, 2))
                    self.secondButton.config(command=lambda: self.cut_wire("LAST"))

            # FOUR WIRES
            elif wires == 4:
                if num == 1:
                    self.selectLabel.config(text="IS THE LAST WIRE YELLOW?")
                    self.firstButton.config(command=lambda: self.cut_wire("FIRST"))
                    self.secondButton.config(command=lambda: self.yes_no_wires(False, 4, 2))
                elif num == 2:
                    self.selectLabel.config(text="IS THERE EXACTLY 1 BLUE WIRE?")
                    self.firstButton.config(command=lambda: self.cut_wire("FIRST"))
                    self.secondButton.config(command=lambda: self.yes_no_wires(False, 4, 3))
                elif num == 3:
                    self.selectLabel.config(text="IS THERE MORE THAN 1 YELLOW WIRE?")
                    self.firstButton.config(command=lambda: self.cut_wire("LAST"))
                    self.secondButton.config(command=lambda: self.cut_wire("SECOND"))

            # FIVE WIRES
            elif wires == 5:
                if num == 1:
                    self.selectLabel.config(text="IS THERE EXACTLY ONE RED WIRE?")
                    self.firstButton.config(command=lambda: self.yes_no_wires(True, 5, 2))
                    self.secondButton.config(command=lambda: self.yes_no_wires(False, 5, 2))
                elif num == 2:
                    self.selectLabel.config(text="ARE THERE ANY BLACK WIRES?")
                    self.firstButton.config(command=lambda: self.cut_wire("FIRST"))
                    self.secondButton.config(command=lambda: self.cut_wire("SECOND"))

            # SIX WIRES
            elif wires == 6:
                if num == 1:
                    self.selectLabel.config(text="IS THE LAST DIGIT OF THE SERIAL NUMBER ODD?")
                    self.firstButton.config(command=lambda: self.cut_wire("THIRD"))
                    self.secondButton.config(command=lambda: self.yes_no_wires(False, 6, 2))

                if num == 2:
                    self.selectLabel.config(text="ARE THERE ANY RED WIRES?")
                    self.firstButton.config(command=lambda: self.cut_wire("FOURTH"))
                    self.secondButton.config(command=lambda: self.cut_wire("LAST"))

    def cut_wire(self, string):
        self.topButtons.pack_forget()
        self.bottomButtons.pack_forget()
        self.selectLabel.config(text="CUT THE " + string + " WIRE")
