from tkinter import *
from tkinter.font import Font

back = "#8f1c0a"
root = Tk()
root.title("BombDefusalApp")
root.geometry("1000x700")
root.resizable(False, False)
root.config(bg=back)

buttons1 = Frame(root, bg=back)
buttons2 = Frame(root, bg=back)
labels1 = Frame(root, bg=back)
wiresOptions = Frame(root, bg=back)


manualFont = Font(
    family="Terminal",
    size=20)

# spinbox = Spinbox(buttons1, font=manualFont, from_=0, to=9)


def main():
    backButton.pack_forget()
    nameLabel.config(text="KEEP TALKING AND NOBODY EXPLODES\n BOMB DEFUSE APP")
    selectLabel.config(text="SELECT A MODULE TO DEFUSE")

    firstButton.config(image=wires, command=lambda: wires_com(0))
    secondButton.config(image=theButton, command=lambda: the_button("", "", -1, ""))
    thirdButton.config(image=keypad, command=lambda: keypad_com())

    seventhButton.config(image=theButton, command="")
    eightButton.config(image=theButton, command="")
    nineButton.config(image=theButton, command="")

    nameLabel.pack(side=TOP, pady=30)
    selectLabel.pack(side=TOP, pady=30)

    firstButton.pack(padx=10, side=LEFT)
    secondButton.pack(padx=10, side=LEFT)
    thirdButton.pack(padx=10, side=LEFT)
    fourthButton.pack(padx=10, side=LEFT)
    fifthButton.pack(padx=10, side=LEFT)
    sixthButton.pack(padx=10, side=LEFT)


    wiresLabel.pack(side=LEFT)
    theButtonLabel.pack(side=LEFT)



    seventhButton.pack(padx=10, side=LEFT)
    eightButton.pack(padx=10, side=LEFT)
    nineButton.pack(padx=10, side=LEFT)
    tenthButton.pack(padx=10, side=LEFT)
    eleventhButton.pack(padx=10, side=LEFT)
    twelveButton.pack(padx=10, side=LEFT)

    buttons1.pack()
    labels1.pack()
    buttons2.pack(pady=10)


