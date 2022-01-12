# WikInterpreter
A Python program with a GUI that can be used to remove the annoying square parentheses and the numbers inside of them from Wikipedia articles that contain references.

## Dependencies

PySimpleGUI:

> pip install PySimpleGUI

pyperclip:

> pip install pyperclip


## How to install from source:
> git clone https://github.com/XenoKage/WikInterpreter && cd WikInterpreter && pip install -r requirements.txt && chmod +x WikInterpreter.py

## Run the program from source:

First, open the folder containing the .py file and then:
>python WikInterpreter.py


## Create a binary from source:
### Linux
For this to work you need to have `git` installed.

First, you will need to install `pyinstaller`
> pip install pyinstaller

Then, you will need to run

> git clone https://github.com/XenoKage/WikInterpreter && cd WikInterpreter && pip install -r requirements.txt && chmod +x WikInterpreter.py

Lastly do

> pyinstaller -F --noconsole WikInterpreter.py

This will produce a working binary for your OS with all the dependencies bundled. It is found in the `dist` folder. For any questions regarding pyinstaller see [here](https://github.com/pyinstaller/pyinstaller "Pyinstaller Github").

## Download existing binary:
Go to releases page and check if there is a working binary for your OS.

