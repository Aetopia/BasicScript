# Nite
A basic barebones scripting language made using Python.

## Using Nite.
To execute a script open up the terminal and type:
```cmd
nite [Script File]
```
Script files end with `.nite`.

## How does it work?
Say, a User inputs the following script into Nite.

```
var Variable = 1
echo Variable is equal to {Variable}.
if {Variable} == 1 | echo Statement is True.
if {Variable} != 0 | echo Statement is False.
echo Pausing script.
pause 1
echo Exiting!
```
Since Nite uses ConfigParser to read values from the script it needs to convert script and structure it like an `.ini` file.  
Nite does this conversion on the fly, creating a `.cnite` file.

The converted script looks like this:
```ini
[Script]

1 = var Variable = 1
2 = echo Variable is equal to {Variable}.
3 = if {Variable} == 1 | echo Statement is True.
4 = if {Variable} != 0 | echo Statement is False.
5 = echo Pausing script.
6 = pause 1
7 = echo Exiting!

```

1. Here, Nite adds a [Script] Section into converted script.
2. Lines are interpreted as Keys with postive integers.
3. Finally, Nite sets up a simple loop in which it goes to each Key/Line and retrieves the corresponding values.
4. The values are then further parsed and executed accordingly.

And we finally get the following output:
```
Variable is equal to 1.
Statement is True.
Statement is False.
Pausing script.
Exiting!
```

## Commands

1. `var <Variable Name> = <Value>` => Creates a variable.
2. `echo <String>` => Prints the specified string into the terminal.
3. `pause <Float Value>` => Pauses a script for a specified time.
4. `if Condition | Command` => If statement.         
**Note: The If statement only uses eval() for logical operations.**

To load in variable/s values into a command, enclose them in `{}`.        
     
Example:
```
var Variable = 1
echo {Variable}
```

