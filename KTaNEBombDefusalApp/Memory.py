from tkinter import *


class Memory:

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
                               text="ON THE SUBJECT OF MEMORY")
        self.selectLabel = Label(self.simonSaysWin, font=self.manual_font, fg="white", bg=back)
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

        self.backButton = Button(self.simonSaysWin, text="BACK TO\nMODULE SELECT", font=("Terminal", 20),
                                 command=lambda: self.reset(0))
        self.resetButton = Button(self.simonSaysWin, text="RESET", font=("Terminal", 20),
                                  command=lambda: self.reset(1))

        self.backButton.pack(side=BOTTOM)

        self.display_select(1, "", 0, "", 0, "", 0, "", 0)

    def display_select(self, stage, pos1, num1, pos2, num2, pos3, num3, pos4, num4):
        self.selectLabel.config(text="STAGE " + str(stage) + "\nWHAT DOES THE DISPLAY SAYS?")
        self.firstButton.config(text="1",
                                command=lambda: self.stages(1, stage, pos1, num1, pos2, num2, pos3, num3, pos4, num4))
        self.secondButton.config(text="2",
                                 command=lambda: self.stages(2, stage, pos1, num1, pos2, num2, pos3, num3, pos4, num4
                                                             ))
        self.thirdButton.config(text="3",
                                command=lambda: self.stages(3, stage, pos1, num1, pos2, num2, pos3, num3, pos4, num4
                                                            ))
        self.fourthButton.config(text="4",
                                 command=lambda: self.stages(4, stage, pos1, num1, pos2, num2, pos3, num3, pos4, num4
                                                             ))

        self.firstButton.pack(side=LEFT, padx=10)
        self.secondButton.pack(side=LEFT, padx=10)
        self.thirdButton.pack(side=LEFT, padx=10)
        self.fourthButton.pack(side=LEFT, padx=10)

    def stages(self, display, stage, pos1, num1, pos2, num2, pos3, num3, pos4, num4):
        self.firstButton.pack(side=LEFT, padx=10)
        self.secondButton.pack(side=LEFT, padx=10)
        self.thirdButton.pack(side=LEFT, padx=10)
        self.fourthButton.pack(side=LEFT, padx=10)

        if stage == 1:
            self.resetButton.place(x=0, y=0)
            if display == 1 or display == 2:
                self.selectLabel.config(text="PRESS THE BUTTON IN THE SECOND POSITION AND"
                                             "\nSELECT THE LABEL IN THAT POSITION")
                self.firstButton.config(text="1",
                                        command=lambda: self.display_select(stage + 1,
                                                                            "SECOND", 1,
                                                                            pos2, num2,
                                                                            pos3, num3,
                                                                            pos4, num4))
                self.secondButton.config(text="2",
                                         command=lambda: self.display_select(stage + 1,
                                                                             "SECOND", 2,
                                                                             pos2, num2,
                                                                             pos3, num3,
                                                                             pos4, num4))
                self.thirdButton.config(text="3",
                                        command=lambda: self.display_select(stage + 1,
                                                                            "SECOND", 3,
                                                                            pos2, num2,
                                                                            pos3, num3,
                                                                            pos4, num4))
                self.fourthButton.config(text="4",
                                         command=lambda: self.display_select(stage + 1,
                                                                             "SECOND", 4,
                                                                             pos2, num2,
                                                                             pos3, num3,
                                                                             pos4, num4))
            elif display == 3:
                self.selectLabel.config(text="PRESS THE BUTTON IN THE THIRD POSITION AND"
                                             "\nSELECT THE LABEL IN THAT POSITION")
                self.firstButton.config(text="1",
                                        command=lambda: self.display_select(stage + 1,
                                                                            "THIRD", 1,
                                                                            pos2, num2,
                                                                            pos3, num3,
                                                                            pos4, num4))
                self.secondButton.config(text="2",
                                         command=lambda: self.display_select(stage + 1,
                                                                             "THIRD", 2,
                                                                             pos2, num2,
                                                                             pos3, num3,
                                                                             pos4, num4))
                self.thirdButton.config(text="3",
                                        command=lambda: self.display_select(stage + 1,
                                                                            "THIRD", 3,
                                                                            pos2, num2,
                                                                            pos3, num3,
                                                                            pos4, num4))
                self.fourthButton.config(text="4",
                                         command=lambda: self.display_select(stage,
                                                                             "THIRD", 4,
                                                                             pos2, num2,
                                                                             pos3, num3,
                                                                             pos4, num4))
            elif display == 4:
                self.selectLabel.config(text="PRESS THE BUTTON IN THE FOURTH POSITION AND"
                                             "\nSELECT THE LABEL IN THAT POSITION")
                self.firstButton.config(text="1",
                                        command=lambda: self.display_select(stage + 1,
                                                                            "FOURTH", 1,
                                                                            pos2, num2,
                                                                            pos3, num3,
                                                                            pos4, num4))
                self.secondButton.config(text="2",
                                         command=lambda: self.display_select(stage + 1,
                                                                             "FOURTH", 2,
                                                                             pos2, num2,
                                                                             pos3, num3,
                                                                             pos4, num4))
                self.thirdButton.config(text="3",
                                        command=lambda: self.display_select(stage + 1,
                                                                            "FOURTH", 3,
                                                                            pos2, num2,
                                                                            pos3, num3,
                                                                            pos4, num4))
                self.fourthButton.config(text="4",
                                         command=lambda: self.display_select(stage + 1,
                                                                             "FOURTH", 4,
                                                                             pos2, num2,
                                                                             pos3, num3,
                                                                             pos4, num4))
        elif stage == 2:
            if display == 1:
                self.selectLabel.config(text="PRESS THE BUTTON LABELED '4' AND"
                                             "\nSELECT THE POSITION OF THAT BUTTON")
                self.firstButton.config(text="FIRST POSITION",
                                        command=lambda: self.display_select(stage + 1,
                                                                            pos1, num1,
                                                                            "FIRST", 4,
                                                                            pos3, num3,
                                                                            pos4, num4))
                self.secondButton.config(text="SECOND POSITION",
                                         command=lambda: self.display_select(stage + 1,
                                                                             pos1, num1,
                                                                             "SECOND", 4,
                                                                             pos3, num3,
                                                                             pos4, num4))
                self.thirdButton.config(text="THIRD POSITION",
                                        command=lambda: self.display_select(stage + 1,
                                                                            pos1, num1,
                                                                            "THIRD", 4,
                                                                            pos3, num3,
                                                                            pos4, num4))
                self.fourthButton.config(text="FOURTH POSITION",
                                         command=lambda: self.display_select(stage + 1,
                                                                             pos1, num1,
                                                                             "FOURTH", 4,
                                                                             pos3, num3,
                                                                             pos4, num4))
            elif display == 2 or 4:
                self.selectLabel.config(text="PRESS THE BUTTON IN THE " + pos1 + " POSITION AND"
                                                                                 "\nSELECT THE LABEL IN THAT POSITION")
                self.firstButton.config(text="1",
                                        command=lambda: self.display_select(stage + 1,
                                                                            pos1, num1,
                                                                            pos1, 1,
                                                                            pos3, num3,
                                                                            pos4, num4))
                self.secondButton.config(text="2",
                                         command=lambda: self.display_select(stage + 1,
                                                                             pos1, num1,
                                                                             pos1, 2,
                                                                             pos3, num3,
                                                                             pos4, num4))
                self.thirdButton.config(text="3",
                                        command=lambda: self.display_select(stage + 1,
                                                                            pos1, num1,
                                                                            pos1, 3,
                                                                            pos3, num3,
                                                                            pos4, num4))
                self.fourthButton.config(text="4",
                                         command=lambda: self.display_select(stage + 1,
                                                                             pos1, num1,
                                                                             pos1, 4,
                                                                             pos3, num3,
                                                                             pos4, num4))
            elif display == 3:
                self.selectLabel.config(text="PRESS THE BUTTON IN THE FIRST POSITION AND"
                                             "\nSELECT THE LABEL IN THAT POSITION")
                self.firstButton.config(text="1",
                                        command=lambda: self.display_select(stage + 1,
                                                                            pos1, num1,
                                                                            "FIRST", 1,
                                                                            pos3, num3,
                                                                            pos4, num4))
                self.secondButton.config(text="2",
                                         command=lambda: self.display_select(stage + 1,
                                                                             pos1, num1,
                                                                             "FIRST", 2,
                                                                             pos3, num3,
                                                                             pos4, num4))
                self.thirdButton.config(text="3",
                                        command=lambda: self.display_select(stage + 1,
                                                                            pos1, num1,
                                                                            "FIRST", 3,
                                                                            pos3, num3,
                                                                            pos4, num4))
                self.fourthButton.config(text="4",
                                         command=lambda: self.display_select(stage + 1,
                                                                             pos1, num1,
                                                                             "FIRST", 4,
                                                                             pos3, num3,
                                                                             pos4, num4))
        elif stage == 3:
            if display == 1:
                self.selectLabel.config(text="PRESS THE BUTTON LABELED '" + str(num2) + "' AND"
                                                                                        "\nSELECT THE POSITION OF "
                                                                                        "THAT BUTTON")

                self.firstButton.config(text="FIRST POSITION",
                                        command=lambda: self.display_select(stage + 1,
                                                                            pos1, num1,
                                                                            pos2, num2,
                                                                            "FIRST", num2,
                                                                            pos4, num4))
                self.secondButton.config(text="SECOND POSITION",
                                         command=lambda: self.display_select(stage + 1,
                                                                             pos1, num1,
                                                                             pos2, num2,
                                                                             "SECOND", num2,
                                                                             pos4, num4))
                self.thirdButton.config(text="THIRD POSITION",
                                        command=lambda: self.display_select(stage + 1,
                                                                            pos1, num1,
                                                                            pos2, num2,
                                                                            "THIRD", num2,
                                                                            pos4, num4))
                self.fourthButton.config(text="FOURTH POSITION",
                                         command=lambda: self.display_select(stage + 1,
                                                                             pos1, num1,
                                                                             pos2, num2,
                                                                             "FOURTH", num2,
                                                                             pos4, num4))
            elif display == 2:
                self.selectLabel.config(text="PRESS THE BUTTON LABELED '" + str(num1) + "' AND"
                                                                                        "\nSELECT THE POSITION OF "
                                                                                        "THAT BUTTON")

                self.firstButton.config(text="FIRST POSITION",
                                        command=lambda: self.display_select(stage + 1,
                                                                            pos1, num1,
                                                                            pos2, num2,
                                                                            "FIRST", num1,
                                                                            pos4, num4))
                self.secondButton.config(text="SECOND POSITION",
                                         command=lambda: self.display_select(stage + 1,
                                                                             pos1, num1,
                                                                             pos2, num2,
                                                                             "SECOND", num1,
                                                                             pos4, num4))
                self.thirdButton.config(text="THIRD POSITION",
                                        command=lambda: self.display_select(stage + 1,
                                                                            pos1, num1,
                                                                            pos2, num2,
                                                                            "THIRD", num1,
                                                                            pos4, num4))
                self.fourthButton.config(text="FOURTH POSITION",
                                         command=lambda: self.display_select(stage + 1,
                                                                             pos1, num1,
                                                                             pos2, num2,
                                                                             "FOURTH", num1,
                                                                             pos4, num4))
            elif display == 3:
                self.selectLabel.config(text="PRESS THE BUTTON IN THE THIRD POSITION AND"
                                             "\nSELECT THE LABEL IN THAT POSITION")
                self.firstButton.config(text="1",
                                        command=lambda: self.display_select(stage + 1,
                                                                            pos1, num1,
                                                                            pos2, num2,
                                                                            "THIRD", 1,
                                                                            pos4, num4))
                self.secondButton.config(text="2",
                                         command=lambda: self.display_select(stage + 1,
                                                                             pos1, num1,
                                                                             pos2, num2,
                                                                             "THIRD", 2,
                                                                             pos4, num4))
                self.thirdButton.config(text="3",
                                        command=lambda: self.display_select(stage + 1,
                                                                            pos1, num1,
                                                                            pos2, num2,
                                                                            "THIRD", 3,
                                                                            pos4, num4))
                self.fourthButton.config(text="4",
                                         command=lambda: self.display_select(stage + 1,
                                                                             pos1, num1,
                                                                             pos2, num2,
                                                                             "THIRD", 4,
                                                                             pos4, num4))
            elif display == 4:
                self.selectLabel.config(text="PRESS THE BUTTON LABELED '4' AND"
                                             "\nSELECT THE POSITION OF THAT BUTTON")
                self.firstButton.config(text="FIRST POSITION",
                                        command=lambda: self.display_select(stage + 1,
                                                                            pos1, num1,
                                                                            pos2, num2,
                                                                            "FIRST", 4,
                                                                            pos4, num4))
                self.secondButton.config(text="SECOND POSITION",
                                         command=lambda: self.display_select(stage + 1,
                                                                             pos1, num1,
                                                                             pos2, num2,
                                                                             "SECOND", 4,
                                                                             pos4, num4))
                self.thirdButton.config(text="THIRD POSITION",
                                        command=lambda: self.display_select(stage + 1,
                                                                            pos1, num1,
                                                                            pos2, num2,
                                                                            "THIRD", 4,
                                                                            pos4, num4))
                self.fourthButton.config(text="FOURTH POSITION",
                                         command=lambda: self.display_select(stage + 1,
                                                                             pos1, num1,
                                                                             pos2, num2,
                                                                             "FOURTH", 4,
                                                                             pos4, num4))
        elif stage == 4:
            if display == 1:
                self.selectLabel.config(text="PRESS THE BUTTON IN THE " + pos1 + " POSITION AND"
                                                                                 "\nSELECT THE LABEL IN THAT POSITION")

                self.firstButton.config(text="1",
                                        command=lambda: self.display_select(stage + 1,
                                                                            pos1, num1,
                                                                            pos2, num2,
                                                                            pos3, num3,
                                                                            pos1, 1))
                self.secondButton.config(text="2",
                                         command=lambda: self.display_select(stage + 1,
                                                                             pos1, num1,
                                                                             pos2, num2,
                                                                             pos3, num3,
                                                                             pos1, 2))
                self.thirdButton.config(text="3",
                                        command=lambda: self.display_select(stage + 1,
                                                                            pos1, num1,
                                                                            pos2, num2,
                                                                            pos3, num3,
                                                                            pos1, 3))
                self.fourthButton.config(text="4",
                                         command=lambda: self.display_select(stage + 1,
                                                                             pos1, num1,
                                                                             pos2, num2,
                                                                             pos3, num3,
                                                                             pos1, 4))
            elif display == 2:
                self.selectLabel.config(text="PRESS THE BUTTON IN THE FIRST POSITION AND"
                                             "\nSELECT THE LABEL IN THAT POSITION")
                self.firstButton.config(text="1",
                                        command=lambda: self.display_select(stage + 1,
                                                                            pos1, num1,
                                                                            pos2, num2,
                                                                            pos3, num3,
                                                                            "FIRST", 1))
                self.secondButton.config(text="2",
                                         command=lambda: self.display_select(stage + 1,
                                                                             pos1, num1,
                                                                             pos2, num2,
                                                                             pos3, num3,
                                                                             "FIRST", 2))
                self.thirdButton.config(text="3",
                                        command=lambda: self.display_select(stage + 1,
                                                                            pos1, num1,
                                                                            pos2, num2,
                                                                            pos3, num3,
                                                                            "FIRST", 3))
                self.fourthButton.config(text="4",
                                         command=lambda: self.display_select(stage + 1,
                                                                             pos1, num1,
                                                                             pos2, num2,
                                                                             pos3, num3,
                                                                             "FIRST", 4))
            elif display == 3 or 4:
                self.selectLabel.config(text="PRESS THE BUTTON IN THE " + pos2 + " POSITION AND"
                                                                                 "\nSELECT THE LABEL IN THAT POSITION")
                self.firstButton.config(text="1",
                                        command=lambda: self.display_select(stage + 1,
                                                                            pos1, num1,
                                                                            pos2, num2,
                                                                            pos3, num3,
                                                                            pos2, 1))
                self.secondButton.config(text="2",
                                         command=lambda: self.display_select(stage + 1,
                                                                             pos1, num1,
                                                                             pos2, num2,
                                                                             pos3, num3,
                                                                             pos2, 2))
                self.thirdButton.config(text="3",
                                        command=lambda: self.display_select(stage + 1,
                                                                            pos1, num1,
                                                                            pos2, num2,
                                                                            pos3, num3,
                                                                            pos2, 3))
                self.fourthButton.config(text="4",
                                         command=lambda: self.display_select(stage + 1,
                                                                             pos1, num1,
                                                                             pos2, num2,
                                                                             pos3, num3,
                                                                             pos2, 4))

        elif stage == 5:
            self.firstButton.pack_forget()
            self.secondButton.pack_forget()
            self.thirdButton.pack_forget()
            self.fourthButton.pack_forget()
            if display == 1:
                self.selectLabel.config(text="PRESS THE BUTTON LABELED '" + str(num1) + "'")
            elif display == 2:
                self.selectLabel.config(text="PRESS THE BUTTON LABELED '" + str(num2) + "'")
            elif display == 3:
                self.selectLabel.config(text="PRESS THE BUTTON LABELED '" + str(num4) + "'")
            elif display == 4:
                self.selectLabel.config(text="PRESS THE BUTTON LABELED '" + str(num3) + "'")
