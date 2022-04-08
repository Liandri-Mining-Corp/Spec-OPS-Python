from tkinter import *
import os

# System Core Code
def Powerplan():
    os.system("")
    pass

# UI Code
root = Tk()
root.title("Spec-OPS")
# root.iconbitmap('./Icons/shield.ico')

# UI Code Buttons
Powerplanbutton = Button(root, text="Powerplan", command=Powerplan).grid(row=1, column=1)


# end of code

root.mainloop()