def yes_no_wires(answer, wires, num):
    if answer:
        # THREE WIRES
        if wires == 3:
            if num == 1:
                selectLabel.config(text="IS THE LAST WIRE WHITE?")
                firstButton.config(command=lambda: cut_wire("LAST"))
                secondButton.config(command=lambda: yes_no_wires(False, 3, 1))

            elif num == 2:
                selectLabel.config(text="IS THERE MORE THAN 1 BLUE WIRE?")
                firstButton.config(command=lambda: cut_wire("LAST BLUE"))
                secondButton.config(command=lambda: cut_wire("LAST"))

        # FOUR WIRES
        elif wires == 4:
            if num == 1:
                selectLabel.config(text="IS THERE MORE THAN 1 RED WIRE?")
                firstButton.config(command=lambda: yes_no_wires(True, 4, 2))
                secondButton.config(command=lambda: yes_no_wires(False, 4, 2))

            elif num == 2:
                selectLabel.config(text="IS THE LAST DIGIT OF THE SERIAL NUMBER ODD?")
                firstButton.config(command=lambda: cut_wire("LAST RED"))
                secondButton.config(command=lambda: yes_no_wires(False, 4, 2))

        # FIVE WIRES
        elif wires == 5:
            if num == 1:
                selectLabel.config(text="IS THE LAST DIGIT OF THE SERIAL NUMBER ODD?")
                firstButton.config(command=lambda: cut_wire("FOURTH"))
                secondButton.config(command=lambda: yes_no_wires(False, 5, 1))
            if num == 2:
                selectLabel.config(text="IS THERE MORE THAN 1 YELLOW WIRE?")
                firstButton.config(command=lambda: cut_wire("FIRST"))
                secondButton.config(command=lambda: yes_no_wires(False, 5, 2))

        # SIX WIRES
        elif wires == 6:
            if num == 1:
                selectLabel.config(text="IS THERE EXACTLY ONE YELLOW WIRE?")
                firstButton.config(command=lambda: yes_no_wires(True, 6, 3))
                secondButton.config(command=lambda: yes_no_wires(False, 6, 2))

            elif num == 2:
                selectLabel.config(text="IS THERE MORE THAN 1 WHITE WIRE?")
                firstButton.config(command=lambda: cut_wire("FOURTH"))
                secondButton.config(command=lambda: yes_no_wires(False, 6, 2))

    elif not answer:
        # THREE WIRES
        if wires == 3:
            if num == 1:
                selectLabel.config(text="ARE THERE ANY BLUE WIRES?")
                firstButton.config(command=lambda: yes_no_wires(True, 3, 2))
                secondButton.config(command=lambda: cut_wire("LAST"))

        # FOUR WIRES
        elif wires == 4:
            if num == 1:
                selectLabel.config(text="IS THE LAST WIRE YELLOW?")
                firstButton.config(command=lambda: cut_wire("FIRST"))
                secondButton.config(command=lambda: yes_no_wires(False, 4, 2))
            elif num == 2:
                selectLabel.config(text="IS THERE EXACTLY 1 BLUE WIRE?")
                firstButton.config(command=lambda: cut_wire("FIRST"))
                secondButton.config(command=lambda: yes_no_wires(False, 4, 3))
            elif num == 3:
                selectLabel.config(text="IS THERE MORE THAN 1 YELLOW WIRE?")
                firstButton.config(command=lambda: cut_wire("LAST"))
                secondButton.config(command=lambda: cut_wire("SECOND"))

        # FIVE WIRES
        elif wires == 5:
            if num == 1:
                selectLabel.config(text="IS THERE EXACTLY ONE RED WIRE?")
                firstButton.config(command=lambda: yes_no_wires(True, 5, 2))
                secondButton.config(command=lambda: yes_no_wires(False, 5, 2))
            elif num == 2:
                selectLabel.config(text="ARE THERE ANY BLACK WIRES?")
                firstButton.config(command=lambda: cut_wire("FIRST"))
                secondButton.config(command=lambda: cut_wire("SECOND"))

        # SIX WIRES
        elif wires == 6:
            if num == 1:
                selectLabel.config(text="IS THE LAST DIGIT OF THE SERIAL NUMBER ODD?")
                firstButton.config(command=lambda: cut_wire("THIRD"))
                secondButton.config(command=lambda: yes_no_wires(False, 6, 2))

            if num == 2:
                selectLabel.config(text="ARE THERE ANY RED WIRES?")
                firstButton.config(command=lambda: cut_wire("FOURTH"))
                secondButton.config(command=lambda: cut_wire("LAST"))


