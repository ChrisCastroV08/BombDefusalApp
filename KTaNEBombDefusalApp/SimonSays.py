from tkinter import *


class SimonSays:

    def reset(self, num):
        if num == 0:
            self.simonSaysWin.destroy()
        elif num == 1:
            self.simonSaysWin.destroy()
            self.__init__(self.root, self.back, self.manual_font)

    def __init__(self, root, back, font):
        self.root = root
        self.back = back
        self.manual_font = font
        self.simonSaysWin = Toplevel(self.root)
        self.simonSaysWin.title("Simon Says")
        self.simonSaysWin.resizable(False, False)
        self.simonSaysWin.config(bg=back)
        self.lftPos = (self.simonSaysWin.winfo_screenwidth() - 1000) / 2
        self.topPos = (self.simonSaysWin.winfo_screenheight() - 700) / 2
        self.simonSaysWin.geometry("%dx%d+%d+%d" % (1000, 700, self.lftPos, self.topPos))

        self.nameLabel = Label(self.simonSaysWin, font=("Terminal", 25), fg="white", bg=back,
                               text="ON THE SUBJECT OF SIMON SAYS")
        self.selectLabel = Label(self.simonSaysWin, font=self.manual_font, fg="white", bg=back,
                                 text="HOW MANY STRIKES THE DEFUSER HAS?")
        self.topButtons = Frame(self.simonSaysWin, bg=back)
        self.bottomButtons = Frame(self.simonSaysWin, bg=back)
        self.nameLabel.pack(side=TOP, pady=30)
        self.selectLabel.pack(side=TOP, pady=30)

        self.topButtons.pack()
        self.bottomButtons.pack(pady=10)

        self.firstButton = Button(self.topButtons, font=self.manual_font)
        self.secondButton = Button(self.topButtons, font=self.manual_font)
        self.thirdButton = Button(self.bottomButtons, font=self.manual_font)
        self.fourthButton = Button(self.bottomButtons, font=self.manual_font)

        self.firstButton.pack(side=LEFT, padx=10)
        self.thirdButton.pack(side=LEFT, padx=10)
        self.fourthButton.pack(side=LEFT, padx=10)

        self.backButton = Button(self.simonSaysWin, text="BACK TO\nMODULE SELECT", font=("Terminal", 20),
                                 command=lambda: self.reset(0))
        self.resetButton = Button(self.simonSaysWin, text="RESET", font=("Terminal", 20),
                                  command=lambda: self.reset(1))

        self.backButton.pack(side=BOTTOM)
        self.bomb_info(3)

    def bomb_info(self, strikes):
        if strikes == 3:
            self.firstButton.config(text="NO STRIKES", command=lambda: self.bomb_info(0))
            self.thirdButton.config(text="1 STRIKE", command=lambda: self.bomb_info(1))
            self.fourthButton.config(text="2 STRIKES", command=lambda: self.bomb_info(2))
        else:
            self.resetButton.place(x=0, y=0)
            self.selectLabel.config(text="DOES THE SERIAL NUMBER CONTAIN A VOWEL?")
            self.firstButton.config(text="YES", command=lambda: self.simon_says(strikes, True, ""))
            self.secondButton.config(text="NO", command=lambda: self.simon_says(strikes, False, ""))
            self.secondButton.pack(side=LEFT, padx=10)
            self.thirdButton.pack_forget()
            self.fourthButton.pack_forget()

    def simon_says(self, strikes, vowel, color):
        if color == "":
            self.firstButton.pack(side=LEFT, padx=10)
            self.secondButton.pack(side=LEFT, padx=10)
            self.thirdButton.pack(side=LEFT, padx=10)
            self.fourthButton.pack(side=LEFT, padx=10)
            self.selectLabel.config(text="SELECT THE COLOR THAT FLASHES")
            self.firstButton.config(text="BLUE", command=lambda: self.simon_says(strikes, vowel, "b"))
            self.secondButton.config(text="YELLOW", command=lambda: self.simon_says(strikes, vowel, "y"))
            self.thirdButton.config(text="RED", command=lambda: self.simon_says(strikes, vowel, "r"))
            self.fourthButton.config(text="GREEN", command=lambda: self.simon_says(strikes, vowel, "g"))
        elif color == "r":
            self.firstButton.config(text="NEXT", command=lambda: self.simon_says(strikes, vowel, ""))
            self.secondButton.pack_forget()
            self.thirdButton.pack_forget()
            self.fourthButton.pack_forget()
            if vowel:
                if strikes == 0:
                    self.selectLabel.config(text="PRESS THE BLUE BUTTON")
                if strikes == 1:
                    self.selectLabel.config(text="PRESS THE YELLOW BUTTON")
                if strikes == 2:
                    self.selectLabel.config(text="PRESS THE GREEN BUTTON")

            if not vowel:
                if strikes == 0:
                    self.selectLabel.config(text="PRESS THE BLUE BUTTON")
                if strikes == 1:
                    self.selectLabel.config(text="PRESS THE RED BUTTON")
                if strikes == 2:
                    self.selectLabel.config(text="PRESS THE YELLOW BUTTON")

        elif color == "b":
            self.firstButton.config(text="NEXT", command=lambda: self.simon_says(strikes, vowel, ""))
            self.secondButton.pack_forget()
            self.thirdButton.pack_forget()
            self.fourthButton.pack_forget()
            if vowel:
                if strikes == 0:
                    self.selectLabel.config(text="PRESS THE RED BUTTON")
                if strikes == 1:
                    self.selectLabel.config(text="PRESS THE GREEN BUTTON")
                if strikes == 2:
                    self.selectLabel.config(text="PRESS THE RED BUTTON")
            if not vowel:
                if strikes == 0:
                    self.selectLabel.config(text="PRESS THE YELLOW BUTTON")
                if strikes == 1:
                    self.selectLabel.config(text="PRESS THE BLUE BUTTON")
                if strikes == 2:
                    self.selectLabel.config(text="PRESS THE GREEN BUTTON")

        elif color == "g":
            self.firstButton.config(text="NEXT", command=lambda: self.simon_says(strikes, vowel, ""))
            self.secondButton.pack_forget()
            self.thirdButton.pack_forget()
            self.fourthButton.pack_forget()
            if vowel:
                if strikes == 0:
                    self.selectLabel.config(text="PRESS THE YELLOW BUTTON")
                if strikes == 1:
                    self.selectLabel.config(text="PRESS THE BLUE BUTTON")
                if strikes == 2:
                    self.selectLabel.config(text="PRESS THE YELLOW BUTTON")
            if not vowel:
                if strikes == 0:
                    self.selectLabel.config(text="PRESS THE GREEN BUTTON")
                if strikes == 1:
                    self.selectLabel.config(text="PRESS THE YELLOW BUTTON")
                if strikes == 2:
                    self.selectLabel.config(text="PRESS THE BLUE BUTTON")

        elif color == "y":
            self.firstButton.config(text="NEXT", command=lambda: self.simon_says(strikes, vowel, ""))
            self.secondButton.pack_forget()
            self.thirdButton.pack_forget()
            self.fourthButton.pack_forget()
            if vowel:
                if strikes == 0:
                    self.selectLabel.config(text="PRESS THE GREEN BUTTON")
                if strikes == 1:
                    self.selectLabel.config(text="PRESS THE RED BUTTON")
                if strikes == 2:
                    self.selectLabel.config(text="PRESS THE BLUE BUTTON")
            if not vowel:
                if strikes == 0:
                    self.selectLabel.config(text="PRESS THE RED BUTTON")
                if strikes == 1:
                    self.selectLabel.config(text="PRESS THE GREEN BUTTON")
                if strikes == 2:
                    self.selectLabel.config(text="PRESS THE RED BUTTON")
