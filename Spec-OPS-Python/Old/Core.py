from tkinter import *
import winreg
import os
import ctypes, sys

def change(number):
    if number == 11:
        RegPrivon["state"] = DISABLED
    if number == 12:
        RegPrivon["state"] = NORMAL
    if number == 21:
        RegPrivoff["state"] = DISABLED
    if number == 22:
        RegPrivoff["state"] = NORMAL

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


        def TurnoffPrivate():
            with winreg.ConnectRegistry(None, winreg.HKEY_CURRENT_USER) as hkey:
                with winreg.OpenKey(hkey, r"SOFTWARE\Microsoft\Windows\CurrentVersion\CapabilityAccessManager\ConsentStore\location", 0, winreg.KEY_ALL_ACCESS) as sub_key:
                  winreg.SetValueEx(sub_key, "Value",0, winreg.REG_SZ, "Allow")
                  winreg.CloseKey(sub_key)
                  print("done")

                with winreg.OpenKey(hkey, r"SOFTWARE\Microsoft\Windows\CurrentVersion\CapabilityAccessManager\ConsentStore\webcam", 0, winreg.KEY_ALL_ACCESS) as sub_key:
                  winreg.SetValueEx(sub_key, "Value",0, winreg.REG_SZ, "Allow")
                  winreg.CloseKey(sub_key)
                  print("done")

                with winreg.OpenKey(hkey, r"SOFTWARE\Microsoft\Windows\CurrentVersion\CapabilityAccessManager\ConsentStore\contacts", 0, winreg.KEY_ALL_ACCESS) as sub_key:
                  winreg.SetValueEx(sub_key, "Value",0, winreg.REG_SZ, "Allow")
                  winreg.CloseKey(sub_key)
                  print("done")

                with winreg.OpenKey(hkey, r"SOFTWARE\Microsoft\Windows\CurrentVersion\CapabilityAccessManager\ConsentStore\phoneCall", 0, winreg.KEY_ALL_ACCESS) as sub_key:
                      winreg.SetValueEx(sub_key, "Value",0, winreg.REG_SZ, "Allow")
                      winreg.CloseKey(sub_key)
                      print("done")

                with winreg.OpenKey(hkey, r"SOFTWARE\Microsoft\Windows\CurrentVersion\CapabilityAccessManager\ConsentStore\phoneCallHistory", 0, winreg.KEY_ALL_ACCESS) as sub_key:
                      winreg.SetValueEx(sub_key, "Value",0, winreg.REG_SZ, "Allow")
                      winreg.CloseKey(sub_key)
                      print("done")

                with winreg.OpenKey(hkey, r"SOFTWARE\Microsoft\Windows\CurrentVersion\CapabilityAccessManager\ConsentStore\chat", 0, winreg.KEY_ALL_ACCESS) as sub_key:
                      winreg.SetValueEx(sub_key, "Value",0, winreg.REG_SZ, "Allow")
                      winreg.CloseKey(sub_key)
                      print("done")

                with winreg.OpenKey(hkey, r"SOFTWARE\Microsoft\Windows\CurrentVersion\CapabilityAccessManager\ConsentStore\appDiagnostics", 0, winreg.KEY_ALL_ACCESS) as sub_key:
                      winreg.SetValueEx(sub_key, "Value",0, winreg.REG_SZ, "Allow")
                      winreg.CloseKey(sub_key)
                      print("done")

                with winreg.OpenKey(hkey, r"SOFTWARE\Microsoft\Windows\CurrentVersion\CapabilityAccessManager\ConsentStore\appointments", 0, winreg.KEY_ALL_ACCESS) as sub_key:
                      winreg.SetValueEx(sub_key, "Value",0, winreg.REG_SZ, "Allow")
                      winreg.CloseKey(sub_key)
                      print("done")
        #change(12)
        #change(21)



        def TurnonPrivate():
            with winreg.ConnectRegistry(None, winreg.HKEY_CURRENT_USER) as hkey:
                with winreg.OpenKey(hkey, r"SOFTWARE\Microsoft\Windows\CurrentVersion\CapabilityAccessManager\ConsentStore\location", 0, winreg.KEY_ALL_ACCESS) as sub_key:
                  winreg.SetValueEx(sub_key, "Value",0, winreg.REG_SZ, "Deny")
                  winreg.CloseKey(sub_key)
                  print("done")

                with winreg.OpenKey(hkey, r"SOFTWARE\Microsoft\Windows\CurrentVersion\CapabilityAccessManager\ConsentStore\webcam", 0, winreg.KEY_ALL_ACCESS) as sub_key:
                  winreg.SetValueEx(sub_key, "Value",0, winreg.REG_SZ, "Deny")
                  winreg.CloseKey(sub_key)
                  print("done")

                with winreg.OpenKey(hkey, r"SOFTWARE\Microsoft\Windows\CurrentVersion\CapabilityAccessManager\ConsentStore\contacts", 0, winreg.KEY_ALL_ACCESS) as sub_key:
                  winreg.SetValueEx(sub_key, "Value",0, winreg.REG_SZ, "Deny")
                  winreg.CloseKey(sub_key)
                  print("done")

                with winreg.OpenKey(hkey, r"SOFTWARE\Microsoft\Windows\CurrentVersion\CapabilityAccessManager\ConsentStore\phoneCall", 0, winreg.KEY_ALL_ACCESS) as sub_key:
                  winreg.SetValueEx(sub_key, "Value",0, winreg.REG_SZ, "Deny")
                  winreg.CloseKey(sub_key)
                  print("done")

                with winreg.OpenKey(hkey, r"SOFTWARE\Microsoft\Windows\CurrentVersion\CapabilityAccessManager\ConsentStore\phoneCallHistory", 0, winreg.KEY_ALL_ACCESS) as sub_key:
                  winreg.SetValueEx(sub_key, "Value",0, winreg.REG_SZ, "Deny")
                  winreg.CloseKey(sub_key)
                  print("done")

                with winreg.OpenKey(hkey, r"SOFTWARE\Microsoft\Windows\CurrentVersion\CapabilityAccessManager\ConsentStore\chat", 0, winreg.KEY_ALL_ACCESS) as sub_key:
                  winreg.SetValueEx(sub_key, "Value",0, winreg.REG_SZ, "Deny")
                  winreg.CloseKey(sub_key)
                  print("done")

                with winreg.OpenKey(hkey, r"SOFTWARE\Microsoft\Windows\CurrentVersion\CapabilityAccessManager\ConsentStore\appDiagnostics", 0, winreg.KEY_ALL_ACCESS) as sub_key:
                  winreg.SetValueEx(sub_key, "Value",0, winreg.REG_SZ, "Deny")
                  winreg.CloseKey(sub_key)
                  print("done")

                with winreg.OpenKey(hkey, r"SOFTWARE\Microsoft\Windows\CurrentVersion\CapabilityAccessManager\ConsentStore\appointments", 0, winreg.KEY_ALL_ACCESS) as sub_key:
                  winreg.SetValueEx(sub_key, "Value",0, winreg.REG_SZ, "Deny")
                  winreg.CloseKey(sub_key)
                  print("done")
        #change(11)
        #change(22)


        # UI Code
        root = Tk()
        root.geometry("500x500")
        root.title("Spec-OPS")
        # root.iconbitmap('./Icons/shield.ico')

        # UI Code Buttons
        PrivLabel = Label(root, text="Private Mode").grid(row=2, column=1)
        Powerplanbutton = Button(root, text="Powerplan", command=Powerplan).grid(row=1, column=2)
        RegPrivon = Button(root, text= "on", command=TurnonPrivate).grid(row=2,column=2)
        RegPrivoff = Button(root, text= "off", command=TurnoffPrivate, state= DISABLED,).grid(row=2,column=3)


        # end of code

        root.mainloop()
    else:
        ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)