def wires_com(num_wires):
    if num_wires == 0:
        backButton.config(text='BACK TO\nMODULE SELECT', command=main)
        backButton.pack(side=BOTTOM)
        nameLabel.config(text="ON THE SUBJECT OF WIRES")
        forget = [wiresLabel, theButtonLabel, thirdButton, fourthButton, fifthButton, sixthButton, nineButton,
                  tenthButton,
                  eleventhButton, twelveButton]
        for i in range(len(forget)):
            forget[i].pack_forget()

        selectLabel.config(text="HOW MANY WIRES ARE THERE?")
        firstButton.config(image='', text="3 WIRES", font=manualFont, command=lambda: wires_com(3))
        secondButton.config(image='', text="4 WIRES", font=manualFont, command=lambda: wires_com(4))
        seventhButton.config(image='', text="5 WIRES", font=manualFont, command=lambda: wires_com(5))
        eightButton.config(image='', text="6 WIRES", font=manualFont, command=lambda: wires_com(6))
    else:
        seventhButton.pack_forget()
        eightButton.pack_forget()
        if num_wires == 3 or num_wires == 4:
            selectLabel.config(text="ARE THERE ANY RED WIRES?")
            firstButton.config(image='', text="YES", font=manualFont, command=lambda: yes_no_wires(True, num_wires, 1))
            if num_wires == 3:
                secondButton.config(image='', text="NO", font=manualFont, command=lambda: cut_wire("SECOND"))
            if num_wires == 4:
                secondButton.config(image='', text="NO", font=manualFont,
                                    command=lambda: yes_no_wires(False, num_wires, 1))
        elif num_wires == 5:
            selectLabel.config(text="IS THE LAST WIRE BLACK?")
            firstButton.config(image='', text="YES", font=manualFont, command=lambda: yes_no_wires(True, num_wires, 1))
            secondButton.config(image='', text="NO", font=manualFont, command=lambda: yes_no_wires(False, num_wires, 1))
        elif num_wires == 6:
            selectLabel.config(text="ARE THERE ANY YELLOW WIRES?")
            firstButton.config(image='', text="YES", font=manualFont, command=lambda: yes_no_wires(True, num_wires, 1))
            secondButton.config(image='', text="NO", font=manualFont, command=lambda: yes_no_wires(False, num_wires, 1))


def cut_wire(string):
    buttons1.pack_forget()
    labels1.pack_forget()
    buttons2.pack_forget()
    selectLabel.config(text="CUT THE " + string + " WIRE")


def ask_the_button(color, text, batteries, indicator):
    if color == "blue" and text == "abort":
        held_button("")
    elif text == "detonate" and batteries > 1:
        held_button("release")
    elif color == "white" and indicator == "car":
        held_button("")
    elif batteries > 2 and indicator == "frk":
        held_button("release")
    elif color == "yellow":
        held_button("")
    elif color == "red" and text == "hold":
        held_button("release")
    else:
        the_button(color, text, batteries, indicator)


def held_button(color):
    seventhButton.pack(padx=10, side=LEFT)
    eightButton.pack(padx=10, side=LEFT)
    nineButton.pack_forget()
    if color == "":
        selectLabel.config(text="HOLD DOWN THE BUTTON AND\nSELECT THE COLOR OF THE STRIP ON THE SIDE")
        firstButton.config(image='', text="BLUE STRIP", font=manualFont, command=lambda: held_button("blue"))
        secondButton.config(image='', text="WHITE STRIP", font=manualFont, command=lambda: held_button("white"))
        seventhButton.config(image='', text="YELLOW STRIP", font=manualFont, command=lambda: held_button("yellow"))
        eightButton.config(image='', text="OTHER", font=manualFont, command=lambda: held_button("any"))
    else:
        buttons1.pack_forget()
        labels1.pack_forget()
        buttons2.pack_forget()
        if color == "blue":
            selectLabel.config(text="RELEASE WHEN THE COUNTDOWN TIMER HAS\nA 4 IN ANY POSITION")
        elif color == "white" or color == "any":
            selectLabel.config(text="RELEASE WHEN THE COUNTDOWN TIMER HAS\nA 1 IN ANY POSITION")
        elif color == "yellow":
            selectLabel.config(text="RELEASE WHEN THE COUNTDOWN TIMER HAS\nA 5 IN ANY POSITION")
        else:
            selectLabel.config(text="PRESS AND IMMEDIATELY RELEASE THE BUTTON")


