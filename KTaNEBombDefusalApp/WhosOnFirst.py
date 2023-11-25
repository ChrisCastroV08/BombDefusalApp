from tkinter import *
from PIL import ImageTk, Image


class WhosOnFirst:

    def reset(self, num):
        if num == 0:
            self.whoOnFirstWin.destroy()
        elif num == 1:
            self.whoOnFirstWin.destroy()
            self.__init__(self.root, self.back, self.manual_font)

    def __init__(self, root, back, font):
        self.root = root
        self.back = back
        self.manual_font = font
        self.whoOnFirstWin = Toplevel(self.root)
        self.whoOnFirstWin.title("Who's On First")
        self.whoOnFirstWin.resizable(False, False)
        self.whoOnFirstWin.config(bg=back)
        self.lftPos = (self.whoOnFirstWin.winfo_screenwidth() - 1000) / 2
        self.topPos = (self.whoOnFirstWin.winfo_screenheight() - 700) / 2
        self.whoOnFirstWin.geometry("%dx%d+%d+%d" % (1000, 700, self.lftPos, self.topPos))

        self.nameLabel = Label(self.whoOnFirstWin, font=("Terminal", 25), fg="white", bg=back,
                               text="ON THE SUBJECT OF WHO'S ON FIRST")
        self.selectLabel = Label(self.whoOnFirstWin, font=self.manual_font, fg="white", bg=back,
                                 text="WHAT WORD DOES THE DISPLAY SAYS?")
        self.answerLabel = Label(self.whoOnFirstWin, bg=back, fg="white", font=self.manual_font)
        self.topButtons = Frame(self.whoOnFirstWin, bg=back)
        self.bottomButtons = Frame(self.whoOnFirstWin, bg=back)
        self.topButtons2 = Frame(self.whoOnFirstWin, bg=back)
        self.bottomButtons2 = Frame(self.whoOnFirstWin, bg=back)

        self.img = Image.open("Images/WhosOnFirstWords.png")

        self.sym1 = self.img_crop(0)
        self.sym2 = self.img_crop(1)
        self.sym3 = self.img_crop(2)
        self.sym4 = self.img_crop(3)
        self.sym5 = self.img_crop(4)
        self.sym6 = self.img_crop(5)
        self.sym7 = self.img_crop(6)
        self.sym8 = self.img_crop(7)
        self.sym9 = self.img_crop(8)
        self.sym10 = self.img_crop(9)
        self.sym11 = self.img_crop(10)
        self.sym12 = self.img_crop(11)
        self.sym13 = self.img_crop(12)
        self.sym14 = self.img_crop(13)
        self.sym15 = self.img_crop(14)
        self.sym16 = self.img_crop(15)
        self.sym17 = self.img_crop(16)
        self.sym18 = self.img_crop(17)
        self.sym19 = self.img_crop(18)
        self.sym20 = self.img_crop(19)
        self.sym21 = self.img_crop(20)
        self.sym22 = self.img_crop(21)
        self.sym23 = self.img_crop(22)
        self.sym24 = self.img_crop(23)
        self.sym25 = self.img_crop(24)
        self.sym26 = self.img_crop(25)
        self.sym27 = self.img_crop(26)
        self.sym28 = self.img_crop(27)

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
        self.s28image = ImageTk.PhotoImage(self.sym28)

        self.nameLabel.pack(side=TOP, pady=30)
        self.selectLabel.pack(side=TOP, pady=30)

        self.topButtons.pack()
        self.topButtons2.pack(pady=10)
        self.bottomButtons.pack()
        self.bottomButtons2.pack(pady=10)
        step1 = [["YES", "FIRST", "DISPLAY", "OKAY", "SAYS", "NOTHING", "      "],
                 ['BLANK', 'NO', 'LED', 'LEAD', 'READ', 'RED', 'REED'],
                 ['LEED', 'HOLD ON', 'YOU', 'YOU ARE', 'YOUR', "YOU'RE", 'UR'],
                 ["THERE", "THEY'RE", "THEIR", "THEY ARE", "SEE", "C", "CEE"]]

        self.word1, self.word2, self.word3, self.word4, self.word5, self.word6, self.word7 =\
            (Button(self.topButtons, font=self.manual_font, text=step1[0][i]) for i in range(7))
        self.word8, self.word9, self.word10, self.word11, self.word12, self.word13, self.word14 = \
            (Button(self.topButtons2, font=self.manual_font, text=step1[1][i]) for i in range(7))
        self.word15, self.word16, self.word17, self.word18, self.word19, self.word20, self.word21 = \
            (Button(self.bottomButtons, font=self.manual_font, text=step1[2][i]) for i in range(7))
        self.word22, self.word23, self.word24, self.word25, self.word26, self.word27, self.word28 = \
            (Button(self.bottomButtons2, font=self.manual_font, text=step1[3][i]) for i in range(7))

        self.buttons = [self.word1, self.word2, self.word3, self.word4, self.word5, self.word6, self.word7,
                        self.word8, self.word9, self.word10, self.word11, self.word12, self.word13, self.word14,
                        self.word15, self.word16, self.word17, self.word18, self.word19, self.word20, self.word21,
                        self.word22, self.word23, self.word24, self.word25, self.word26, self.word27, self.word28]

        j = 0
        for i in step1:
            for letter in i:
                if letter in "UR":
                    self.buttons[j].config(command=lambda x=j: self.select("TOP LEFT", x))

                elif letter in ("FIRST", "OKAY", "C"):
                    self.buttons[j].config(command=lambda x=j: self.select("TOP RIGHT", x))

                elif letter in ("YES", "NOTHING", "LED", "THEY ARE"):
                    self.buttons[j].config(command=lambda x=j: self.select("MIDDLE LEFT", x))

                elif letter in ("BLANK", "READ", "RED", "YOU", "YOUR", "YOU'RE", "THEIR"):
                    self.buttons[j].config(command=lambda x=j: self.select("MIDDLE RIGHT", x))

                elif letter in ("      ", "REED", "LEED", "THEY'RE"):
                    self.buttons[j].config(command=lambda x=j: self.select("BOTTOM LEFT", x))

                elif letter in ("DISPLAY", "SAYS", "NO", "LEAD", "HOLD ON", "YOU ARE", "THERE", "CEE", "SEE"):
                    self.buttons[j].config(command=lambda x=j: self.select("BOTTOM RIGHT", x))

                self.buttons[j].pack(side=LEFT, padx=10)
                j = j + 1
        self.backButton = Button(self.whoOnFirstWin, text="BACK TO\nMODULE SELECT", font=("Terminal", 20),
                                 command=lambda: self.reset(0))
        self.resetButton = Button(self.whoOnFirstWin, text="RESET", font=("Terminal", 20),
                                  command=lambda: self.reset(1))

        self.backButton.pack(side=BOTTOM)

    def select(self, display, sel):
        step1 = ["YES", "FIRST", "DISPLAY", "OKAY", "SAYS", "NOTHING", "      ",
                 'BLANK', 'NO', 'LED', 'LEAD', 'READ', 'RED', 'REED',
                 'LEED', 'HOLD ON', 'YOU', 'YOU ARE', 'YOUR', "YOU'RE", 'UR',
                 "THERE", "THEY'RE", "THEIR", "THEY ARE", "SEE", "C", "CEE"]
        self.resetButton.place(x=0, y=0)
        self.selectLabel.config(text="SELECTED '{}'\n NOW TELL THE DEFUSER TO LOOK AT THE\n"
                                     "{} BUTTON AND SELECT THE WORD OF THAT BUTTON".format(step1[sel], display))

        but_config = [("READY", lambda: self.word_list(0)),
                      ("FIRST", lambda: self.word_list(1)),
                      ("NO", lambda: self.word_list(2)),
                      ("BLANK", lambda: self.word_list(3)),
                      ("NOTHING", lambda: self.word_list(4)),
                      ("YES", lambda: self.word_list(5)),
                      ("WHAT", lambda: self.word_list(6)),
                      ("UHHH", lambda: self.word_list(7)),
                      ("LEFT", lambda: self.word_list(8)),
                      ("RIGHT", lambda: self.word_list(9)),
                      ("MIDDLE", lambda: self.word_list(10)),
                      ("OKAY", lambda: self.word_list(11)),
                      ("WAIT", lambda: self.word_list(12)),
                      ("PRESS", lambda: self.word_list(13)),
                      ("YOU", lambda: self.word_list(14)),
                      ("YOU ARE", lambda: self.word_list(15)),
                      ("YOUR", lambda: self.word_list(16)),
                      ("YOU'RE", lambda: self.word_list(17)),
                      ("UR", lambda: self.word_list(18)),
                      ("U", lambda: self.word_list(19)),
                      ("UH HUH", lambda: self.word_list(20)),
                      ("UH UH", lambda: self.word_list(21)),
                      ("WHAT?", lambda: self.word_list(22)),
                      ("DONE", lambda: self.word_list(23)),
                      ("NEXT", lambda: self.word_list(24)),
                      ("HOLD", lambda: self.word_list(25)),
                      ("SURE", lambda: self.word_list(26)),
                      ("LIKE", lambda: self.word_list(27))]

        i = 0
        for btn in but_config:
            self.buttons[i].config(text=btn[0], command=btn[1])
            self.buttons[i].pack(side=LEFT, padx=10)
            i = i + 1

    def word_list(self, list_num):
        self.selectLabel.config(text="NOW SAY ALL THESE WORDS FROM LEFT TO RIGHT\n"
                                     "AND PRESS THE FIRST ONE THAT APPEARS")
        step2 = ["READY", "FIRST", "NO", "BLANK", "NOTHING", "YES", "WHAT",
                 'UHHH', 'LEFT', 'RIGHT', 'MIDDLE', 'OKAY', 'WAIT', 'PRESS',
                 'YOU', 'YOU ARE', 'YOUR', "YOU'RE", 'UR', "U", 'UH HUH',
                 "UH UH", "WHAT?", "DONE", "NEXT", "HOLD", "SURE", "LIKE"]
        self.answerLabel.pack()
        self.topButtons.pack_forget()
        self.topButtons2.pack_forget()
        self.bottomButtons.pack_forget()
        self.bottomButtons2.pack_forget()
        images = [self.s1image, self.s2image, self.s3image, self.s4image, self.s5image, self.s6image, self.s7image,
                  self.s8image, self.s9image, self.s10image, self.s11image, self.s12image, self.s13image, self.s14image,
                  self.s15image, self.s16image, self.s17image, self.s18image, self.s19image, self.s20image,
                  self.s21image,
                  self.s22image, self.s23image, self.s24image, self.s25image, self.s26image, self.s27image,
                  self.s28image]
        for i in range(len(images)):
            if list_num == i:
                self.answerLabel.config(compound=BOTTOM, text="SELECTED '" + step2[i] + "'", image=images[i])
                break

    def img_crop(self, y):
        left = 0
        right = 674
        upper = y * 30
        lower = y * 30 + 31
        return self.img.crop([left, upper, right, lower])
