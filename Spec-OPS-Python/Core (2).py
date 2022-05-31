from tkinter import *
import winreg
import os
import ctypes, sys

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

if __name__ == "__main__":
    if is_admin():
            # System Core Code

        


        def Powerplan():
            os.system("powercfg /import 'Spec-OPS-Python\External Data\Data\Powerplan.cfg'")
            os.system("powercfg /setactive Number")

        def test():
            os.system("dir")


        def TurnonPrivate():
            os.system("Windows Privacy script.reg")

        def Turnon2():
            with winreg.ConnectRegistry(None, winreg.HKEY_LOCAL_MACHINE) as hkey:
              with winreg.OpenKey(hkey, r"SOFTWARE\Microsoft\Windows\CurrentVersion\CapabilityAccessManager\ConsentStore\webcam", 0, winreg.KEY_ALL_ACCESS) as sub_key:
                  current_path = winreg.EnumValue(sub_key,3)[1]
                  print(f"{current_path=}")


        # UI Code
        root = Tk()
        root.title("Spec-OPS")
        # root.iconbitmap('./Icons/shield.ico')

        # UI Code Buttons
        Powerplanbutton = Button(root, text="Powerplan", command=Powerplan).grid(row=1, column=1)
        RegPriv = Button(root, text= "Private Mode", command=TurnonPrivate).grid(row=2,column=2)
        Test = Button(root, text= "Test", command=Turnon2).grid(row=3,column=3)


        # end of code

        root.mainloop()
    else:
        ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)