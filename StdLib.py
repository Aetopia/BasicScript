# Nite Standard Library 

from time import sleep

Variables = {}
def Variable(Arguments):
    Name, Value = Arguments.split(' ', 1)[0].strip(), Arguments.split('=')[1].strip() 
    Variables[Name] = Value

def Echo(String): 
    try: print(f'{String}'.format(**Variables))
    except: print(String)                                  

def Pause(Time):
    try: 
        try: sleep(float(f'{Time}'.format(**Variables)))
        except: sleep(float(Time))  
    except Exception as Error: 
        print(f'[Pause] Error: {Error.__class__}')
        exit()

def If(Arguments):
    from Core import Input
    Statement, Command = Arguments.split('|')
    try:
        try: Statement = eval(f'{Statement.format(**Variables)}'.strip())
        except: Statement = eval(f'{Statement}'.strip())  
    except Exception as Error:
          print(f'[If] Error: {Error.__class__}') 
          exit()          
    if Statement: Input(Command.strip())     


