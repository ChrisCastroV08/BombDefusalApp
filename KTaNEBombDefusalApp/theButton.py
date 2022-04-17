from tkinter import *


class TheButton:

    def reset(self, num):
        if num == 0:
            self.theButtonWind.destroy()
        elif num == 1:
            self.theButtonWind.destroy()
            self.__init__(self.root, self.back, self.manual_font, self.batteries)

    def __init__(self, root, back, manual_font, batteries):
        self.root = root
        self.back = back
        self.manual_font = manual_font
        self.theButtonWind = Toplevel(self.root)
        self.theButtonWind.title("The Button")
        self.theButtonWind.resizable(False, False)
        self.theButtonWind.config(bg=back)
        self.lftPos = (self.theButtonWind.winfo_screenwidth() - 1000) / 2
        self.topPos = (self.theButtonWind.winfo_screenheight() - 700) / 2
        self.theButtonWind.geometry("%dx%d+%d+%d" % (1000, 700, self.lftPos, self.topPos))

        self.batteries = batteries

        self.nameLabel = Label(self.theButtonWind, font=("Terminal", 25), fg="white", bg=back,
                               text="ON THE SUBJECT OF THE BUTTON")
        self.selectLabel = Label(self.theButtonWind, font=("Terminal", 20), fg="white", bg=back)

        self.topButtons = Frame(self.theButtonWind, bg=back)
        self.bottomButtons = Frame(self.theButtonWind, bg=back)
        self.nameLabel.pack(side=TOP, pady=30)
        self.selectLabel.pack(side=TOP, pady=30)

        self.topButtons.pack()
        self.bottomButtons.pack(pady=10)

        self.firstButton = Button(self.topButtons)
        self.secondButton = Button(self.topButtons)
        self.thirdButton = Button(self.topButtons)
        self.fourthButton = Button(self.bottomButtons)
        self.fifthButton = Button(self.bottomButtons)

        self.firstButton.pack(side=LEFT, padx=10)
        self.secondButton.pack(side=LEFT, padx=10)
        self.thirdButton.pack(side=LEFT, padx=10)
        self.fourthButton.pack(side=LEFT, padx=10)
        self.fifthButton.pack(side=LEFT, padx=10)

        self.backButton = Button(self.theButtonWind, text="BACK TO\nMODULE SELECT", font=("Terminal", 20),
                                 command=lambda: self.reset(0))
        self.resetButton = Button(self.theButtonWind, text="RESET", font=("Terminal", 20),
                                  command=lambda: self.reset(1))

        self.backButton.pack(side=BOTTOM)

        self.the_button("", "", "")

    def the_button(self, color, text, indicator):
        if color == "":
            self.selectLabel.config(text="WHAT COLOR IS THE BUTTON?")
            self.firstButton.config(image='', text="BLUE", font=self.manual_font,
                                    command=lambda: self.ask_the_button("blue", "", ""))
            self.secondButton.config(image='', text="WHITE", font=self.manual_font,
                                     command=lambda: self.ask_the_button("white", "", ""))
            self.thirdButton.config(image='', text="YELLOW", font=self.manual_font,
                                    command=lambda: self.ask_the_button("yellow", "", ""))
            self.fourthButton.config(image='', text="RED", font=self.manual_font,
                                     command=lambda: self.ask_the_button("red", "", ""))
            self.fifthButton.config(image='', text="OTHER", font=self.manual_font,
                                    command=lambda: self.ask_the_button("other", "", ""))
        elif text == "":
            self.resetButton.place(x=0, y=0)
            self.fifthButton.pack_forget()
            self.selectLabel.config(text="WHAT DOES THE BUTTON SAY?")
            self.firstButton.config(image='', text="ABORT", font=self.manual_font,
                                    command=lambda: self.ask_the_button(color, "abort", ""))
            self.secondButton.config(image='', text="DETONATE", font=self.manual_font,
                                     command=lambda: self.ask_the_button(color, "detonate", ""))
            self.thirdButton.config(image='', text="HOLD", font=self.manual_font,
                                    command=lambda: self.ask_the_button(color, "hold", ""))
            self.fourthButton.config(image='', text="OTHER", font=self.manual_font,
                                     command=lambda: self.ask_the_button(color, "other", ""))

        elif (indicator == "") and (color == "white" or self.batteries > 2):
            self.fourthButton.pack_forget()
            self.selectLabel.config(text="IS THERE A LIT INDICATOR WITH ANY OF THESE LABELS?")
            self.firstButton.config(image='', text="CAR", font=self.manual_font,
                                    command=lambda: self.ask_the_button(color, text, "car"))
            self.secondButton.config(image='', text="FRK", font=self.manual_font,
                                     command=lambda: self.ask_the_button(color, text, "frk"))
            self.thirdButton.config(image='', text="OTHER/NONE", font=self.manual_font,
                                    command=lambda: self.ask_the_button(color, text, "other"))

        else:
            self.hold_button("")

    def ask_the_button(self, color, text, indicator):
        if color == "blue" and text == "abort":
            self.hold_button("")
        elif text == "detonate" and self.batteries > 1:
            self.hold_button("release")
        elif color == "white" and indicator == "car":
            self.hold_button("")
        elif self.batteries > 2 and indicator == "frk":
            self.hold_button("release")
        elif color == "yellow" and self.batteries != -1 and indicator != "":
            self.resetButton.place(x=0, y=0)
            self.hold_button("")
        elif color == "red" and text == "hold":
            self.hold_button("release")
        else:
            self.the_button(color, text, indicator)

    def hold_button(self, color):
        self.thirdButton.pack(padx=10, side=LEFT)
        self.fourthButton.pack(padx=10, side=LEFT)
        self.fifthButton.pack_forget()

        if color == "":
            self.fourthButton.pack_forget()
            self.selectLabel.config(text="HOLD DOWN THE BUTTON AND\nSELECT THE COLOR OF THE STRIP ON THE SIDE")
            self.firstButton.config(text="BLUE STRIP", font=self.manual_font,
                                    command=lambda: self.hold_button(4))
            self.secondButton.config(text="YELLOW STRIP", font=self.manual_font,
                                     command=lambda: self.hold_button(5))
            self.thirdButton.config(text="OTHER COLOR STRIP", font=self.manual_font,
                                    command=lambda: self.hold_button(1))
        else:
            self.topButtons.pack_forget()
            self.bottomButtons.pack_forget()
            if isinstance(color, int):
                self.selectLabel.config(text="RELEASE WHEN THE COUNTDOWN TIMER HAS\nA {} IN ANY POSITION".format(color))
            else:
                self.selectLabel.config(text="PRESS AND IMMEDIATELY RELEASE THE BUTTON")
