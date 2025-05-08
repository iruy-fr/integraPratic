import os,pywinauto,subprocess
from pywinauto.application import Application
import pyautogui
from AppOpener import open

def iecoper_import():
    app = Application(backend='uia').start('C:\PRATIC\iecoper.exe')
    dlg = app.window(title='IECOPER')

    button = dlg.child_window(title='Importar' , control_type='button')
    button.click_input()

    button1 = dlg.child_window(title='Sim' , control_type='button')
    button1.click_input()

    button2 = dlg.child_window(title='Confirmar', control_type='button')
    button2.click_input()

    button3 = dlg.child_window(title='Sim', control_type='button')
    button3.click_input()