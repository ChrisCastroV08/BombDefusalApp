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

        self.topButtons = Frame(self.passWin, bg=back)

        self.nextButton = Button(self.topButtons, font=self.manual_font, text="NEXT",
                                 command=lambda: self.check_entry(False))
        self.returnButton = Button(self.topButtons, font=self.manual_font, text="BACK", state=DISABLED,
                                   command=lambda: self.check_entry(True))
        self.special = ''' `,~,!,@,#,$,%,^,&,*,(,),_,-,+,=,{,[,],},|,\\,:,;,",',<,,,>,.,?,/1234567890'''
        self.active = []

        self.old_letters = []
        self.old_possible = []
        self.times = 0
        self.all_passwords = [
            "about", "after", "again", "below", "could",
            "every", "first", "found", "great", "house",
            "large", "learn", "never", "other", "place",
            "plant", "point", "right", "small", "sound",
            "spell", "still", "study", "their", "there",
            "these", "thing", "think", "three", "water",
            "where", "which", "world", "would", "write"]

        self.letters.pack()
        self.topButtons.pack(pady=10)
        self.returnButton.pack(side=LEFT, padx=10)
        self.nextButton.pack(side=LEFT, padx=10)
        self.infoLabel.pack(pady=10)

        self.backButton = Button(self.passWin, text="BACK TO\nMODULE SELECT", font=("Terminal", 20),
                                 command=lambda: self.reset(0))
        self.resetButton = Button(self.passWin, text="RESET", font=("Terminal", 20),
                                  command=lambda: self.reset(1))

        self.backButton.pack(side=BOTTOM)

    def check_entry(self, back):
        times = ["FIRST", "SECOND", "THIRD", "FOURTH", "FIFTH"]
        if not back:
            entry = str(self.letters.get().translate({ord(i): None for i in self.special}).lower())
            if entry == "":
                self.selectLabel.config(text="INSERT ALL THE LETTERS IN THE {} POSITION\n"
                                             "MAKE SURE YOU WROTE ALL VALID LETTERS\n"
                                             "(NO NUMBERS, EMPTY SPACES OR SPECIAL CHARACTERS)\n"
                                             "EXAMPLE: abcdef".format(times[self.times]))
                return None
            self.selectLabel.config(text="INSERT ALL THE LETTERS IN THE {} POSITION\n\n\n".format(times[
                                                                                                      self.times + 1]))
            self.returnButton.config(state=NORMAL)
            self.old_letters.append(entry)
            if self.times == 0:
                self.active = [x for x in self.all_passwords if x[self.times] in self.old_letters[self.times]]
            else:
                self.active = [x for x in self.active if x[self.times] in self.old_letters[self.times]]
            self.old_possible.append(self.active)
            self.passwords(back)

        else:
            if isinstance(back, int):
                self.letters.pack()
                self.nextButton.pack(side=LEFT, padx=10)
                self.infoLabel.pack(pady=10)

            self.times -= 1
            self.selectLabel.config(text="INSERT ALL THE LETTERS IN THE {} POSITION\n\n\n".format(times[
                                                                                                      self.times]))
            self.letters.delete(0, "end")
            self.letters.insert(0, self.old_letters[self.times])
            del (self.old_letters[-1])
            self.active = self.old_possible[self.times - 1]
            del (self.old_possible[-1])
            self.passwords(back)

    def passwords(self, back):
        if len(self.active) == 1:
            self.nextButton.pack_forget()
            self.letters.pack_forget()
            self.infoLabel.pack_forget()
            self.returnButton.config(command=lambda: self.check_entry(1))
            self.selectLabel.config(text="THE WORD IS: " + ''.join(self.active).upper())
            self.letters.delete(0, "end")
            self.times += 1

        elif len(self.active) == 0:
            self.nextButton.pack_forget()
            self.letters.pack_forget()
            self.infoLabel.pack_forget()
            self.returnButton.config(command=lambda: self.check_entry(1))
            self.selectLabel.config(text="NO POSSIBLE MATCHES.\nMAKE SURE YOU INSERTED THE CORRECT LETTERS")
            self.letters.delete(0, "end")
            self.times += 1

        else:
            if len(self.active) >= 10:
                active = []
                for i in range(9):
                    active.append(self.active[i])
                self.infoLabel.config(text="POSSIBLE WORDS:\n" + '\n'.join(active).upper() +
                                           "\nAND {} MORE".format(len(self.active) - 9))
            else:
                self.infoLabel.config(text="POSSIBLE WORDS:\n" + '\n'.join(self.active).upper())

            if not back:
                self.letters.delete(0, "end")
                self.times += 1
            else:
                if self.times == 0:
                    self.infoLabel.config(text="POSSIBLE WORDS:")
                    self.returnButton.config(state=DISABLED)
                else:
                    self.returnButton.config(state=NORMAL)

    def back_button(self):
        self.times -= 1
        self.letters.insert(0, self.old_letters[self.times - 1])
        del (self.old_letters[-1])
        self.active = self.old_possible[self.times - 1]
        del (self.old_possible[-1])
        self.check_entry(True)

