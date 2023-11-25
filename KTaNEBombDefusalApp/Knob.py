from tkinter import *


class Knob:

    def reset(self, num):
        if num == 0:
            self.knobWin.destroy()
        elif num == 1:
            self.knobWin.destroy()
            self.__init__(self.root, self.back, self.manual_font, self.knobImage)

    def __init__(self, root, back, manual_font, knob_image):
        self.root = root
        self.back = back
        self.manual_font = manual_font
        self.knobImage = knob_image
        self.knobWin = Toplevel(self.root)
        self.knobWin.title("The Button")
        self.knobWin.resizable(False, False)
        self.knobWin.config(bg=back)
        self.lftPos = (self.knobWin.winfo_screenwidth() - 1000) / 2
        self.topPos = (self.knobWin.winfo_screenheight() - 700) / 2
        self.knobWin.geometry("%dx%d+%d+%d" % (1000, 700, self.lftPos, self.topPos))

        self.nameLabel = Label(self.knobWin, font=("Terminal", 25), fg="white", bg=back,
                               text="ON THE SUBJECT OF KNOBS")
        self.selectLabel = Label(self.knobWin, font=("Terminal", 20), fg="white", bg=back,
                                 text="TELL THE DEFUSER TO LOOK AT THE SIX LEDs ON THE LEFT\n"
                                      "AND ASK HOW MANY LEDs ARE ON")

        self.width = self.knobImage.width()
        self.height = self.knobImage.height()

        self.topButtons = Frame(self.knobWin, bg=back)
        self.bottomButtons = Frame(self.knobWin, bg=back)
        self.nameLabel.pack(side=TOP, pady=30)
        self.selectLabel.pack(side=TOP, pady=30)
        self.canvas = Canvas(self.knobWin, bg=back, highlightthickness=0, height=self.height + 1,
                             width=self.width + 1)
        self.canvas.create_image(self.width / 2, self.height / 2, image=self.knobImage)
        self.canvas.create_oval(10, 55, 45, 90, outline="red", width=2, tag="first")

        self.topButtons.pack()
        self.bottomButtons.pack(pady=10)
        self.canvas.pack()

        self.firstButton = Button(self.topButtons, font=self.manual_font, text="0 LEDs",
                                  command=lambda: self.check_led("LEFT"))
        self.secondButton = Button(self.topButtons, font=self.manual_font, text="1 LED",
                                   command=lambda: self.check_led("LEFT"))
        self.thirdButton = Button(self.topButtons, font=self.manual_font, text="2 LEDs",
                                  command=lambda: self.check_led("LEFT"))
        self.fourthButton = Button(self.bottomButtons, font=self.manual_font, text="3 LEDs",
                                   command=lambda: self.check_led("DOWN"))
        self.fifthButton = Button(self.bottomButtons, font=self.manual_font, text="4 LEDs",
                                  command=lambda: self.check_led("UP"))
        self.sixthButton = Button(self.bottomButtons, font=self.manual_font, text="5 LEDs",
                                  command=lambda: self.check_led("FIVE"))

        self.firstButton.pack(side=LEFT, padx=10)
        self.secondButton.pack(side=LEFT, padx=10)
        self.thirdButton.pack(side=LEFT, padx=10)
        self.fourthButton.pack(side=LEFT, padx=10)
        self.fifthButton.pack(side=LEFT, padx=10)
        self.sixthButton.pack(side=LEFT, padx=10)

        self.backButton = Button(self.knobWin, text="BACK TO\nMODULE SELECT", font=("Terminal", 20),
                                 command=lambda: self.reset(0))
        self.resetButton = Button(self.knobWin, text="RESET", font=("Terminal", 20),
                                  command=lambda: self.reset(1))

        self.backButton.pack(side=BOTTOM)

    def check_led(self, led_s):
        self.resetButton.place(x=0, y=0)
        self.topButtons.pack_forget()
        self.bottomButtons.pack_forget()
        self.thirdButton.pack_forget()

        if led_s != "FIVE":
            self.canvas.pack_forget()
            self.selectLabel.config(text="PLACE THE KNOB IN THE {} POSITION,\n"
                                         "RELATIVE TO THE 'UP' LABEL IN THE KNOB".format(led_s))
        else:
            self.selectLabel.config(text="IS THE TOP LEFT LED ON?")
            self.topButtons.pack()
            self.canvas.delete("first")
            self.canvas.create_oval(20, 55, 30, 65, outline="red", width=2)
            self.firstButton.config(text="YES", command=lambda: self.check_led("RIGHT"))
            self.secondButton.config(text="NO", command=lambda: self.check_led("DOWN"))