def the_button(color, text, batteries, indicator):
    backButton.config(text='BACK TO\nMODULE SELECT', command=main)
    backButton.pack(side=BOTTOM)
    nameLabel.config(text="ON THE SUBJECT OF THE BUTTON")
    forget = [wiresLabel, theButtonLabel, thirdButton, fourthButton, fifthButton,
              sixthButton, tenthButton, eleventhButton, twelveButton]
    for i in range(len(forget)):
        forget[i].pack_forget()

    if color == "":
        selectLabel.config(text="WHAT COLOR IS THE BUTTON?")
        firstButton.config(image='', text="BLUE", font=manualFont, command=lambda: ask_the_button("blue", "", -1, ""))
        secondButton.config(image='', text="WHITE", font=manualFont, command=lambda: ask_the_button("white", "", -1, ""))
        seventhButton.config(image='', text="YELLOW", font=manualFont, command=lambda: ask_the_button("yellow", "", -1, ""))
        eightButton.config(image='', text="RED", font=manualFont, command=lambda: ask_the_button("red", "", -1, ""))
        nineButton.config(image='', text="OTHER", font=manualFont, command=lambda: ask_the_button("other", "", -1, ""))

    elif text == "":
        nineButton.pack_forget()
        selectLabel.config(text="WHAT DOES THE BUTTON SAY?")
        firstButton.config(image='', text="ABORT", font=manualFont, command=lambda: ask_the_button(color, "abort", -1, ""))
        secondButton.config(image='', text="DETONATE", font=manualFont,
                            command=lambda: ask_the_button(color, "detonate", -1, ""))
        seventhButton.config(image='', text="HOLD", font=manualFont, command=lambda: ask_the_button(color, "hold", -1, ""))
        eightButton.config(image='', text="OTHER", font=manualFont, command=lambda: ask_the_button(color, "other", -1, ""))

    elif batteries == -1:
        selectLabel.config(text="HOW MANY BATTERIES ARE IN THE BOMB?")
        firstButton.config(image='', text="NONE", font=manualFont, command=lambda: ask_the_button(color, text, 0, ""))
        secondButton.config(image='', text="1 BATTERY", font=manualFont,
                            command=lambda: ask_the_button(color, text, 1, ""))
        seventhButton.config(image='', text="2 BATTERIES", font=manualFont, command=lambda: ask_the_button(color, text, 2, ""))
        eightButton.config(image='', text="3 OR MORE BATTERIES", font=manualFont,
                           command=lambda: ask_the_button(color, text, 3, ""))
    elif indicator == "":
        eightButton.pack_forget()
        selectLabel.config(text="IS THERE A LIT INDICATOR WITH ANY OF THESE LABELS?")
        firstButton.config(image='', text="CAR", font=manualFont,
                           command=lambda: ask_the_button(color, text, batteries, "car"))
        secondButton.config(image='', text="FRK", font=manualFont,
                            command=lambda: ask_the_button(color, text, batteries, "frk"))
        seventhButton.config(image='', text="OTHER/NONE", font=manualFont,
                             command=lambda: ask_the_button(color, text, batteries, "other"))
    else:
        held_button("")

def keypad_com():
    pass


wires = PhotoImage(file="Images/Wires.png")
theButton = PhotoImage(file="Images/TheButton.png")
keypad = PhotoImage(file="Images/Keypad.png")


nameLabel = Label(root, font=("Terminal", 25), fg="white", bg=back)
selectLabel = Label(root, font=manualFont, fg="white", bg=back)

backButton = Button(root, font=('Terminal', 18))


firstButton = Button(buttons1, image=wires)
secondButton = Button(buttons1, image=theButton)
thirdButton = Button(buttons1, image=keypad)
fourthButton = Button(buttons1, image=theButton)
fifthButton = Button(buttons1, image=wires)
sixthButton = Button(buttons1, image=theButton)

seventhButton = Button(buttons2)
eightButton = Button(buttons2, image=theButton)
nineButton = Button(buttons2, image=wires)
tenthButton = Button(buttons2, image=theButton)
eleventhButton = Button(buttons2, image=wires)
twelveButton = Button(buttons2, image=theButton)


wiresLabel = Label(labels1, text="WIRES", fg='white', font=manualFont, bg=back)
theButtonLabel = Label(labels1, text="THE BUTTON", fg='white', font=manualFont, bg=back)

main()

root.mainloop()
