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
        self.selectLabel = Label(self.passWin, font=self.manual_font, fg="white", bg=back,
                                 text="INSERT ALL THE LETTERS IN THE FIRST POSITION\n\n\n")

        self.infoLabel = Label(self.passWin, font=self.manual_font, fg="white", bg=back)

        self.nameLabel.pack(side=TOP, pady=30)
        self.selectLabel.pack(side=TOP, pady=30)

        self.letters = Entry(self.passWin, font=self.manual_font)
        self.letters.focus()

        self.nextButton = Button(self.passWin, font=self.manual_font, text="NEXT",
                                 command=lambda: self.passwords(0))

        self.active = []
        self.active2 = []
        self.all_passwords = [
            "about", "after", "again", "below", "could",
            "every", "first", "found", "great", "house",
            "large", "learn", "never", "other", "place",
            "plant", "point", "right", "small", "sound",
            "spell", "still", "study", "their", "there",
            "these", "thing", "think", "three", "water",
            "where", "which", "world", "would", "write"]

        self.letters.pack()
        self.nextButton.pack(pady=10)
        self.infoLabel.pack(pady=10)

        self.backButton = Button(self.passWin, text="BACK TO\nMODULE SELECT", font=("Terminal", 20),
                                 command=lambda: self.reset(0))
        self.resetButton = Button(self.passWin, text="RESET", font=("Terminal", 20),
                                  command=lambda: self.reset(1))

        self.backButton.pack(side=BOTTOM)

    def passwords(self, iterations):
        self.resetButton.place(x=0, y=0)
        times = ["SECOND", "THIRD", "FOURTH", "FIFTH"]
        self.selectLabel.config(text="INSERT ALL THE LETTERS IN THE " + times[iterations] + " POSITION\n\n\n")
        entry = str(self.letters.get().translate({ord(i): None for i in '-._/ 1234567890"' + "'"}).lower())
        if entry == "":
            self.selectLabel.config(text="INSERT ALL THE LETTERS IN THE FIRST POSITION\n"
                                         "MAKE SURE YOU WROTE ALL VALID LETTERS\n"
                                         "(NO NUMBERS, EMPTY SPACES OR SPECIAL CHARACTERS)\n"
                                         "EXAMPLE: a-b-c-d-e-f")
            return None

        self.active = [x for x in self.all_passwords if x[iterations] in entry]
        self.all_passwords = self.active
        if len(self.active) == 1:
            self.nextButton.pack_forget()
            self.letters.pack_forget()
            self.infoLabel.pack_forget()
            self.selectLabel.config(text="THE WORD IS: " + ''.join(self.active).upper())
        else:
            self.letters.delete(0, "end")
            self.infoLabel.config(text="POSSIBLE WORDS:\n" + ', '.join(self.active).upper())
            self.nextButton.config(command=lambda: self.passwords(iterations + 1))

