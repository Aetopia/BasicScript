from configparser import ConfigParser
from os import path, remove
from Core import Input
from platform import system
from subprocess import run
    
def Parse(Script, Clear = False):
    # Parses Raw .ini Files.

    Line = 1
    Parse = ConfigParser()
    Parse.read(path.abspath(Script))
    while True:
        try:
            Command = str(Parse['Script'][str(Line)]).strip()
            Line += 1
            if Command == 'None': break
            elif Command != '':
                Input(Command)
        except: 
            break 
    if Clear: remove(Script)    

def Script(File):
    # Opens and parses a IniScript File.
    File = path.abspath(File)
    if path.exists(File) is False:
        print("Error: File doesn't exist.")
        exit()
    if path.splitext(File)[1].lower() not in ['.nite','.cnite','.ini']:
        print('Error: Invalid IniScript File.')
        exit()
    Script = ConfigParser()
    try: 
        Script.read(File)  
        Parse(File)
    except: 
        Line = 1
        Raw = open(File,'r+').readlines()
        Raw = ['[Script]\n\n']  + Raw
        while True:
            try:
                Raw[Line] = f'{Line} = {Raw[Line]}'
                Line += 1
            except: break  
        CompliedScript = f'{path.splitext(File)[0]}.cnite'  
        with open(CompliedScript, 'w+') as Script:
            Script.write(''.join(Raw))
        if system() == 'Windows':
            run(f'attrib.exe +H {path.abspath(CompliedScript)}', shell=True)    
        Parse(CompliedScript, Clear=True)           