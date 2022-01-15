import PySimpleGUI as sg
import pyperclip

magic_list = ["[", "]"]
nums = str([i for i in range(0, 11)])



def wikipedia_inter(strr):
    index_count = 0
    toretl = []
    fnln = len(strr)
    try:
        while True:
            if index_count >= fnln:
                break
            elif strr[index_count] == "[":
                if strr[index_count + 3] in nums:
                    index_count += 3
                    pass
                elif strr[index_count + 4] in nums:
                    index_count += 4
                    pass
                elif strr[index_count + 2] in nums:
                    index_count += 2
                    pass
                elif strr[index_count + 1] in nums:
                    index_count += 1
                    pass
                else:
                    index_count += 1
            elif strr[index_count] == "]":
                index_count += 1
            elif strr[index_count] not in magic_list:
                toretl.append(strr[index_count])
                index_count += 1

    except:
        pass

    theret = "".join(toretl)

    #print(theret)
    return (theret)


# All the stuff inside your window.
layout = [[sg.Text('Welcome to WikInterpreter!', justification='center')],
          [sg.InputText(key= 'ttinput' ,right_click_menu=['&Edit', ['Copy', 'Paste', 'Select All']])],
          [sg.Button('Interpret!', bind_return_key=True), sg.Button('Close')]]

# Create the Window
window = sg.Window('WikInterpreter', layout, margins=(150, 15), element_justification='c', return_keyboard_events=True)
# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()
    #print(event)
    window['ttinput'].bind('<Control-v>', 'pest')
    window['ttinput'].bind('<Control-a>', 'sel')
    if event == sg.WIN_CLOSED or event == 'Close' or event == 'Interpret!':  # if user closes window or clicks cancel
        values[0] = window['ttinput']
        break
    elif event == 'Copy':
        pyperclip.copy(window['ttinput'].Widget.selection_get())
    elif event == 'Paste' or event == 'ttinputpest':
        try:
            selection = (window['ttinput'].Widget.index("sel.first"), window['ttinput'].Widget.index("sel.last"))
            if type(selection) != None:
                window['ttinput'].Widget.delete(selection[0],selection[1])
                #print(selection)
        except:
            pass
        window['ttinput'].Widget.insert("insert",pyperclip.paste())
    elif event == 'Select All' or event == 'ttinputsel':
        window['ttinput'].Widget.select_range(0, 'end')

window.close()




wikival = wikipedia_inter(values['ttinput'])
pwikival = len(wikival) + 10




if event == 'Interpret!' and values['ttinput'] != '':

    layout = [[sg.Text("Text interpreted!", justification='center')], \
              sg.InputText(wikival, use_readonly_for_disable=True, disabled=True, key='-IN-', justification='center', \
                           size=(pwikival, 15), right_click_menu=['&Edit', ['Copy', 'Select All']])], \
             [sg.Button("OK", bind_return_key=True)]

    # Create the window
    window = sg.Window("WikInterpreter", layout, margins=(150, 15), return_keyboard_events=True, \
                       element_justification='c')

    # Create an event loop
    while True:
        event, values = window.read()
        window['-IN-'].bind('<Control-a>', 'sel')
        # End program if user closes window or
        # presses the OK button
        if event == "OK" or event == sg.WIN_CLOSED:
            break
        elif event == 'Copy':
            pyperclip.copy(window['-IN-'].Widget.selection_get())
        elif event == 'Select All' or event == '-IN-sel':
            window['-IN-'].Widget.select_range(0, 'end')

window.close()
