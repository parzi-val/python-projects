import time
from tkinter import *  # pylint: disable=unused-wildcard-import


def clock():
    root = Tk()
    root.title("Digital Clock")
    root.geometry("324x150")
    root.resizable(1, 1)
    label = Label(root, font=("Courier", 30, "bold"), bg="black", fg="white", bd=30)
    label.grid(row=0, column=1)

    def digitalclock():
        text_input = time.strftime("%d/%m/%Y \n%I:%M:%S %p")
        label.config(text=text_input)
        label.after(200, digitalclock)

    digitalclock()
    root.mainloop()


clock()
