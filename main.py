import PySimpleGUI as sg

magic_list=["[", "]"]
nums = str([i for i in range(0,11)])

def wikipedia_inter(strr):
    index_count = 0
    toretl = []
    fnln = len(strr)
    try:
        while True:
            #print(toretl)
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

    print(theret)
    return(theret)




layout = [[sg.Text("Hello from PySimpleGUI")], [sg.Button("OK")]]

#sg.theme('DarkAmber')   # Add a touch of color
# All the stuff inside your window.
layout = [  [sg.Text('Welcome to WikInterpreter!', justification='center')],
            #[sg.Text('Enter your text:'),\
            [sg.InputText()],
            [sg.Button('Interpret!' , bind_return_key = True), sg.Button('Close')] ]


# Create the Window
window = sg.Window('WikInterpreter', layout, margins=(150,15), element_justification = 'c')
# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Close' or event == 'Interpret!': # if user closes window or clicks cancel
        break
    #print('You entered ', values[0])

window.close()

#print(values)
#print(values[0])

wikival = wikipedia_inter(values[0])
pwikival = len(wikival) + 10

if event == 'Interpret!' and values[0] != '':

    layout = [[sg.Text("Text interpreted!", justification='center')], \
              sg.InputText(wikival, use_readonly_for_disable=True, disabled=True, key='-IN-', justification='center' , \
                           size = (pwikival,15))], \
                            [sg.Button("OK" , bind_return_key = True)]

    # Create the window
    window = sg.Window("WikInterpreter", layout, margins=(150,15), element_justification='c')

    # Create an event loop
    while True:
        event, values = window.read()
        # End program if user closes window or
        # presses the OK button
        if event == "OK" or event == sg.WIN_CLOSED:
            break

    window.close()
