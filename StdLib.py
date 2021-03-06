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


