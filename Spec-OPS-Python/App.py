import sys
import platform
import os
import winreg
import ctypes
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMessageBox
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

class App(QWidget):

    def __init__(self):
        super().__init__()
        self.title = 'Spec-Ops'
        self.left = 10
        self.top = 10
        self.width = 320
        self.height = 200
        self.initUI()
    
    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        
        buttonAll = QPushButton('Boost!', self)
        buttonAll.setToolTip('Fire at Will')
        buttonAll.move(150,40)
        buttonAll.clicked.connect(self.Boost)

        buttonPower = QPushButton('Effenience', self)
        buttonPower.setToolTip('Fire at Will')
        buttonPower.move(50,40)
        buttonPower.clicked.connect(self.Powerplan)
        
        buttonPOF = QPushButton('Privacy off', self)
        buttonPOF.setToolTip('Fire at Will')
        buttonPOF.move(50,60)
        buttonPOF.clicked.connect(self.TurnoffPrivate)

        buttonPON = QPushButton('Privacy on', self)
        buttonPON.setToolTip('Fire at Will')
        buttonPON.move(150,60)
        buttonPON.clicked.connect(self.TurnonPrivate)

        buttonPON = QPushButton('System Info', self)
        buttonPON.setToolTip('Fire at Will')
        buttonPON.move(100,80)
        buttonPON.clicked.connect(self.getsysinfo)

        self.show()

    @pyqtSlot()
    def Boost(self):
            os.system('dir')
            os.system('Spec-OPS-Python\ExternalData\Batchs\deltemp.bat')

    def Powerplan(self):
            os.system("powercfg /import 'Spec-OPS-Python\ExternalData\Data\Powerplan.pow'")
            os.system("powercfg /setactive Number")

    def getsysinfo(self):
       maschine = platform.machine()
       version = platform.version()
       platformer = platform.platform()
       lucke = " "
       Systemer = platform.system()
       processor = platform.processor()
       text = maschine + lucke + version + lucke + platformer + lucke + Systemer + lucke + processor
       alert = QMessageBox()
       alert.setText(text)
       alert.exec()


    def TurnoffPrivate(self):
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

    def TurnonPrivate(self):
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

    def deltemp(self):
        os.system(open('\External Data\Batchs\deltemp.bat'))

if __name__ == '__main__':
    if is_admin():
        pass
    else:
        ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)
    
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())