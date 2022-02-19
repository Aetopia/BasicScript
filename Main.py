from sys import argv
from Parser import Script

if len(argv) == 1: print('| Nite Interpreter |')
else:
    try: Script(argv[1])
    except: exit()    
