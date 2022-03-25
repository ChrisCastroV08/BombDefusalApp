from tkinter import *

from KTaNEBombDefusalApp.main import backButton, selectLabel, firstButton, secondButton, manualFont, nameLabel, main, \
    buttons1, labels1


def yes_no(answer, string, wires, num):
    if num == 1:
        backButton.config(text="BACK", command=lambda: yes_no(answer, string, wires, num))
    else:
        backButton.config(text="BACK", command=lambda: yes_no(answer, string, wires, num-1))
    if answer:
        # THREE WIRES
        if string == "wires" and wires == 3:
            if num == 1:
                selectLabel.config(text="IS THE LAST WIRE WHITE?")
                firstButton.config(command=lambda: cut_wire("LAST"))
                secondButton.config(command=lambda: yes_no(False, "wires", 3, 1))

            elif num == 2:
                selectLabel.config(text="IS THERE MORE THAN 1 BLUE WIRE?")
                firstButton.config(command=lambda: cut_wire("LAST BLUE"))
                secondButton.config(command=lambda: cut_wire("LAST"))

        # FOUR WIRES
        elif string == "wires" and wires == 4:
            if num == 1:
                selectLabel.config(text="IS THERE MORE THAN 1 RED WIRE?")
                firstButton.config(command=lambda: yes_no(True, "wires", 4, 2))
                secondButton.config(command=lambda: yes_no(False, "wires", 4, 2))

            elif num == 2:
                selectLabel.config(text="IS THE LAST DIGIT OF THE SERIAL NUMBER ODD?")
                firstButton.config(command=lambda: cut_wire("LAST RED"))
                secondButton.config(command=lambda: yes_no(False, "wires", 4, 2))
    elif not answer:
        # THREE WIRES
        if string == "wires" and wires == 3:
            if num == 1:
                selectLabel.config(text="ARE THERE ANY BLUE WIRES?")
                firstButton.config(command=lambda: yes_no(True, "wires", 3, 2))
                secondButton.config(command=lambda: cut_wire("LAST"))

        # FOUR WIRES
        elif string == "wires" and wires == 4:
            if num == 1:
                selectLabel.config(text="IS THE LAST WIRE YELLOW?")
                firstButton.config(command=lambda: cut_wire("FIRST"))
                secondButton.config(command=lambda: yes_no(False, "wires", 4, 2))
            elif num == 2:
                selectLabel.config(text="IS THERE EXACTLY 1 BLUE WIRE?")
                firstButton.config(command=lambda: cut_wire("FIRST"))
                secondButton.config(command=lambda: yes_no(False, "wires", 4, 3))
            elif num == 3:
                selectLabel.config(text="IS THERE MORE THAN 1 YELLOW WIRE?")
                firstButton.config(command=lambda: cut_wire("LAST"))
                secondButton.config(command=lambda: cut_wire("SECOND"))

def ask_wires(wiresnum):
    backButton.config(text="BACK", command=wires_com)
    selectLabel.config(text="ARE THERE ANY RED WIRES?")
    firstButton.config(image='', text="YES", font=manualFont, command=lambda: yes_no(True, "wires", wiresnum, 1))
    if wiresnum == 3:
        secondButton.config(image='', text="NO", font=manualFont, command=lambda: cut_wire("SECOND"))
    else:
        secondButton.config(image='', text="NO", font=manualFont, command=lambda: yes_no(False, "wires", wiresnum, 1))


def wires_com():
    backButton.config(text='BACK TO\nMODULE SELECT', command=main)
    backButton.pack(side=BOTTOM)
    nameLabel.config(text="ON THE SUBJECT OF WIRES")
    selectLabel.config(text="HOW MANY WIRES ARE THERE?")
    firstButton.config(image='', text="3 WIRES", font=manualFont, command=lambda:ask_wires(3))
    secondButton.config(image='', text="4 WIRES", font=manualFont, command=lambda:ask_wires(4))
    labels1.pack_forget()


def cut_wire(string):
    backButton.config(text='BACK TO\nMODULE SELECT', command=main)
    buttons1.pack_forget()
    selectLabel.config(text="CUT THE " + string + " WIRE")