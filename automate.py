import os,pywinauto
from pywinauto.application import Application

"""
def iecoper_import():
    app = Application(backend='uia').start('C:/PRATIC/iecoper.exe')
    dlg = app.window(title='IECOPER')

    button = dlg.child_window(title='Importar' , control_type='button')
    button.click_input()

    button1 = dlg.child_window(title='Pergunta do sistema' , control_type='button')

"""
def vsrel_test():
    app = Application(backend='uia').start('V:/Tools/VSRel3C.exe')
    dlg = app.window(title='VSRel3C')
    button = dlg.child_window(title='Sim' , control_type='button')
    button.click_input()