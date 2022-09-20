from tkinter import *
import winreg
import os
import ctypes, sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout
import sys


def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

if __name__ == "__main__":
    if is_admin():
        app = QApplication([])
        window = QWidget()
        layout = QVBoxLayout()
        layout.addWidget(QPushButton('Top'))
        layout.addWidget(QPushButton('Bottom'))
        window.setLayout(layout)
        window.show()
        app.exec()

        


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


        

        # end of code

    else:
        ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)