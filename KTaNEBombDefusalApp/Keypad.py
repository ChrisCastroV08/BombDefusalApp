from tkinter import *
from PIL import ImageTk, Image


class Keypad:

    def reset(self, num):
        if num == 0:
            self.keypadWin.destroy()
        elif num == 1:
            self.keypadWin.destroy()
            self.__init__(self.root, self.back)

    def __init__(self, root, back):
        self.root = root
        self.back = back
        self.keypadWin = Toplevel(self.root)
        self.keypadWin.title("Keypads")
        self.keypadWin.resizable(False, False)
        self.keypadWin.config(bg=back)
        self.lftPos = (self.keypadWin.winfo_screenwidth() - 1000) / 2
        self.topPos = (self.keypadWin.winfo_screenheight() - 700) / 2
        self.keypadWin.geometry("%dx%d+%d+%d" % (1000, 700, self.lftPos, self.topPos))

        self.nameLabel = Label(self.keypadWin, font=("Terminal", 25), fg="white", bg=back,
                               text="ON THE SUBJECT OF KEYPADS")
        self.selectLabel = Label(self.keypadWin, font=("Terminal", 20), fg="white", bg=back,
                                 text="SELECT ALL FOUR SYMBOLS OF THE KEYPAD")
        self.topButtons = Frame(self.keypadWin, bg=back)
        self.topButtons2 = Frame(self.keypadWin, bg=back)
        self.bottomButtons = Frame(self.keypadWin, bg=back)
        self.bottomButtons2 = Frame(self.keypadWin, bg=back)
        self.labels = Frame(self.keypadWin, bg=back)
        self.nameLabel.pack(side=TOP, pady=30)
        self.selectLabel.pack(side=TOP, pady=30)

        self.firstSymbol = Label(self.labels, bg=back)
        self.secondSymbol = Label(self.labels, bg=back)
        self.thirdSymbol = Label(self.labels, bg=back)
        self.fourthSymbol = Label(self.labels, bg=back)

        self.topButtons.pack()
        self.topButtons2.pack(pady=10)
        self.bottomButtons.pack()
        self.bottomButtons2.pack(pady=10)

        self.img = Image.open("Images/KeypadSymbols.PNG")

        self.sym1, self.sym2, self.sym3, self.sym4, self.sym5, self.sym6, self.sym7 = \
            (self.img_crop(0, i) for i in range(7))

        self.sym8, self.sym9, self.sym10, self.sym11, self.sym12, self. sym13, self.sym14 = \
            (self.img_crop(1, i) for i in range(7))

        self.sym15, self.sym16, self.sym17, self.sym18, self.sym19, self.sym20, self.sym21 = \
            (self.img_crop(2, i) for i in range(7))

        self.sym22, self.sym23, self.sym24, self.sym25, self.sym26, self.sym27 = \
            (self.img_crop(3, i) for i in range(6))

        self.symbols = [self.sym1, self.sym2, self.sym3, self.sym4, self.sym5, self.sym6, self.sym7,
                        self.sym8, self.sym9, self.sym10, self.sym11, self.sym12, self. sym13, self.sym14,
                        self.sym15, self.sym16, self.sym17, self.sym18, self.sym19, self.sym20, self.sym21,
                        self.sym22, self.sym23, self.sym24, self.sym25, self.sym26, self.sym27]

        self.s1image, self.s2image, self.s3image, self.s4image, self.s5image, self.s6image, self.s7image,\
            self.s8image, self.s9image, self.s10image, self.s11image, self.s12image, self.s13image, self.s14image,\
            self.s15image, self.s16image, self.s17image, self.s18image, self.s19image, self.s20image, self.s21image,\
            self.s22image, self.s23image, self.s24image, self.s25image, self.s26image, self.s27image = \
            (ImageTk.PhotoImage(self.symbols[i]) for i in range(len(self.symbols)))

        self.images = [
            self.s1image, self.s2image, self.s3image, self.s4image, self.s5image, self.s6image, self.s7image,
            self.s8image, self.s9image, self.s10image, self.s11image, self.s12image, self.s13image, self.s14image,
            self.s15image, self.s16image, self.s17image, self.s18image, self.s19image, self.s20image, self.s21image,
            self.s22image, self.s23image, self.s24image, self.s25image, self.s26image, self.s27image]

        self.s1, self.s2, self.s3, self.s4, self.s5, self.s6, self.s7 = \
            (Button(self.topButtons, image=self.images[i], command=lambda x=i: self.on_off(x, True)) for i in range(7))

        self.s8, self.s9, self.s10, self.s11, self.s12, self.s13, self.s14, = \
            (Button(self.topButtons2, image=self.images[i + 7], command=lambda x=i + 7: self.on_off(x, True)) for i in
             range(7))

        self.s15, self.s16, self.s17, self.s18, self.s19, self.s20, self.s21, = \
            (Button(self.bottomButtons, image=self.images[i + 14],
                    command=lambda x=i + 14: self.on_off(x, True)) for i in range(7))

        self.s22, self.s23, self.s24, self.s25, self.s26, self.s27 = \
            (Button(self.bottomButtons2, image=self.images[i + 21],
                    command=lambda x=i + 21: self.on_off(x, True)) for i in range(6))

        self.buttons = [self.s1, self.s2, self.s3, self.s4, self.s5, self.s6, self.s7,
                        self.s8, self.s9, self.s10, self.s11, self.s12, self.s13, self.s14,
                        self.s15, self.s16, self.s17, self.s18, self.s19, self.s20, self.s21,
                        self.s22, self.s23, self.s24, self.s25, self.s26, self.s27]

        self.states = [False for i in range(27)]

        for i in range(len(self.buttons)):
            self.buttons[i].pack(side=LEFT, padx=5)

        self.nextButton = Button(self.keypadWin, text="NEXT", font=("Terminal", 20), state=DISABLED,
                                 command=lambda: self.compare(0))
        self.backButton = Button(self.keypadWin, text="BACK TO\nMODULE SELECT", font=("Terminal", 20),
                                 command=lambda: self.reset(0))
        self.resetButton = Button(self.keypadWin, text="RESET", font=("Terminal", 20),
                                  command=lambda: self.reset(1))
        self.nextButton.pack()
        self.backButton.pack(side=BOTTOM)

    def img_crop(self, i, j):
        left = i * 75
        right = i * 75 + 75
        upper = j * 75
        lower = j * 75 + 75
        return self.img.crop([left, upper, right, lower])

    def on_off(self, but, state):
        if state:
            self.buttons[but].config(bg="green", command=lambda: self.on_off(but, False))
        else:
            self.buttons[but].config(bg="lightgray", command=lambda: self.on_off(but, True))

        self.states[but] = state
        on = 0
        for i in range(len(self.states)):
            if self.states[i]:
                on = on + 1
        if on == 4:
            self.nextButton.config(state=NORMAL)
        else:
            self.nextButton.config(state=DISABLED)

    def compare(self, num):
        self.resetButton.place(x=0, y=0)
        pressed = []
        symbols = [[1, 2, 3, 4, 5, 6, 7],
                   [8, 1, 7, 11, 12, 6, 14],
                   [9, 13, 11, 10, 15, 3, 12],
                   [16, 17, 18, 5, 10, 14, 19],
                   [20, 19, 18, 22, 17, 23, 24],
                   [16, 8, 21, 25, 20, 26, 27]]
        possible = [
            [self.states[0], self.states[1], self.states[2], self.states[3], self.states[4], self.states[5],
             self.states[6]],
            [self.states[7], self.states[0], self.states[6], self.states[10], self.states[11], self.states[5],
             self.states[13]],
            [self.states[8], self.states[12], self.states[10], self.states[9], self.states[14], self.states[2],
             self.states[11]],
            [self.states[15], self.states[16], self.states[17], self.states[4], self.states[9], self.states[13],
             self.states[18]],
            [self.states[19], self.states[18], self.states[17], self.states[21], self.states[16], self.states[22],
             self.states[23]],
            [self.states[15], self.states[7], self.states[20], self.states[24], self.states[19], self.states[25],
             self.states[26]]
        ]
        images = [
            [self.s1image, self.s2image, self.s3image, self.s4image, self.s5image, self.s6image, self.s7image],
            [self.s8image, self.s1image, self.s7image, self.s11image, self.s12image, self.s6image, self.s14image],
            [self.s9image, self.s13image, self.s11image, self.s10image, self.s15image, self.s3image, self.s12image],
            [self.s16image, self.s17image, self.s18image, self.s5image, self.s10image, self.s14image, self.s19image],
            [self.s20image, self.s19image, self.s18image, self.s22image, self.s17image, self.s23image, self.s24image],
            [self.s16image, self.s8image, self.s21image, self.s25image, self.s20image, self.s26image, self.s27image]
        ]

        labels = [self.firstSymbol, self.secondSymbol, self.thirdSymbol, self.fourthSymbol]

        self.topButtons.pack_forget()
        self.topButtons2.pack_forget()
        self.bottomButtons.pack_forget()
        self.bottomButtons2.pack_forget()
        self.nextButton.pack_forget()
        self.labels.pack()

        for i in range(len(self.states)):
            if self.states[i]:
                pressed.append(i + 1)

        if pressed[0] in symbols[num] and pressed[1] in symbols[num] and pressed[2] in symbols[num] \
                and pressed[3] in symbols[num]:
            self.selectLabel.config(text="PRESS THE SYMBOLS IN THE ORDER THAT\nAPPEAR HERE (LEFT TO RIGHT)")
            lbl = 0
            for x in range(len(possible[num])):
                if possible[num][x]:
                    labels[lbl].config(image=images[num][x])
                    lbl = lbl + 1
            for y in range(len(labels)):
                labels[y].pack(side=LEFT)
        elif num != 5:
            self.compare(num + 1)
        else:
            self.firstSymbol.config(fg="white", font=("Terminal", 20), text="MAKE SURE YOU TYPED THE\nCORRECT SYMBOLS")
            self.firstSymbol.pack()
            self.selectLabel.config(text="THOSE SYMBOLS ARE NOT CORRELATED")
