from tkinter import *


class Passwords:

    def reset(self, num):
        if num == 0:
            self.passWin.destroy()
        elif num == 1:
            self.passWin.destroy()
            self.__init__(self.root, self.back, self.manual_font)

    def __init__(self, root, back, font):
        self.root = root
        self.back = back
        self.manual_font = font
        self.passWin = Toplevel(self.root)
        self.passWin.title("Passwords")
        self.passWin.resizable(False, False)
        self.passWin.config(bg=back)
        self.lftPos = (self.passWin.winfo_screenwidth() - 1000) / 2
        self.topPos = (self.passWin.winfo_screenheight() - 700) / 2
        self.passWin.geometry("%dx%d+%d+%d" % (1000, 700, self.lftPos, self.topPos))

        self.nameLabel = Label(self.passWin, font=("Terminal", 25), fg="white", bg=back,
                               text="ON THE SUBJECT OF PASSWORDS")
        self.selectLabel = Label(self.passWin, font=self.manual_font, fg="white", bg=back)

        self.nameLabel.pack(side=TOP, pady=30)
        self.selectLabel.pack(side=TOP, pady=30)

        self.letters = Entry(self.passWin, font=self.manual_font)

        self.nextButton = Button(self.passWin, font=self.manual_font, text="NEXT",
                                 command=lambda: self.ask_letters())

        self.letters.pack()
        self.nextButton.pack()

        self.backButton = Button(self.passWin, text="BACK TO\nMODULE SELECT", font=("Terminal", 20),
                                 command=lambda: self.reset(0))
        self.resetButton = Button(self.passWin, text="RESET", font=("Terminal", 20),
                                  command=lambda: self.reset(1))

        self.backButton.pack(side=BOTTOM)

    def ask_letters(self):
        word = self.letters.get().translate({ord(i): None for i in '-./ 1234567890'})

        print(list(word))
