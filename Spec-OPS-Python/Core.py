from tkinter import *
import winreg
import os

# System Core Code
def Powerplan():
    os.system("powercfg /import 'Spec-OPS-Python\External Data\Data\Powerplan.cfg'")
    os.system("powercfg /setactive Number")

def TurnonPrivate():
    reg = reg=winreg.ConnectRegistry(None, )
    reg.ConnectRegestry


# UI Code
root = Tk()
root.title("Spec-OPS")
# root.iconbitmap('./Icons/shield.ico')

# UI Code Buttons
Powerplanbutton = Button(root, text="Powerplan", command=Powerplan).grid(row=1, column=1)
RegPriv = Button(root, text= "Private Mode", command=TurnonPrivate).grid(row=2,column=2)


# end of code

root.mainloop()
