from tkinter import *


# BIG THANKS TO USER ALBRECHT FOR THE IMPLEMENTATION OF THIS MORSE DECODER
def morse(txt):
    encrypt = {'A': '.-', 'B': '-...', 'C': '-.-.',
               'D': '-..', 'E': '.', 'F': '..-.',
               'G': '--.', 'H': '....', 'I': '..',
               'J': '.---', 'K': '-.-', 'L': '.-..',
               'M': '--', 'N': '-.', 'O': '---',
               'P': '.--.', 'Q': '--.-', 'R': '.-.',
               'S': '...', 'T': '-', 'U': '..-',
               'V': '...-', 'W': '.--', 'X': '-..-',
               'Y': '-.--', 'Z': '--..', ' ': '.....'}
    decrypt = {v: k for k, v in encrypt.items()}
    return ''.join(decrypt[i] for i in txt.split())


class MorseCode:

    def reset(self, num):
        if num == 0:
            self.morseCodeWin.destroy()
        elif num == 1:
            self.morseCodeWin.destroy()
            self.__init__(self.root, self.back, self.manual_font)

    def __init__(self, root, back, font):
        self.root = root
        self.back = back
        self.manual_font = font
        self.morseCodeWin = Toplevel(self.root)
        self.morseCodeWin.title("Complicated Wires")
        self.morseCodeWin.resizable(False, False)
        self.morseCodeWin.config(bg=back)
        self.lftPos = (self.morseCodeWin.winfo_screenwidth() - 1000) / 2
        self.topPos = (self.morseCodeWin.winfo_screenheight() - 700) / 2
        self.morseCodeWin.geometry("%dx%d+%d+%d" % (1000, 700, self.lftPos, self.topPos))

        self.nameLabel = Label(self.morseCodeWin, font=("Terminal", 25), fg="white", bg=back,
                               text="ON THE SUBJECT OF MORSE CODE")
        self.selectLabel = Label(self.morseCodeWin, font=self.manual_font, fg="white", bg=back)
        self.topButtons = Frame(self.morseCodeWin, bg=back)
        self.topButtons2 = Frame(self.morseCodeWin, bg=back)
        self.bottomButtons = Frame(self.morseCodeWin, bg=back)
        self.bottomButtons2 = Frame(self.morseCodeWin, bg=back)
        self.nameLabel.pack(side=TOP, pady=30)
        self.selectLabel.pack(side=TOP, pady=30)
        self.i = 0

        self.topButtons.pack()
        self.topButtons2.pack(pady=10)
        self.bottomButtons.pack()
        self.bottomButtons2.pack(pady=10)
        self.morseLabel = Label(self.morseCodeWin, font=self.manual_font, fg="white", bg=back)
        self.morseLabel.pack()
        self.letter_list = []
        self.letter_label = []

        self.firstButton = Button(self.topButtons, font=self.manual_font)
        self.secondButton = Button(self.topButtons, font=self.manual_font)
        self.thirdButton = Button(self.topButtons, font=self.manual_font)
        self.fourthButton = Button(self.topButtons, font=self.manual_font)

        self.fifthButton = Button(self.topButtons2, font=self.manual_font)
        self.sixthButton = Button(self.topButtons2, font=self.manual_font)
        self.seventhButton = Button(self.topButtons2, font=self.manual_font)
        self.eightButton = Button(self.topButtons2, font=self.manual_font)

        self.nineButton = Button(self.bottomButtons, font=self.manual_font)
        self.tenthButton = Button(self.bottomButtons, font=self.manual_font)
        self.elevenButton = Button(self.bottomButtons, font=self.manual_font)
        self.twelveButton = Button(self.bottomButtons, font=self.manual_font)

        self.thirteenButton = Button(self.bottomButtons2, font=self.manual_font)
        self.fourteenButton = Button(self.bottomButtons2, font=self.manual_font)
        self.fifteenButton = Button(self.bottomButtons2, font=self.manual_font)
        self.sixteenButton = Button(self.bottomButtons2, font=self.manual_font)

        self.firstButton.pack(side=LEFT, padx=10)
        self.secondButton.pack(side=LEFT, padx=10)
        self.thirdButton.pack(side=LEFT, padx=10)
        self.fifthButton.pack(side=LEFT, padx=10)
        self.sixthButton.pack(side=LEFT, padx=10)
        self.seventhButton.pack(side=LEFT, padx=10)

        self.backButton = Button(self.morseCodeWin, text="BACK TO\nMODULE SELECT", font=("Terminal", 20),
                                 command=lambda: self.reset(0))
        self.resetButton = Button(self.morseCodeWin, text="RESET", font=("Terminal", 20),
                                  command=lambda: self.reset(1))

        self.backButton.pack(side=BOTTOM)
        self.write()

    def word(self, string):
        if string != "clear" and string != "erase":
            self.letter_label.append(string)
            self.morseLabel.config(text=''.join(self.letter_label))
            if string == "/":
                self.letter_list.append(" ")
            else:
                self.letter_list.append(string)
        elif string == "erase":
            self.letter_label = self.letter_label[:-1]
            self.morseLabel.config(text=''.join(self.letter_label))
            self.letter_list = self.letter_list[:-1]
        else:
            self.letter_label.clear()
            self.letter_list.clear()
            self.morseLabel.config(text='')

    def write(self):
        self.selectLabel.config(text="WRITE THE LETTERS DESCRIBED BY THE MODULE\n"
                                     "EVERY LETTER NEEDS TO BE SEPARATED BY '/'\n"
                                     "MAKE SURE YOU START TYPING AFTER THE LONG PAUSE OF\n"
                                     "THE LIGHT IN THE MODULE\n"
                                     "IF YOU KNOW THE WORD, SIMPLY PRESS 'NEXT'")
        self.firstButton.config(text="-", command=lambda: self.word("-"))
        self.secondButton.config(text=".", command=lambda: self.word("."))
        self.thirdButton.config(text="/", command=lambda: self.word("/"))
        self.fifthButton.config(text="CLEAR", command=lambda: self.word("clear"), fg="red")
        self.sixthButton.config(text="ERASE", command=lambda: self.word("erase"))
        self.seventhButton.config(text="NEXT", command=lambda: self.detect(''.join(self.letter_list)), fg="green")

    def detect(self, txt):
        self.resetButton.place(x=0, y=0)
        buttons = [self.firstButton, self.secondButton, self.thirdButton, self.fourthButton,
                   self.fifthButton, self.sixthButton, self.seventhButton, self.eightButton,
                   self.nineButton, self.tenthButton, self.elevenButton, self.twelveButton,
                   self.thirteenButton, self.fourteenButton, self.fifteenButton, self.sixteenButton]
        but_config = [("SHELL", lambda: self.frequency(0)),
                      ("HALLS", lambda: self.frequency(1)),
                      ("SLICK", lambda: self.frequency(2)),
                      ("TRICK", lambda: self.frequency(3)),
                      ("BOXES", lambda: self.frequency(4)),
                      ("LEAKS", lambda: self.frequency(5)),
                      ("STROBE", lambda: self.frequency(6)),
                      ("BISTRO", lambda: self.frequency(7)),
                      ("FLICK", lambda: self.frequency(8)),
                      ("BOMBS", lambda: self.frequency(9)),
                      ("BREAK", lambda: self.frequency(10)),
                      ("BRICK", lambda: self.frequency(11)),
                      ("STEAK", lambda: self.frequency(12)),
                      ("STING", lambda: self.frequency(13)),
                      ("VECTOR", lambda: self.frequency(14)),
                      ("BEATS", lambda: self.frequency(15))]

        word = ""
        if txt != "":
            try:
                word = morse(txt)
            except KeyError:
                self.selectLabel.config(text="MAKE SURE YOU TYPED\nTHE CORRECT MORSE CODE")
                self.topButtons.pack_forget()
                self.bottomButtons.pack_forget()
            self.selectLabel.config(text="THE WORD IS " + word + "\n"
                                                                 "SELECT THE WORD THAT MATCHES THE BEST")
        else:
            self.selectLabel.config(text="SELECT THE WORD THAT MATCHES THE BEST")
        i = 0
        for btn in but_config:
            buttons[i].config(text=btn[0], command=btn[1], fg="black")
            buttons[i].pack(side=LEFT, padx=10)
            i = i + 1

    def frequency(self, num):
        self.topButtons.pack_forget()
        self.topButtons2.pack_forget()
        self.bottomButtons.pack_forget()
        self.bottomButtons2.pack_forget()
        info = [["SHELL", "HALLS", "SLICK", "TRICK",
                 "BOXES", "LEAKS", "STROBE", 'BISTRO',
                 'FLICK', 'BOMBS', 'BREAK', 'BRICK',
                 'STEAK', 'STING', 'VECTOR', 'BEATS'],
                [505, 515, 522, 532,
                 535, 542, 545, 552,
                 555, 565, 572, 575,
                 582, 592, 595, 600]]
        for i in range(len(info[0])):
            if num == i:
                self.selectLabel.config(text="THE CHOSEN WORD IS " + info[0][i] +
                                             "\nAND RESPONDS TO THE FREQUENCY 3." + str(info[1][i]) + "MHz")
                break
