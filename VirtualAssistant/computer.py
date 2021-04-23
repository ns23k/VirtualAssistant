'''
Most of the features in this file are only for windows
'''


import os
from .audioinout import speak
import colorama
import getpass

colorama.init(autoreset=True)
warning = colorama.Fore.RED
username = getpass.getuser()
def opencalc():
    '''
  it opens calculator
    '''
    speak('opening calculator')
    os.startfile('C:\\Windows\\system32\\calc.exe')



def openmsword():
    '''
    it opens ms word
    '''
    try:
        speak('opening MS word')
        os.startfile('C:\\programData\\Microsoft\Windows\\Start Menu\\Programs\\Microsoft Office\\Microsoft Word 2010.lnk')
    except:
        print(f'''{warning} couldn't find ms word at C:\\ProgramData\\Microsoft\Windows\\Start Menu\\Programs\\Microsoft Office\\Microsoft Word 2010.lnk''')


def openfile(path):
    '''
    it starts file of which you give path

    '''
    try:
        speak('opening file')
        os.startfile(path)
    except:
        print(f'{warning}the path specified does not exist on this computer')


def openvscode():
    '''
    opens vs code on your computer (if present)

    '''
    path = f'C:\\Users\\{username}\\appdata\\local\\programs\\Microsoft VS Code\\code.exe'
    try:
        speak('opening V S code')
        os.startfile(path)
    except:
        print(f'{warning} VS code is not present at {path}.It may not be installed on computer or it is saved on some different location')
# more features coming soon
