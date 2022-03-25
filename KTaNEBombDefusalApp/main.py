from tkinter import *
from tkinter.font import Font

from KTaNEBombDefusalApp.Wires import wires_com


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
    wiresLabel.pack(side=LEFT)
    theButtonLabel.pack(side=LEFT)

    buttons1.pack()
    labels1.pack()





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

main()

root.mainloop()
