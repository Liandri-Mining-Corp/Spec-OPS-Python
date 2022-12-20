# imports
import sys
import platform
import os
import winreg
import ctypes
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMessageBox
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot, qAbs

# internal check if admin for internal testing
def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

# Window class
class App(QWidget):

    # Window definitions
    def __init__(self):
        super().__init__()
        self.title = 'Spec-Ops'
        self.left = 10
        self.top = 10
        self.width = 320
        self.height = 200
        self.initUI()
    
    # Window buttons and function
    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        
        buttonAll = QPushButton('Boost!', self)
        buttonAll.setToolTip('Optimieren Sie den PC')
        buttonAll.move(150,40)
        buttonAll.clicked.connect(self.Boost)

        buttonPower = QPushButton('Effenience', self)
        buttonPower.setToolTip('Powerplan. Achtung: funktioniert möglicherweise nicht auf allen PCs')
        buttonPower.move(50,40)
        buttonPower.clicked.connect(self.Powerplan)
        
        buttonPOF = QPushButton('Privacy off', self)
        buttonPOF.setToolTip('Ermöglicht den Zugang zu Positionsdaten, etc.')
        buttonPOF.move(50,75)
        buttonPOF.clicked.connect(self.TurnoffPrivate)

        buttonPON = QPushButton('Privacy on', self)
        buttonPON.setToolTip('Verweigert den Zugriff zu Positionsdaten, etc.')
        buttonPON.move(150,75)
        buttonPON.clicked.connect(self.TurnonPrivate)

        buttonPON = QPushButton('System Info', self)
        buttonPON.setToolTip('Sehen Sie einige Informationen über Ihren PC')
        buttonPON.move(100,110)
        buttonPON.clicked.connect(self.getsysinfo)

        # Make it visible for user
        self.show()

    @pyqtSlot()
    def Powerplan(self):
           os.system("powercfg /import '\Powerscheme.pow'")
           os.system("powercfg /setactive Number")
           # we found out that some systems aren't acception external powerplans

    def Boost(self):
            os.system('boostG.bat')
            os.system('deltempG.bat')
            #Powerplan() problem with execution, may attempt later to fix

    

    def getsysinfo(self):
       maschine = platform.machine()
       version = platform.version()
       platformer = platform.platform()
       lucke = "; "
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

            with winreg.OpenKey(hkey, r"SOFTWARE\Microsoft\Windows\CurrentVersion\CapabilityAccessManager\ConsentStore\webcam", 0, winreg.KEY_ALL_ACCESS) as sub_key:
                winreg.SetValueEx(sub_key, "Value",0, winreg.REG_SZ, "Allow")
                winreg.CloseKey(sub_key)

            with winreg.OpenKey(hkey, r"SOFTWARE\Microsoft\Windows\CurrentVersion\CapabilityAccessManager\ConsentStore\contacts", 0, winreg.KEY_ALL_ACCESS) as sub_key:
                winreg.SetValueEx(sub_key, "Value",0, winreg.REG_SZ, "Allow")
                winreg.CloseKey(sub_key)

            with winreg.OpenKey(hkey, r"SOFTWARE\Microsoft\Windows\CurrentVersion\CapabilityAccessManager\ConsentStore\phoneCall", 0, winreg.KEY_ALL_ACCESS) as sub_key:
                    winreg.SetValueEx(sub_key, "Value",0, winreg.REG_SZ, "Allow")
                    winreg.CloseKey(sub_key)
                     

            with winreg.OpenKey(hkey, r"SOFTWARE\Microsoft\Windows\CurrentVersion\CapabilityAccessManager\ConsentStore\phoneCallHistory", 0, winreg.KEY_ALL_ACCESS) as sub_key:
                    winreg.SetValueEx(sub_key, "Value",0, winreg.REG_SZ, "Allow")
                    winreg.CloseKey(sub_key)
                     

            with winreg.OpenKey(hkey, r"SOFTWARE\Microsoft\Windows\CurrentVersion\CapabilityAccessManager\ConsentStore\chat", 0, winreg.KEY_ALL_ACCESS) as sub_key:
                    winreg.SetValueEx(sub_key, "Value",0, winreg.REG_SZ, "Allow")
                    winreg.CloseKey(sub_key)
                     

            with winreg.OpenKey(hkey, r"SOFTWARE\Microsoft\Windows\CurrentVersion\CapabilityAccessManager\ConsentStore\appDiagnostics", 0, winreg.KEY_ALL_ACCESS) as sub_key:
                    winreg.SetValueEx(sub_key, "Value",0, winreg.REG_SZ, "Allow")
                    winreg.CloseKey(sub_key)
                     

            with winreg.OpenKey(hkey, r"SOFTWARE\Microsoft\Windows\CurrentVersion\CapabilityAccessManager\ConsentStore\appointments", 0, winreg.KEY_ALL_ACCESS) as sub_key:
                    winreg.SetValueEx(sub_key, "Value",0, winreg.REG_SZ, "Allow")
                    winreg.CloseKey(sub_key)
                    print('Datenschutz-Modus: Aus!')

    def TurnonPrivate(self):
        with winreg.ConnectRegistry(None, winreg.HKEY_CURRENT_USER) as hkey:
            with winreg.OpenKey(hkey, r"SOFTWARE\Microsoft\Windows\CurrentVersion\CapabilityAccessManager\ConsentStore\location", 0, winreg.KEY_ALL_ACCESS) as sub_key:
                winreg.SetValueEx(sub_key, "Value",0, winreg.REG_SZ, "Deny")
                winreg.CloseKey(sub_key)
                 

            with winreg.OpenKey(hkey, r"SOFTWARE\Microsoft\Windows\CurrentVersion\CapabilityAccessManager\ConsentStore\webcam", 0, winreg.KEY_ALL_ACCESS) as sub_key:
                winreg.SetValueEx(sub_key, "Value",0, winreg.REG_SZ, "Deny")
                winreg.CloseKey(sub_key)
                 

            with winreg.OpenKey(hkey, r"SOFTWARE\Microsoft\Windows\CurrentVersion\CapabilityAccessManager\ConsentStore\contacts", 0, winreg.KEY_ALL_ACCESS) as sub_key:
                winreg.SetValueEx(sub_key, "Value",0, winreg.REG_SZ, "Deny")
                winreg.CloseKey(sub_key)
                 

            with winreg.OpenKey(hkey, r"SOFTWARE\Microsoft\Windows\CurrentVersion\CapabilityAccessManager\ConsentStore\phoneCall", 0, winreg.KEY_ALL_ACCESS) as sub_key:
                winreg.SetValueEx(sub_key, "Value",0, winreg.REG_SZ, "Deny")
                winreg.CloseKey(sub_key)
                 

            with winreg.OpenKey(hkey, r"SOFTWARE\Microsoft\Windows\CurrentVersion\CapabilityAccessManager\ConsentStore\phoneCallHistory", 0, winreg.KEY_ALL_ACCESS) as sub_key:
                winreg.SetValueEx(sub_key, "Value",0, winreg.REG_SZ, "Deny")
                winreg.CloseKey(sub_key)
                 

            with winreg.OpenKey(hkey, r"SOFTWARE\Microsoft\Windows\CurrentVersion\CapabilityAccessManager\ConsentStore\chat", 0, winreg.KEY_ALL_ACCESS) as sub_key:
                winreg.SetValueEx(sub_key, "Value",0, winreg.REG_SZ, "Deny")
                winreg.CloseKey(sub_key)
                 

            with winreg.OpenKey(hkey, r"SOFTWARE\Microsoft\Windows\CurrentVersion\CapabilityAccessManager\ConsentStore\appDiagnostics", 0, winreg.KEY_ALL_ACCESS) as sub_key:
                winreg.SetValueEx(sub_key, "Value",0, winreg.REG_SZ, "Deny")
                winreg.CloseKey(sub_key)
                 

            with winreg.OpenKey(hkey, r"SOFTWARE\Microsoft\Windows\CurrentVersion\CapabilityAccessManager\ConsentStore\appointments", 0, winreg.KEY_ALL_ACCESS) as sub_key:
                winreg.SetValueEx(sub_key, "Value",0, winreg.REG_SZ, "Deny")
                winreg.CloseKey(sub_key)
                print('Datenschutz-Modus: On!')

    #Test function
    def deltemp(self):
        os.system(open('deltemp.bat'))


if __name__ == '__main__':
    # internal check if admin for internal testing
    if is_admin():
        pass
    else:
       app = QApplication(sys.argv)
       text = 'The Programm has no admin rights and may not work correctly. Please start the Programm with admin rights.'
       alert = QMessageBox()
       alert.setText(text)
       alert.exec()
    
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())