from tkinter import *
from tkinter.font import Font
from PIL import ImageTk, Image

but1state, but2state, but3state, but4state, but5state, but6state, but7state, but8state, \
 but9state, but10state, but11state, but12state, but13state, but14state, but15state, but16state, \
 but17state, but18state, but19state, but20state, but21state, but22state, but23state, but24state, \
 but25state, but26state, but27state = (False for i in range(27))


def clear():
    global but1state, but2state, but3state, but4state, \
        but5state, but6state, but7state, but8state, \
        but9state, but10state, but11state, but12state, \
        but13state, but14state, but15state, but16state, \
        but17state, but18state, but19state, but20state, \
        but21state, but22state, but23state, but24state, \
        but25state, but26state, but27state

    but1state, but2state, but3state, but4state, but5state, but6state, but7state, but8state, \
      but9state, but10state, but11state, but12state, but13state, but14state, but15state, but16state, \
      but17state, but18state, but19state, but20state, but21state, but22state, but23state, but24state, \
      but25state, but26state, but27state = (False for i in range(27))


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

        self.manual_font = Font(
            family="Terminal",
            size=20)

        self.nameLabel = Label(self.keypadWin, font=("Terminal", 25), fg="white", bg=back,
                               text="ON THE SUBJECT OF KEYPADS")
        self.selectLabel = Label(self.keypadWin, font=("Terminal", 20), fg="white", bg=back,
                                 text="SELECT ALL FOUR SYMBOLS OF THE KEYPAD")
        self.topButtons = Frame(self.keypadWin, bg=back)
        self.topButtons2 = Frame(self.keypadWin, bg=back)
        self.bottomButtons = Frame(self.keypadWin, bg=back)
        self.bottomButtons2 = Frame(self.keypadWin, bg=back)
        self.labels = Frame(self.keypadWin, bg=back)
        self.nextButton = Button(self.keypadWin, text="NEXT", font=("Terminal", 20), state=DISABLED)
        self.nameLabel.pack(side=TOP, pady=30)
        self.selectLabel.pack(side=TOP, pady=30)

        self.firstSymbol = Label(self.labels, bg=back)
        self.secondSymbol = Label(self.labels, bg=back)
        self.thirdSymbol = Label(self.labels, bg=back)
        self.fourthSymbol = Label(self.labels, bg=back)
        self.fifthSymbol = Label(self.labels, bg=back)
        self.sixthSymbol = Label(self.labels, bg=back)
        self.seventhSymbol = Label(self.labels, bg=back)

        self.topButtons.pack()
        self.topButtons2.pack(pady=10)
        self.bottomButtons.pack()
        self.bottomButtons2.pack(pady=10)
        self.nextButton.pack()

        self.img = Image.open("Images/KeypadSymbols.PNG")

        self.sym1 = self.img_crop(0, 0)
        self.sym2 = self.img_crop(0, 1)
        self.sym3 = self.img_crop(0, 2)
        self.sym4 = self.img_crop(0, 3)
        self.sym5 = self.img_crop(0, 4)
        self.sym6 = self.img_crop(0, 5)
        self.sym7 = self.img_crop(0, 6)
        self.sym8 = self.img_crop(1, 0)
        self.sym9 = self.img_crop(1, 1)
        self.sym10 = self.img_crop(1, 2)
        self.sym11 = self.img_crop(1, 3)
        self.sym12 = self.img_crop(1, 4)
        self.sym13 = self.img_crop(1, 5)
        self.sym14 = self.img_crop(1, 6)
        self.sym15 = self.img_crop(2, 0)
        self.sym16 = self.img_crop(2, 1)
        self.sym17 = self.img_crop(2, 2)
        self.sym18 = self.img_crop(2, 3)
        self.sym19 = self.img_crop(2, 4)
        self.sym20 = self.img_crop(2, 5)
        self.sym21 = self.img_crop(2, 6)
        self.sym22 = self.img_crop(3, 0)
        self.sym23 = self.img_crop(3, 2)
        self.sym24 = self.img_crop(3, 3)
        self.sym25 = self.img_crop(3, 4)
        self.sym26 = self.img_crop(3, 5)
        self.sym27 = self.img_crop(3, 6)

        self.s1image = ImageTk.PhotoImage(self.sym1)
        self.s2image = ImageTk.PhotoImage(self.sym2)
        self.s3image = ImageTk.PhotoImage(self.sym3)
        self.s4image = ImageTk.PhotoImage(self.sym4)
        self.s5image = ImageTk.PhotoImage(self.sym5)
        self.s6image = ImageTk.PhotoImage(self.sym6)
        self.s7image = ImageTk.PhotoImage(self.sym7)
        self.s8image = ImageTk.PhotoImage(self.sym8)
        self.s9image = ImageTk.PhotoImage(self.sym9)
        self.s10image = ImageTk.PhotoImage(self.sym10)
        self.s11image = ImageTk.PhotoImage(self.sym11)
        self.s12image = ImageTk.PhotoImage(self.sym12)
        self.s13image = ImageTk.PhotoImage(self.sym13)
        self.s14image = ImageTk.PhotoImage(self.sym14)
        self.s15image = ImageTk.PhotoImage(self.sym15)
        self.s16image = ImageTk.PhotoImage(self.sym16)
        self.s17image = ImageTk.PhotoImage(self.sym17)
        self.s18image = ImageTk.PhotoImage(self.sym18)
        self.s19image = ImageTk.PhotoImage(self.sym19)
        self.s20image = ImageTk.PhotoImage(self.sym20)
        self.s21image = ImageTk.PhotoImage(self.sym21)
        self.s22image = ImageTk.PhotoImage(self.sym22)
        self.s23image = ImageTk.PhotoImage(self.sym23)
        self.s24image = ImageTk.PhotoImage(self.sym24)
        self.s25image = ImageTk.PhotoImage(self.sym25)
        self.s26image = ImageTk.PhotoImage(self.sym26)
        self.s27image = ImageTk.PhotoImage(self.sym27)

        self.s1 = Button(self.topButtons, image=self.s1image, command=lambda: self.on(1))
        self.s2 = Button(self.topButtons, image=self.s2image, command=lambda: self.on(2))
        self.s3 = Button(self.topButtons, image=self.s3image, command=lambda: self.on(3))
        self.s4 = Button(self.topButtons, image=self.s4image, command=lambda: self.on(4))
        self.s5 = Button(self.topButtons, image=self.s5image, command=lambda: self.on(5))
        self.s6 = Button(self.topButtons, image=self.s6image, command=lambda: self.on(6))
        self.s7 = Button(self.topButtons, image=self.s7image, command=lambda: self.on(7))
        self.s8 = Button(self.topButtons2, image=self.s8image, command=lambda: self.on(8))
        self.s9 = Button(self.topButtons2, image=self.s9image, command=lambda: self.on(9))
        self.s10 = Button(self.topButtons2, image=self.s10image, command=lambda: self.on(10))
        self.s11 = Button(self.topButtons2, image=self.s11image, command=lambda: self.on(11))
        self.s12 = Button(self.topButtons2, image=self.s12image, command=lambda: self.on(12))
        self.s13 = Button(self.topButtons2, image=self.s13image, command=lambda: self.on(13))
        self.s14 = Button(self.topButtons2, image=self.s14image, command=lambda: self.on(14))
        self.s15 = Button(self.bottomButtons, image=self.s15image, command=lambda: self.on(15))
        self.s16 = Button(self.bottomButtons, image=self.s16image, command=lambda: self.on(16))
        self.s17 = Button(self.bottomButtons, image=self.s17image, command=lambda: self.on(17))
        self.s18 = Button(self.bottomButtons, image=self.s18image, command=lambda: self.on(18))
        self.s19 = Button(self.bottomButtons, image=self.s19image, command=lambda: self.on(19))
        self.s20 = Button(self.bottomButtons, image=self.s20image, command=lambda: self.on(20))
        self.s21 = Button(self.bottomButtons, image=self.s21image, command=lambda: self.on(21))
        self.s22 = Button(self.bottomButtons2, image=self.s22image, command=lambda: self.on(22))
        self.s23 = Button(self.bottomButtons2, image=self.s23image, command=lambda: self.on(23))
        self.s24 = Button(self.bottomButtons2, image=self.s24image, command=lambda: self.on(24))
        self.s25 = Button(self.bottomButtons2, image=self.s25image, command=lambda: self.on(25))
        self.s26 = Button(self.bottomButtons2, image=self.s26image, command=lambda: self.on(26))
        self.s27 = Button(self.bottomButtons2, image=self.s27image, command=lambda: self.on(27))

        self.s1.pack(side=LEFT, padx=5)
        self.s2.pack(side=LEFT, padx=5)
        self.s3.pack(side=LEFT, padx=5)
        self.s4.pack(side=LEFT, padx=5)
        self.s5.pack(side=LEFT, padx=5)
        self.s6.pack(side=LEFT, padx=5)
        self.s7.pack(side=LEFT, padx=5)
        self.s8.pack(side=LEFT, padx=5)
        self.s9.pack(side=LEFT, padx=5)
        self.s10.pack(side=LEFT, padx=5)
        self.s11.pack(side=LEFT, padx=5)
        self.s12.pack(side=LEFT, padx=5)
        self.s13.pack(side=LEFT, padx=5)
        self.s14.pack(side=LEFT, padx=5)
        self.s15.pack(side=LEFT, padx=5)
        self.s16.pack(side=LEFT, padx=5)
        self.s17.pack(side=LEFT, padx=5)
        self.s18.pack(side=LEFT, padx=5)
        self.s19.pack(side=LEFT, padx=5)
        self.s20.pack(side=LEFT, padx=5)
        self.s21.pack(side=LEFT, padx=5)
        self.s22.pack(side=LEFT, padx=5)
        self.s23.pack(side=LEFT, padx=5)
        self.s24.pack(side=LEFT, padx=5)
        self.s25.pack(side=LEFT, padx=5)
        self.s26.pack(side=LEFT, padx=5)
        self.s27.pack(side=LEFT, padx=5)

        self.backButton = Button(self.keypadWin, text="BACK TO\nMODULE SELECT", font=("Terminal", 20),
                                 command=lambda: self.reset(0))
        self.resetButton = Button(self.keypadWin, text="RESET", font=("Terminal", 20),
                                  command=lambda: self.reset(1))

        self.backButton.pack(side=BOTTOM)
        clear()

    def img_crop(self, i, j):
        left = i * 75
        right = i * 75 + 76
        upper = j * 74
        lower = j * 74 + 75
        return self.img.crop([left, upper, right, lower])

    def activate(self, button_list):
        on = 0
        for i in range(len(button_list)):
            if button_list[i] is True:
                on = on + 1

        if on == 4:
            self.nextButton.config(state=NORMAL, command=lambda: self.compare(button_list))
        else:
            self.nextButton.config(state=DISABLED)

    def compare(self, buttons):
        self.resetButton.place(x=0, y=0)
        pressed = []
        symbols = [[1, 2, 3, 4, 5, 6, 7],
                   [8, 1, 7, 11, 12, 6, 14],
                   [9, 13, 11, 10, 15, 3, 12],
                   [16, 17, 18, 5, 10, 14, 19],
                   [20, 19, 18, 22, 17, 23, 24],
                   [16, 8, 21, 25, 20, 26, 27]]
        global but1state, but2state, but3state, but4state, \
            but5state, but6state, but7state, but8state, \
            but9state, but10state, but11state, but12state, \
            but13state, but14state, but15state, but16state, \
            but17state, but18state, but19state, but20state, \
            but21state, but22state, but23state, but24state, \
            but25state, but26state, but27state
        self.selectLabel.config(text="PRESS THE SYMBOLS IN THE ORDER THAT\nAPPEAR HERE (LEFT TO RIGHT)")
        self.topButtons.pack_forget()
        self.topButtons2.pack_forget()
        self.bottomButtons.pack_forget()
        self.bottomButtons2.pack_forget()
        self.nextButton.pack_forget()
        self.labels.pack()

        for i in range(len(buttons)):
            if buttons[i]:
                pressed.append(i + 1)

        # FIRST COLUMN OF SYMBOLS
        if pressed[0] in symbols[0] and pressed[1] in symbols[0] and pressed[2] in symbols[0] \
                and pressed[3] in symbols[0]:
            possible = [but1state, but2state, but3state, but4state, but5state, but6state, but7state]
            images = [self.s1image, self.s2image, self.s3image, self.s4image, self.s5image, self.s6image, self.s7image]
            labels = [self.firstSymbol, self.secondSymbol, self.thirdSymbol, self.fourthSymbol]
            lbl = 0
            for x in range(len(possible)):
                if possible[x]:
                    labels[lbl].config(image=images[x])
                    lbl = lbl + 1
            for y in range(len(labels)):
                labels[y].pack(side=LEFT)
        # SECOND COLUMN OF SYMBOLS
        elif pressed[0] in symbols[1] and pressed[1] in symbols[1] and pressed[2] in symbols[1] \
                and pressed[3] in symbols[1]:
            possible = [but8state, but1state, but7state, but11state, but12state, but6state, but14state]
            images = [self.s8image, self.s1image, self.s7image, self.s11image, self.s12image, self.s6image,
                      self.s14image]
            labels = [self.firstSymbol, self.secondSymbol, self.thirdSymbol, self.fourthSymbol]
            lbl = 0
            for x in range(len(possible)):
                if possible[x]:
                    labels[lbl].config(image=images[x])
                    lbl = lbl + 1
            for y in range(len(labels)):
                labels[y].pack(side=LEFT)
        # THIRD COLUMN OF SYMBOLS
        elif pressed[0] in symbols[2] and pressed[1] in symbols[2] and pressed[2] in symbols[2] \
                and pressed[3] in symbols[2]:
            possible = [but9state, but13state, but11state, but10state, but15state, but3state, but12state]
            images = [self.s9image, self.s13image, self.s11image, self.s10image, self.s15image, self.s3image,
                      self.s12image]
            labels = [self.firstSymbol, self.secondSymbol, self.thirdSymbol, self.fourthSymbol]
            lbl = 0
            for x in range(len(possible)):
                if possible[x]:
                    labels[lbl].config(image=images[x])
                    lbl = lbl + 1
            for y in range(len(labels)):
                labels[y].pack(side=LEFT)
        # FOURTH COLUMN OF SYMBOLS
        elif pressed[0] in symbols[3] and pressed[1] in symbols[3] and pressed[2] in symbols[3] \
                and pressed[3] in symbols[3]:
            possible = [but16state, but17state, but18state, but5state, but10state, but14state, but19state]
            images = [self.s16image, self.s17image, self.s18image, self.s5image, self.s10image, self.s14image,
                      self.s19image]
            labels = [self.firstSymbol, self.secondSymbol, self.thirdSymbol, self.fourthSymbol]
            lbl = 0
            for x in range(len(possible)):
                if possible[x]:
                    labels[lbl].config(image=images[x])
                    lbl = lbl + 1
            for y in range(len(labels)):
                labels[y].pack(side=LEFT)
        # FIFTH COLUMN OF SYMBOLS
        elif pressed[0] in symbols[4] and pressed[1] in symbols[4] and pressed[2] in symbols[4] \
                and pressed[3] in symbols[4]:
            possible = [but20state, but19state, but18state, but22state, but17state, but23state, but24state]
            images = [self.s20image, self.s19image, self.s18image, self.s22image, self.s17image, self.s23image,
                      self.s24image]
            labels = [self.firstSymbol, self.secondSymbol, self.thirdSymbol, self.fourthSymbol]
            lbl = 0
            for x in range(len(possible)):
                if possible[x]:
                    labels[lbl].config(image=images[x])
                    lbl = lbl + 1
            for y in range(len(labels)):
                labels[y].pack(side=LEFT)
        # SIXTH COLUMN OF SYMBOLS
        elif pressed[0] in symbols[5] and pressed[1] in symbols[5] and pressed[2] in symbols[5] \
                and pressed[3] in symbols[5]:
            possible = [but16state, but8state, but21state, but25state, but20state, but26state, but27state]
            images = [self.s16image, self.s8image, self.s21image, self.s25image, self.s20image, self.s26image,
                      self.s27image]
            labels = [self.firstSymbol, self.secondSymbol, self.thirdSymbol, self.fourthSymbol]
            lbl = 0
            for x in range(len(possible)):
                if possible[x]:
                    labels[lbl].config(image=images[x])
                    lbl = lbl + 1
            for y in range(len(labels)):
                labels[y].pack(side=LEFT)
        else:
            self.firstSymbol.config(fg="white", font=("Terminal", 20), text="MAKE SURE YOU TYPED THE\nCORRECT SYMBOLS")
            self.firstSymbol.pack()
            self.selectLabel.config(text="THOSE SYMBOLS ARE NOT CORRELATED")

    def on(self, but):
        global but1state, but2state, but3state, but4state, \
            but5state, but6state, but7state, but8state, \
            but9state, but10state, but11state, but12state, \
            but13state, but14state, but15state, but16state, \
            but17state, but18state, but19state, but20state, \
            but21state, but22state, but23state, but24state, \
            but25state, but26state, but27state

        if but == 1:
            self.s1.config(bg="green", command=lambda: self.off(1))
            but1state = True

        elif but == 2:
            self.s2.config(bg="green", command=lambda: self.off(2))
            but2state = True
        elif but == 3:
            self.s3.config(bg="green", command=lambda: self.off(3))
            but3state = True
        elif but == 4:
            self.s4.config(bg="green", command=lambda: self.off(4))
            but4state = True
        elif but == 5:
            self.s5.config(bg="green", command=lambda: self.off(5))
            but5state = True
        elif but == 6:
            self.s6.config(bg="green", command=lambda: self.off(6))
            but6state = True
        elif but == 7:
            self.s7.config(bg="green", command=lambda: self.off(7))
            but7state = True
        elif but == 8:
            self.s8.config(bg="green", command=lambda: self.off(8))
            but8state = True
        elif but == 9:
            self.s9.config(bg="green", command=lambda: self.off(9))
            but9state = True
        elif but == 10:
            self.s10.config(bg="green", command=lambda: self.off(10))
            but10state = True
        elif but == 11:
            self.s11.config(bg="green", command=lambda: self.off(11))
            but11state = True
        elif but == 12:
            self.s12.config(bg="green", command=lambda: self.off(12))
            but12state = True
        elif but == 13:
            self.s13.config(bg="green", command=lambda: self.off(13))
            but13state = True
        elif but == 14:
            self.s14.config(bg="green", command=lambda: self.off(14))
            but14state = True
        elif but == 15:
            self.s15.config(bg="green", command=lambda: self.off(15))
            but15state = True
        elif but == 16:
            self.s16.config(bg="green", command=lambda: self.off(16))
            but16state = True
        elif but == 17:
            self.s17.config(bg="green", command=lambda: self.off(17))
            but17state = True
        elif but == 18:
            self.s18.config(bg="green", command=lambda: self.off(18))
            but18state = True
        elif but == 19:
            self.s19.config(bg="green", command=lambda: self.off(19))
            but19state = True
        elif but == 20:
            self.s20.config(bg="green", command=lambda: self.off(20))
            but20state = True
        elif but == 21:
            self.s21.config(bg="green", command=lambda: self.off(21))
            but21state = True
        elif but == 22:
            self.s22.config(bg="green", command=lambda: self.off(22))
            but22state = True
        elif but == 23:
            self.s23.config(bg="green", command=lambda: self.off(23))
            but23state = True
        elif but == 24:
            self.s24.config(bg="green", command=lambda: self.off(24))
            but24state = True
        elif but == 25:
            self.s25.config(bg="green", command=lambda: self.off(25))
            but25state = True
        elif but == 26:
            self.s26.config(bg="green", command=lambda: self.off(26))
            but26state = True
        elif but == 27:
            self.s27.config(bg="green", command=lambda: self.off(27))
            but27state = True

        states = [but1state, but2state, but3state, but4state,
                  but5state, but6state, but7state, but8state,
                  but9state, but10state, but11state, but12state,
                  but13state, but14state, but15state, but16state,
                  but17state, but18state, but19state, but20state,
                  but21state, but22state, but23state, but24state,
                  but25state, but26state, but27state]
        self.activate(states)

    def off(self, but):
        global but1state, but2state, but3state, but4state, \
            but5state, but6state, but7state, but8state, \
            but9state, but10state, but11state, but12state, \
            but13state, but14state, but15state, but16state, \
            but17state, but18state, but19state, but20state, \
            but21state, but22state, but23state, but24state, \
            but25state, but26state, but27state

        if but == 1:
            self.s1.config(bg="lightgray", command=lambda: self.on(1))
            but1state = False
        elif but == 2:
            self.s2.config(bg="lightgray", command=lambda: self.on(2))
            but2state = False
        elif but == 3:
            self.s3.config(bg="lightgray", command=lambda: self.on(3))
            but3state = False
        elif but == 4:
            self.s4.config(bg="lightgray", command=lambda: self.on(4))
            but4state = False
        elif but == 5:
            self.s5.config(bg="lightgray", command=lambda: self.on(5))
            but5state = False
        elif but == 6:
            self.s6.config(bg="lightgray", command=lambda: self.on(6))
            but6state = False
        elif but == 7:
            self.s7.config(bg="lightgray", command=lambda: self.on(7))
            but7state = False
        elif but == 8:
            self.s8.config(bg="lightgray", command=lambda: self.on(8))
            but8state = False
        elif but == 9:
            self.s9.config(bg="lightgray", command=lambda: self.on(9))
            but9state = False
        elif but == 10:
            self.s10.config(bg="lightgray", command=lambda: self.on(10))
            but10state = False
        elif but == 11:
            self.s11.config(bg="lightgray", command=lambda: self.on(11))
            but11state = False
        elif but == 12:
            self.s12.config(bg="lightgray", command=lambda: self.on(12))
            but12state = False
        elif but == 13:
            self.s13.config(bg="lightgray", command=lambda: self.on(13))
            but13state = False
        elif but == 14:
            self.s14.config(bg="lightgray", command=lambda: self.on(14))
            but14state = False
        elif but == 15:
            self.s15.config(bg="lightgray", command=lambda: self.on(15))
            but15state = False
        elif but == 16:
            self.s16.config(bg="lightgray", command=lambda: self.on(16))
            but16state = False
        elif but == 17:
            self.s17.config(bg="lightgray", command=lambda: self.on(17))
            but17state = False
        elif but == 18:
            self.s18.config(bg="lightgray", command=lambda: self.on(18))
            but18state = False
        elif but == 19:
            self.s19.config(bg="lightgray", command=lambda: self.on(19))
            but19state = False
        elif but == 20:
            self.s20.config(bg="lightgray", command=lambda: self.on(20))
            but20state = False
        elif but == 21:
            self.s21.config(bg="lightgray", command=lambda: self.on(21))
            but21state = False
        elif but == 22:
            self.s22.config(bg="lightgray", command=lambda: self.on(22))
            but22state = False
        elif but == 23:
            self.s23.config(bg="lightgray", command=lambda: self.on(23))
            but23state = False
        elif but == 24:
            self.s24.config(bg="lightgray", command=lambda: self.on(24))
            but24state = False
        elif but == 25:
            self.s25.config(bg="lightgray", command=lambda: self.on(25))
            but25state = False
        elif but == 26:
            self.s26.config(bg="lightgray", command=lambda: self.on(26))
            but26state = False
        elif but == 27:
            self.s27.config(bg="lightgray", command=lambda: self.on(27))
            but27state = False

        states = [but1state, but2state, but3state, but4state,
                  but5state, but6state, but7state, but8state,
                  but9state, but10state, but11state, but12state,
                  but13state, but14state, but15state, but16state,
                  but17state, but18state, but19state, but20state,
                  but21state, but22state, but23state, but24state,
                  but25state, but26state, but27state]
        self.activate(states)
