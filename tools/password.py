import os
from random import randint
try:
    import PySimpleGUI as sg
    sg.theme('DefaultNoMoreNagging') 
except:
    os.system('cls')
    print("Failed to load 'PySimpleGUI', please install it for better experience (GUI)\n\ncopy and paste in 'cmd' or 'powershell' or 'terminal': pip install PySimpleGUI\n")
    input("> (quit) ")
    quit()

temp = ""
long = 0
opt1 = False
opt2 = False
opt3 = False
debug = False

lettre = ["a", "z", "e", "r", "t", "y", "u", "i", "o", "p", "q", "s", "d", "f", "g", "h", "j", "k", "l", "m", "w", "x", "c", "v", "b", "n"]
lettrem = ["A", "Z", "E", "R", "T", "Y", "U", "I", "O", "P", "Q", "S", "D", "F", "G", "H", "J", "K", "L", "M", "W", "X", "C", "V", "B", "N"]
Caraspe = ["&", "#", "{", "}", "(", ")", "/", "@", "|", "[", "]", ":", ";", "?", ".", "!", "%", "$", "+", "-", "_"]
nombre = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
password = ""


frame_layout = [
    [sg.Slider(range=(6,32), default_value=8, orientation='horizontal')],
    [sg.Text('Numbers: '), sg.Checkbox('', default=True)],
    [sg.Text('uppercase: '), sg.Checkbox('', default=True)],
    [sg.Text('Special characters: '), sg.Checkbox('', default=True)]

    ]
frame_layout2 = [
    [sg.Button('Generate'), sg.Button('Quit')],


    ]

layout = [
    [sg.Frame('Password Settings', frame_layout, font='Any 12', title_color='blue'), sg.Frame('Password Menu', frame_layout2, font='Any 12', title_color='blue')],
    [sg.Text('Password: '),sg.Input('', key='passwordf', size=(34,15))],
    ]

window = sg.Window('Password Generator', layout, font=("Helvetica", 12))

while True:             # Event Loop
    event, values = window.read()
    if debug == True:
        print(event, values)
    long = values[0]
    opt1 = values[3]
    opt2 = values[1]
    opt3 = values[2]
    password = ""

    try:
        long = int(long)
        for passw in range(long):

            # SPECIAL
            if opt1 == True and opt2 == False and opt3 == False:
                temp = randint(0,2)
                if temp == 1:
                    password = password + Caraspe[randint(0, len(Caraspe) - 1)]
                else:
                    password = password + lettre[randint(0, len(lettre) - 1)]
            
            # SPECIAL + MAJ
            if opt1 == True and opt2 == False and opt3 == True:
                temp = randint(0,3)
                if temp == 1:
                    password = password + Caraspe[randint(0, len(Caraspe) - 1)]
                elif temp == 2:
                    password = password + lettrem[randint(0, len(lettrem) - 1)]
                else:
                    password = password + lettre[randint(0, len(lettre) - 1)]
            
            # SPECIAL + NUMBER
            if opt1 == True and opt2 == True and opt3 == False:
                temp = randint(0,3)
                if temp == 1:
                    password = password + Caraspe[randint(0, len(Caraspe) - 1)]
                elif temp == 2:
                    password = password + nombre[randint(0, len(nombre) - 1)]
                else:
                    password = password + lettre[randint(0, len(lettre) - 1)]
            
            # SPECIAL + NUMBER + MAJ
            if opt1 == True and opt2 == True and opt3 == True:
                temp = randint(0,4)
                if temp == 1:
                    password = password + Caraspe[randint(0, len(Caraspe) - 1)]
                elif temp == 2:
                    password = password + nombre[randint(0, len(nombre) - 1)]
                elif temp == 3:
                    password = password + lettrem[randint(0, len(lettrem) - 1)]
                else:
                    password = password + lettre[randint(0, len(lettre) - 1)]

            # NUMBER
            if opt1 == False and opt2 == True and opt3 == False:
                temp = randint(0,2)
                if temp == 1:
                    password = password + nombre[randint(0, len(nombre) - 1)]
                else:
                    password = password + lettre[randint(0, len(lettre) - 1)]
            
            # NUMBER + MAJ
            if opt1 == False and opt2 == True and opt3 == True:
                temp = randint(0,3)
                if temp == 1:
                    password = password + nombre[randint(0, len(nombre) - 1)]
                elif temp == 2:
                    password = password + lettrem[randint(0, len(lettrem) - 1)]
                else:
                    password = password + lettre[randint(0, len(lettre) - 1)]
            
            # MAJ
            if opt1 == False and opt2 == False and opt3 == True:
                temp = randint(0,2)
                if temp == 1:
                    password = password + lettrem[randint(0, len(lettrem) - 1)]
                else:
                    password = password + lettre[randint(0, len(lettre) - 1)]

            # JUST LOWER LETTER
            if opt1 == False and opt2 == False and opt3 == False:
                password = password + lettre[randint(0, len(lettre) - 1)]

    except:
        print("error")
    
    window['passwordf'].update(password)
    if event == sg.WIN_CLOSED or event == 'Quit':
        break

window.close()

