import os
from tkinter import *
from tkinter.font import Font

back = "#8f1c0a"
root = Tk()
root.geometry("1000x700")
root.resizable(False, False)
root.config(bg=back)

buttons1 = Frame(root, bg=back)
labels1 = Frame(root, bg=back)
wiresOptions = Frame(root, bg=back)

manualFont = Font(
    family="Terminal",
    size=20
)
def main():
    nameLabel.config(text="KEEP TALKING AND NOBODY EXPLODES\n BOMB DEFUSE APP")
    selectLabel.config(text="SELECT A MODULE TO DEFUSE")
    firstButton.config(image=wires, command=lambda: wires_com())
    secondButton.config(image=theButton, command=the_button)

    backButton.pack_forget()
    nameLabel.pack(side=TOP, pady=30)
    selectLabel.pack(side=TOP, pady=30)

    firstButton.pack(padx=10, side=LEFT)
    secondButton.pack(padx=10, side=LEFT)
    wiresLabel.pack(side=LEFT)
    theButtonLabel.pack(side=LEFT)

    buttons1.pack()
    labels1.pack()


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

def the_button():
    pass

wires = PhotoImage(file="Images/Wires.png")
theButton = PhotoImage(file="Images/TheButton.png")

nameLabel = Label(root, text="KEEP TALKING AND NOBODY EXPLODES\n BOMB DEFUSE APP", font=("Terminal", 25), fg="white" ,bg=back)
selectLabel = Label(root, text="SELECT A MODULE TO DEFUSE", font=manualFont, fg="white" ,bg=back)

backButton = Button(root, font=('Terminal', 18))
firstButton = Button(buttons1, image=wires, command=wires_com)
secondButton = Button(buttons1, image=theButton, command=the_button)

wiresLabel = Label(labels1, text="WIRES",fg='white', font=manualFont,bg=back)
theButtonLabel = Label(labels1, text="THE BUTTON",fg='white', font=manualFont,bg=back)









'''
def move(e):
    noButton.place(x=random.randint(0, 465),y=random.randint(0, 270))


def yes():
    label2.place(x=150, y=150)

label = Label(root, text="Te gustaría ser mi novia? c:", font=('Arvo', 12 , 'bold'))
yesButton = Button(root, text="Sí", font=('Arvo', 12 , 'bold'), command=yes)
noButton = Button(root, text="No", font=('Arvo', 12 , 'bold'))

label2 = Label(root, text="Sabía que dirías que sí! Jsjs", font=('Arvo', 10 , 'bold'), fg="red")

yesButton.place(x=100, y=200)
noButton.place(x=350, y=200)



noButton.bind("<Enter>", move)
'''



main()


root.mainloop()
