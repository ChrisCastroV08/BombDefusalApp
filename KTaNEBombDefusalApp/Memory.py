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

        self.display_select(1, "", 0, "", 0, 0, 0)

    def display_select(self, stage, pos1, num1, pos2, num2, num3, num4):
        self.selectLabel.config(text="STAGE " + str(stage) + "\nWHAT DOES THE DISPLAY SAYS?")
        self.firstButton.config(text="1",
                                command=lambda: self.stages(1, stage, pos1, num1, pos2, num2, num3, num4))
        self.secondButton.config(text="2",
                                 command=lambda: self.stages(2, stage, pos1, num1, pos2, num2, num3, num4
                                                             ))
        self.thirdButton.config(text="3",
                                command=lambda: self.stages(3, stage, pos1, num1, pos2, num2, num3, num4
                                                            ))
        self.fourthButton.config(text="4",
                                 command=lambda: self.stages(4, stage, pos1, num1, pos2, num2, num3, num4
                                                             ))
        self.firstButton.pack(side=LEFT, padx=10)
        self.secondButton.pack(side=LEFT, padx=10)
        self.thirdButton.pack(side=LEFT, padx=10)
        self.fourthButton.pack(side=LEFT, padx=10)

    def stages(self, display, stage, pos1, num1, pos2, num2, num3, num4):
        self.firstButton.pack(side=LEFT, padx=10)
        self.secondButton.pack(side=LEFT, padx=10)
        self.thirdButton.pack(side=LEFT, padx=10)
        self.fourthButton.pack(side=LEFT, padx=10)

        if stage == 1:
            self.resetButton.place(x=0, y=0)
            pos = ["", "SECOND", "SECOND", "THIRD", "FOURTH"]
            self.selectLabel.config(text="PRESS THE BUTTON IN THE {} POSITION AND"
                                         "\nSELECT THE LABEL IN THAT POSITION".format(pos[display]))
            self.firstButton.config(text="1",
                                    command=lambda: self.display_select(stage + 1,
                                                                        pos[display], 1,
                                                                        pos2, num2,
                                                                        num3,
                                                                        num4))
            self.secondButton.config(text="2",
                                     command=lambda: self.display_select(stage + 1,
                                                                         pos[display], 2,
                                                                         pos2, num2,
                                                                         num3,
                                                                         num4))
            self.thirdButton.config(text="3",
                                    command=lambda: self.display_select(stage + 1,
                                                                        pos[display], 3,
                                                                        pos2, num2,
                                                                        num3,
                                                                        num4))
            self.fourthButton.config(text="4",
                                     command=lambda: self.display_select(stage + 1,
                                                                         pos[display], 4,
                                                                         pos2, num2,
                                                                         num3,
                                                                         num4))

        elif stage == 2:
            if display == 1:
                self.selectLabel.config(text="PRESS THE BUTTON LABELED '4' AND"
                                             "\nSELECT THE POSITION OF THAT BUTTON")
                self.firstButton.config(text="FIRST POSITION",
                                        command=lambda: self.display_select(stage + 1,
                                                                            pos1, num1,
                                                                            "FIRST", 4,
                                                                            num3,
                                                                            num4))
                self.secondButton.config(text="SECOND POSITION",
                                         command=lambda: self.display_select(stage + 1,
                                                                             pos1, num1,
                                                                             "SECOND", 4,
                                                                             num3,
                                                                             num4))
                self.thirdButton.config(text="THIRD POSITION",
                                        command=lambda: self.display_select(stage + 1,
                                                                            pos1, num1,
                                                                            "THIRD", 4,
                                                                            num3,
                                                                            num4))
                self.fourthButton.config(text="FOURTH POSITION",
                                         command=lambda: self.display_select(stage + 1,
                                                                             pos1, num1,
                                                                             "FOURTH", 4,
                                                                             num3,
                                                                             num4))

            else:
                pos = [None, None, pos1, "FIRST", pos1]
                self.selectLabel.config(text="PRESS THE BUTTON IN THE {} POSITION AND"
                                             "\nSELECT THE LABEL IN THAT POSITION".format(pos[display]))
                self.firstButton.config(text="1",
                                        command=lambda: self.display_select(stage + 1,
                                                                            pos1, num1,
                                                                            pos[display], 1,
                                                                            num3,
                                                                            num4))
                self.secondButton.config(text="2",
                                         command=lambda: self.display_select(stage + 1,
                                                                             pos1, num1,
                                                                             pos[display], 2,
                                                                             num3,
                                                                             num4))
                self.thirdButton.config(text="3",
                                        command=lambda: self.display_select(stage + 1,
                                                                            pos1, num1,
                                                                            pos[display], 3,
                                                                            num3,
                                                                            num4))
                self.fourthButton.config(text="4",
                                         command=lambda: self.display_select(stage + 1,
                                                                             pos1, num1,
                                                                             pos[display], 4,
                                                                             num3,
                                                                             num4))

        elif stage == 3:
            if display == 3:
                self.selectLabel.config(text="PRESS THE BUTTON IN THE THIRD POSITION AND"
                                             "\nSELECT THE LABEL IN THAT POSITION")
                self.firstButton.config(text="1",
                                        command=lambda: self.display_select(stage + 1,
                                                                            pos1, num1,
                                                                            pos2, num2,
                                                                            1,
                                                                            num4))
                self.secondButton.config(text="2",
                                         command=lambda: self.display_select(stage + 1,
                                                                             pos1, num1,
                                                                             pos2, num2,
                                                                             2,
                                                                             num4))
                self.thirdButton.config(text="3",
                                        command=lambda: self.display_select(stage + 1,
                                                                            pos1, num1,
                                                                            pos2, num2,
                                                                            3,
                                                                            num4))
                self.fourthButton.config(text="4",
                                         command=lambda: self.display_select(stage + 1,
                                                                             pos1, num1,
                                                                             pos2, num2,
                                                                             4,
                                                                             num4))

            else:
                labels = ["", num2, num1, "", 4]
                self.selectLabel.config(text="PRESS THE BUTTON LABELED '{}'".format(labels[display]))

                self.firstButton.config(text="NEXT",
                                        command=lambda: self.display_select(stage + 1,
                                                                            pos1, num1,
                                                                            pos2, num2,
                                                                            labels[display],
                                                                            num4))
                self.secondButton.pack_forget()
                self.thirdButton.pack_forget()
                self.fourthButton.pack_forget()

        elif stage == 4:
            self.secondButton.pack(side=LEFT, padx=10)
            self.thirdButton.pack(side=LEFT, padx=10)
            self.fourthButton.pack(side=LEFT, padx=10)

            pos = ["", pos1, "FIRST", pos2, pos2]
            self.selectLabel.config(text="PRESS THE BUTTON IN THE {} POSITION AND\n"
                                         "SELECT THE LABEL IN THAT POSITION".format(pos[display]))
            self.firstButton.config(text="1",
                                    command=lambda: self.display_select(stage + 1,
                                                                        pos1, num1,
                                                                        pos2, num2,
                                                                        num3,
                                                                        1))
            self.secondButton.config(text="2",
                                     command=lambda: self.display_select(stage + 1,
                                                                         pos1, num1,
                                                                         pos2, num2,
                                                                         num3,
                                                                         2))
            self.thirdButton.config(text="3",
                                    command=lambda: self.display_select(stage + 1,
                                                                        pos1, num1,
                                                                        pos2, num2,
                                                                        num3,
                                                                        3))
            self.fourthButton.config(text="4",
                                     command=lambda: self.display_select(stage + 1,
                                                                         pos1, num1,
                                                                         pos2, num2,
                                                                         num3,
                                                                         4))
        elif stage == 5:
            self.firstButton.pack_forget()
            self.secondButton.pack_forget()
            self.thirdButton.pack_forget()
            self.fourthButton.pack_forget()
            labels = ["", num1, num2, num4, num3]
            self.selectLabel.config(text="PRESS THE BUTTON LABELED '{}'".format(labels[display]))
