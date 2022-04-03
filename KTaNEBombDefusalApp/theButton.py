from tkinter import *
from tkinter.font import Font


class TheButton:

    def reset(self, num):
        if num == 0:
            self.theButtonWind.destroy()
        elif num == 1:
            self.theButtonWind.destroy()
            self.__init__(self.root, self.back)

    def __init__(self, root, back):
        self.root = root
        self.back = back
        self.theButtonWind = Toplevel(self.root)
        self.theButtonWind.title("The Button")
        self.theButtonWind.resizable(False, False)
        self.theButtonWind.config(bg=back)
        self.lftPos = (self.theButtonWind.winfo_screenwidth() - 1000) / 2
        self.topPos = (self.theButtonWind.winfo_screenheight() - 700) / 2
        self.theButtonWind.geometry("%dx%d+%d+%d" % (1000, 700, self.lftPos, self.topPos))

        self.wires = PhotoImage(file="Images/Wires.png")
        self.manual_font = Font(
            family="Terminal",
            size=20)

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

        self.the_button("", "", -1, "")

    def the_button(self, color, text, batteries, indicator):
        if color == "":
            self.selectLabel.config(text="WHAT COLOR IS THE BUTTON?")
            self.firstButton.config(image='', text="BLUE", font=self.manual_font,
                                    command=lambda: self.ask_the_button("blue", "", -1, ""))
            self.secondButton.config(image='', text="WHITE", font=self.manual_font,
                                     command=lambda: self.ask_the_button("white", "", -1, ""))
            self.thirdButton.config(image='', text="YELLOW", font=self.manual_font,
                                    command=lambda: self.ask_the_button("yellow", "", -1, ""))
            self.fourthButton.config(image='', text="RED", font=self.manual_font,
                                     command=lambda: self.ask_the_button("red", "", -1, ""))
            self.fifthButton.config(image='', text="OTHER", font=self.manual_font,
                                    command=lambda: self.ask_the_button("other", "", -1, ""))
        elif text == "":
            self.resetButton.place(x=0, y=0)
            self.fifthButton.pack_forget()
            self.selectLabel.config(text="WHAT DOES THE BUTTON SAY?")
            self.firstButton.config(image='', text="ABORT", font=self.manual_font,
                                    command=lambda: self.ask_the_button(color, "abort", -1, ""))
            self.secondButton.config(image='', text="DETONATE", font=self.manual_font,
                                     command=lambda: self.ask_the_button(color, "detonate", -1, ""))
            self.thirdButton.config(image='', text="HOLD", font=self.manual_font,
                                    command=lambda: self.ask_the_button(color, "hold", -1, ""))
            self.fourthButton.config(image='', text="OTHER", font=self.manual_font,
                                     command=lambda: self.ask_the_button(color, "other", -1, ""))
        elif indicator == "" and (color == "white" and text != "detonate" or batteries > 2):
            self.fourthButton.pack_forget()
            self.selectLabel.config(text="IS THERE A LIT INDICATOR WITH ANY OF THESE LABELS?")
            self.firstButton.config(image='', text="CAR", font=self.manual_font,
                                    command=lambda: self.ask_the_button(color, text, batteries, "car"))
            self.secondButton.config(image='', text="FRK", font=self.manual_font,
                                     command=lambda: self.ask_the_button(color, text, batteries, "frk"))
            self.thirdButton.config(image='', text="OTHER/NONE", font=self.manual_font,
                                    command=lambda: self.ask_the_button(color, text, batteries, "other"))

        elif batteries == -1 and (text == "detonate" or indicator == "frk" or indicator == ""):
            self.fourthButton.pack(side=LEFT, padx=10)
            self.selectLabel.config(text="HOW MANY BATTERIES ARE IN THE BOMB?")
            self.firstButton.config(image='', text="NONE", font=self.manual_font,
                                    command=lambda: self.ask_the_button(color, text, 0, indicator))
            self.secondButton.config(image='', text="1 BATTERY", font=self.manual_font,
                                     command=lambda: self.ask_the_button(color, text, 1, indicator))
            self.thirdButton.config(image='', text="2 BATTERIES", font=self.manual_font,
                                    command=lambda: self.ask_the_button(color, text, 2, indicator))
            self.fourthButton.config(image='', text="3 OR MORE BATTERIES", font=self.manual_font,
                                     command=lambda: self.ask_the_button(color, text, 3, indicator))

        else:
            self.held_button("")

    def ask_the_button(self, color, text, batteries, indicator):
        if color == "blue" and text == "abort":
            self.held_button("")
        elif text == "detonate" and batteries > 1:
            self.held_button("release")
        elif color == "white" and indicator == "car":
            self.held_button("")
        elif batteries > 2 and indicator == "frk":
            self.held_button("release")
        elif color == "yellow":
            self.resetButton.place(x=0, y=0)
            self.held_button("")
        elif color == "red" and text == "hold":
            self.held_button("release")
        else:
            self.the_button(color, text, batteries, indicator)

    def held_button(self, color):
        self.thirdButton.pack(padx=10, side=LEFT)
        self.fourthButton.pack(padx=10, side=LEFT)
        self.fifthButton.pack_forget()

        if color == "":
            self.selectLabel.config(text="HOLD DOWN THE BUTTON AND\nSELECT THE COLOR OF THE STRIP ON THE SIDE")
            self.firstButton.config(image='', text="BLUE STRIP", font=self.manual_font,
                                    command=lambda: self.held_button("blue"))
            self.secondButton.config(image='', text="WHITE STRIP", font=self.manual_font,
                                     command=lambda: self.held_button("white"))
            self.thirdButton.config(image='', text="YELLOW STRIP", font=self.manual_font,
                                    command=lambda: self.held_button("yellow"))
            self.fourthButton.config(image='', text="OTHER", font=self.manual_font,
                                     command=lambda: self.held_button("any"))
        else:
            self.topButtons.pack_forget()
            self.bottomButtons.pack_forget()
            if color == "blue":
                self.selectLabel.config(text="RELEASE WHEN THE COUNTDOWN TIMER HAS\nA 4 IN ANY POSITION")
            elif color == "white" or color == "any":
                self.selectLabel.config(text="RELEASE WHEN THE COUNTDOWN TIMER HAS\nA 1 IN ANY POSITION")
            elif color == "yellow":
                self.selectLabel.config(text="RELEASE WHEN THE COUNTDOWN TIMER HAS\nA 5 IN ANY POSITION")
            else:
                self.selectLabel.config(text="PRESS AND IMMEDIATELY RELEASE THE BUTTON")
