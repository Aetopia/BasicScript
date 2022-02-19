# Import Standard Library
import StdLib

def Input(Input):
    Command, Arguments = Input.split(" ", 1)
    Execute(Command.lower().strip(), Arguments.strip())

def Execute(Command, Arguments):
    match Command: 
    # Standard Library     
        case 'echo': StdLib.Echo(Arguments)
        case 'pause': StdLib.Pause(Arguments)
        case 'var': StdLib.Variable(Arguments)