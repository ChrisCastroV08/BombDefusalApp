from tkinter import *


class SimonSays:

    def reset(self, num):
        if num == 0:
            self.simonSaysWin.destroy()
        elif num == 1:
            self.simonSaysWin.destroy()
            self.__init__(self.root, self.back, self.manual_font, self.serial)

    def __init__(self, root, back, manual_font, serial):
        self.root = root
        self.back = back
        self.manual_font = manual_font
        self.serial = serial
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
        self.ansLabel = Label(self.simonSaysWin, font=self.manual_font, fg="white", bg=back)

        self.topButtons = Frame(self.simonSaysWin, bg=back)
        self.bottomButtons = Frame(self.simonSaysWin, bg=back)
        self.bottomButtons2 = Frame(self.simonSaysWin, bg=back)
        self.simon_list = []
        self.info = []

        for char in self.serial:
            if char in 'AEIOU':
                self.vowel = True
                break
            self.vowel = False
        self.nameLabel.pack(side=TOP, pady=30)
        self.selectLabel.pack(side=TOP, pady=30)

        self.topButtons.pack()
        self.bottomButtons.pack(pady=10)
        self.bottomButtons2.pack()
        self.ansLabel.pack(pady=10)

        self.firstButton = Button(self.topButtons, font=self.manual_font,
                                  text="NO STRIKES", command=lambda: self.simon_says(0, True))
        self.secondButton = Button(self.topButtons, font=self.manual_font
                                   )
        self.thirdButton = Button(self.bottomButtons, font=self.manual_font,
                                  text="1 STRIKE", command=lambda: self.simon_says(1, True))
        self.fourthButton = Button(self.bottomButtons, font=self.manual_font,
                                   text="2 STRIKES", command=lambda: self.simon_says(2, True))
        self.fifthButton = Button(self.bottomButtons2, font=self.manual_font, fg="red")
        self.sixthButton = Button(self.bottomButtons2, font=self.manual_font)
        self.seventhButton = Button(self.bottomButtons2, font=self.manual_font, fg="green", state=DISABLED)

        self.firstButton.pack(side=LEFT, padx=10)
        self.thirdButton.pack(side=LEFT, padx=10)
        self.fourthButton.pack(side=LEFT, padx=10)

        self.buttons = [self.firstButton, self.secondButton, self.thirdButton, self.fourthButton,
                        self.fifthButton, self.sixthButton, self.seventhButton]

        self.backButton = Button(self.simonSaysWin, text="BACK TO\nMODULE SELECT", font=("Terminal", 20),
                                 command=lambda: self.reset(0))
        self.resetButton = Button(self.simonSaysWin, text="RESET", font=("Terminal", 20),
                                  command=lambda: self.reset(1))

        self.backButton.pack(side=BOTTOM)

    def word(self, string):
        if string != "clear" and string != "erase":
            self.simon_list.append(string)
            self.ansLabel.config(text=' - '.join(self.simon_list))

        elif string == "erase":
            self.simon_list = self.simon_list[:-1]
            self.ansLabel.config(text=' - '.join(self.simon_list))
        else:
            self.simon_list.clear()
            self.ansLabel.config(text='')
        if len(self.simon_list) < 1:
            self.seventhButton.config(state=DISABLED)
        else:
            self.seventhButton.config(state=NORMAL)

    def simon_says(self, strikes, first_time):
        self.resetButton.place(x=0, y=0)
        self.ansLabel.config(text=' - '.join(self.simon_list))
        if first_time:
            self.info.append(strikes)
            self.info.append(self.vowel)
        self.seventhButton.pack_forget()
        self.selectLabel.config(text="SELECT ALL THE COLORS THAT FLASHES IN ORDER")
        but_config = [("BLUE", lambda: self.word("BLUE")),
                      ("YELLOW", lambda: self.word("YELLOW")),
                      ("RED", lambda: self.word("RED")),
                      ("GREEN", lambda: self.word("GREEN")),
                      ("CLEAR", lambda: self.word("clear")),
                      ("ERASE", lambda: self.word("erase")),
                      ("NEXT", lambda: self.press())]
        i = 0
        for btn in but_config:
            self.buttons[i].config(text=btn[0], command=btn[1])
            self.buttons[i].pack(side=LEFT, padx=10)
            i = i + 1

    def press(self):
        ans_label = []
        self.firstButton.pack_forget()
        self.secondButton.pack_forget()
        self.thirdButton.pack_forget()
        self.fourthButton.pack_forget()
        self.fifthButton.pack_forget()
        self.sixthButton.pack_forget()
        self.ansLabel.config(text="")
        self.seventhButton.config(command=lambda: self.simon_says(0, False))
        for i in range(len(self.simon_list)):
            if self.simon_list[i] == "RED":
                if self.info[1]:
                    if self.info[0] == 0:
                        ans_label.append("BLUE")
                    if self.info[0] == 1:
                        ans_label.append("YELLOW")
                    if self.info[0] == 2:
                        ans_label.append("GREEN")

                if not self.info[1]:
                    if self.info[0] == 0:
                        ans_label.append("BLUE")
                    if self.info[0] == 1:
                        ans_label.append("RED")
                    if self.info[0] == 2:
                        ans_label.append("YELLOW")

            elif self.simon_list[i] == "BLUE":
                if self.info[1]:
                    if self.info[0] == 0 or self.info[0] == 2:
                        ans_label.append("RED")
                    if self.info[0] == 1:
                        ans_label.append("GREEN")

                if not self.info[1]:
                    if self.info[0] == 0:
                        ans_label.append("YELLOW")
                    if self.info[0] == 1:
                        ans_label.append("BLUE")
                    if self.info[0] == 2:
                        ans_label.append("GREEN")

            elif self.simon_list[i] == "GREEN":
                if self.info[1]:
                    if self.info[0] == 0 or self.info[0] == 2:
                        ans_label.append("YELLOW")
                    if self.info[0] == 1:
                        ans_label.append("BLUE")

                if not self.info[1]:
                    if self.info[0] == 0:
                        ans_label.append("GREEN")
                    if self.info[0] == 1:
                        ans_label.append("YELLOW")
                    if self.info[0] == 2:
                        ans_label.append("BLUE")

            elif self.simon_list[i] == "YELLOW":
                if self.info[1]:
                    if self.info[0] == 0:
                        ans_label.append("GREEN")
                    if self.info[0] == 1:
                        ans_label.append("RED")
                    if self.info[0] == 2:
                        ans_label.append("BLUE")

                if not self.info[1]:
                    if self.info[0] == 0 or self.info[0] == 2:
                        ans_label.append("RED")
                    if self.info[0] == 1:
                        ans_label.append("GREEN")

        if len(self.simon_list) != 0:
            self.selectLabel.config(text="PRESS '" + ', '.join(ans_label) + "' IN THAT ORDER")
