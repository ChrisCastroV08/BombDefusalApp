from tkinter import *
from tkinter.font import Font

back = "#8f1c0a"
root = Tk()
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
    thirdButton.pack(padx=10, side=LEFT)
    fourthButton.pack(padx=10, side=LEFT)
    fifthButton.pack(padx=10, side=LEFT)
    sixthButton.pack(padx=10, side=LEFT)

    seventhButton.pack(padx=10, side=LEFT)
    eightButton.pack(padx=10, side=LEFT)
    ninethButton.pack(padx=10, side=LEFT)
    tenthButton.pack(padx=10, side=LEFT)
    eleventhButton.pack(padx=10, side=LEFT)
    twelvethButton.pack(padx=10, side=LEFT)

    wiresLabel.pack(side=LEFT)
    theButtonLabel.pack(side=LEFT)


    buttons1.pack()
    labels1.pack()
    buttons2.pack(pady=10)


def yes_no(answer, string, wires, num):
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
                selectLabel.config(text="ARE THERE MORE THAN 1 RED WIRE?")
                firstButton.config(command=lambda: yes_no(True, "wires", 4, 2))
                secondButton.config(command=lambda: yes_no(False, "wires", 4, 2))

            elif num == 2:
                selectLabel.config(text="IS THE LAST DIGIT OF THE SERIAL NUMBER ODD?")
                firstButton.config(command=lambda: cut_wire("LAST RED"))
                secondButton.config(command=lambda: yes_no(False, "wires", 4, 2))

        # FIVE WIRES
        elif string == "wires" and wires == 5:
            if num == 1:
                selectLabel.config(text="IS THERE EXACTLY 1 RED WIRE?")
                firstButton.config(command=lambda: yes_no(True, "wires", 5, 2))
                secondButton.config(command=lambda: yes_no(False, "wires", 5, 1))

            elif num == 2:
                selectLabel.config(text="ARE THERE ANY YELLOW WIRES?")
                firstButton.config(command=lambda: yes_no(True, "wires", 5, 3))
                secondButton.config(command=lambda: yes_no(False, "wires", 5, 1))

            elif num == 3:
                selectLabel.config(text="ARE THERE MORE THAN ONE YELLOW WIRE?")
                firstButton.config(command=lambda: cut_wire("FIRST"))
                secondButton.config(command=lambda: yes_no(False, "wires", 5, 1))

            elif num == 4:
                selectLabel.config(text="IS THE LAST DIGIT OF THE SERIAL NUMBER ODD?")
                firstButton.config(command=lambda: cut_wire("FOURTH"))
                secondButton.config(command=lambda: yes_no(False, "wires", 5, 2))

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

        # FIVE WIRES
        elif string == "wires" and wires == 5:
            if num == 1:
                selectLabel.config(text="IS THE LAST WIRE BLACK?")
                firstButton.config(command=lambda: yes_no(True, "wires", 5, 4))
                secondButton.config(command=lambda: yes_no(False, "wires", 5, 2))
            elif num == 2:
                selectLabel.config(text="ARE THERE ANY BLACK WIRES")
                firstButton.config(command=lambda: cut_wire("FIRST"))
                secondButton.config(command=lambda: cut_wire("SECOND"))
            elif num == 3:
                selectLabel.config(text="IS THERE MORE THAN 1 YELLOW WIRE?")
                firstButton.config(command=lambda: cut_wire("LAST"))
                secondButton.config(command=lambda: cut_wire("SECOND"))


def ask_wires(wiresnum):
    selectLabel.config(text="ARE THERE ANY RED WIRES?")
    firstButton.config(image='', text="YES", font=manualFont, command=lambda: yes_no(True, "wires", wiresnum, 1))
    seventhButton.pack_forget()
    eightButton.pack_forget()
    if wiresnum == 3:
        secondButton.config(image='', text="NO", font=manualFont, command=lambda: cut_wire("SECOND"))
    elif wiresnum == 6:
        secondButton.config(image='', text="NO", font=manualFont, command=lambda: cut_wire("LAST"))
    else:
        secondButton.config(image='', text="NO", font=manualFont, command=lambda: yes_no(False, "wires", wiresnum, 1))


def wires_com():
    backButton.config(text='BACK TO\nMODULE SELECT', command=main)
    backButton.pack(side=BOTTOM)
    nameLabel.config(text="ON THE SUBJECT OF WIRES")
    selectLabel.config(text="HOW MANY WIRES ARE THERE?")
    firstButton.config(image='', text="3 WIRES", font=manualFont, command=lambda: ask_wires(3))
    secondButton.config(image='', text="4 WIRES", font=manualFont, command=lambda: ask_wires(4))
    seventhButton.config(image='', text="5 WIRES", font=manualFont, command=lambda: ask_wires(5))
    eightButton.config(image='', text="6 WIRES", font=manualFont, command=lambda: ask_wires(6))
    forget = [labels1, thirdButton, fourthButton, fifthButton, sixthButton, ninethButton, tenthButton, eleventhButton,
              twelvethButton]
    for i in range(len(forget)):
        forget[i].pack_forget()


def cut_wire(string):
    buttons1.pack_forget()
    selectLabel.config(text="CUT THE " + string + " WIRE")


def the_button():
    pass

wires = PhotoImage(file="Images/Wires.png")
theButton = PhotoImage(file="Images/TheButton.png")

nameLabel = Label(root, text="KEEP TALKING AND NOBODY EXPLODES\n BOMB DEFUSE APP", font=("Terminal", 25), fg="white" ,bg=back)
selectLabel = Label(root, text="SELECT A MODULE TO DEFUSE", font=manualFont, fg="white" ,bg=back)

backButton = Button(root, font=('Terminal', 18))




firstButton = Button(buttons1, image=wires)
secondButton = Button(buttons1, image=theButton)
thirdButton = Button(buttons1, image=wires)
fourthButton = Button(buttons1, image=theButton)
fifthButton = Button(buttons1, image=wires)
sixthButton = Button(buttons1, image=theButton)

seventhButton = Button(buttons2, image=wires)
eightButton = Button(buttons2, image=theButton)
ninethButton = Button(buttons2, image=wires)
tenthButton = Button(buttons2, image=theButton)
eleventhButton = Button(buttons2, image=wires)
twelvethButton = Button(buttons2, image=theButton)


wiresLabel = Label(labels1, text="WIRES",fg='white', font=manualFont,bg=back)
theButtonLabel = Label(labels1, text="THE BUTTON",fg='white', font=manualFont,bg=back)

main()

root.mainloop()
