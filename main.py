from tkinter import *
from pwdGenerator import *

global l1, l2, l3

root = Tk()
root.title("Generate your password!")


def l1Fun():
    le1 = number1.get("1.0", "end")
    le1 = int(le1)
    le2 = number2.get("1.0", "end")
    le2 = int(le2)
    le3 = number3.get("1.0", "end")
    le3 = int(le3)
    fileSave(generator(le1, le2, le3))


letter1 = Label(root, text="Number of letters")
letter1.grid(row=1, column=0, padx=5, pady=5)
letter2 = Label(root, text="Number of numbers")
letter2.grid(row=2, column=0, padx=5, pady=5)
letter3 = Label(root, text="Number of special characters")
letter3.grid(row=3, column=0, padx=5, pady=5)

number1 = Text(root, width=6, height=1)
number1.grid(row=1, column=1, padx=5, pady=5)
number2 = Text(root, width=6, height=1)
number2.grid(row=2, column=1, padx=5, pady=5)
number3 = Text(root, width=6, height=1)
number3.grid(row=3, column=1, padx=5, pady=5)

myButton = Button(root, text="Generate new password", command=l1Fun)
myButton.grid(row=5, columnspan=2, padx=5, pady=5)

root.mainloop()