import os
from random import randint
try:
    import PySimpleGUI as sg
    gui = True
    sg.theme('DefaultNoMoreNagging') 
except:
    os.system('cls')
    print("Failed to load 'PySimpleGUI', please install it for better experience (GUI)\n\ncopy and paste in 'cmd': pip install PySimpleGUI\n")
    input("> (skip) ")
    gui = False

temp = ""
long = 0
opt1 = False
opt2 = False

lettre = ["a", "z", "e", "r", "t", "y", "u", "i", "o", "p", "q", "s", "d", "f", "g", "h", "j", "k", "l", "m", "uw", "x", "c", "v", "b", "n"]
Caraspe = ["&", "#", "{", "}", "(", ")", "/", "@", "|", "[", "]", ":", ";", "?", ".", "!"]
nombre = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
password = ""


if gui == True:
    frame_layout = [
        [sg.Text('Lenght: '), sg.Input('8')],
        [sg.Text('Numbers: '), sg.Checkbox('', default=True)],
        [sg.Text('Special characters: '), sg.Checkbox('', default=True)]

        ]

    layout = [
        [sg.Frame('Password Generator', frame_layout, font='Any 12', title_color='blue')],
        [sg.Text('Password: '),sg.Input('', key='passwordf')],
        [sg.Button('Generate'), sg.Button('Quit')]
        ]


    window = sg.Window('Password Generator', layout, font=("Helvetica", 12))
    
    while True:             # Event Loop
        event, values = window.read()
        print(event, values)
        long = values[0]
        opt1 = values[2]
        opt2 = values[1]
        password = ""

        try:
            long = int(long)
            for passw in range(long):
                if opt1 == True and opt2 == False:
                    temp = randint(0,2)
                    if temp == 1:
                        password = password + Caraspe[randint(0, len(Caraspe) - 1)]
                    else:
                        password = password + lettre[randint(0, len(lettre) - 1)]
                if opt1 == True and opt2 == True:
                    temp = randint(0,3)
                    if temp == 1:
                        password = password + Caraspe[randint(0, len(Caraspe) - 1)]
                    elif temp == 2:
                        password = password + nombre[randint(0, len(nombre) - 1)]
                    else:
                        password = password + lettre[randint(0, len(lettre) - 1)]
                if opt1 == False and opt2 == True:
                    temp = randint(0,2)
                    if temp == 1:
                        password = password + nombre[randint(0, len(nombre) - 1)]
                    else:
                        password = password + lettre[randint(0, len(lettre) - 1)]
                if opt1 == False and opt2 == False:
                    password = password + lettre[randint(0, len(lettre) - 1)]
        except:
            print("error")
        
        window['passwordf'].update(password)
        if event == sg.WIN_CLOSED or event == 'Quit':
            break
    
    window.close()









else:
    os.system('cls')
    print("--------------------\n|Password Generator|\n--------------------\n")

    temp = input("Length: (default=8) ")
    try:
        int(temp)
    except:
        temp = 8

    long = int(temp)
    if long <= 3:
        long = 8
    temp = input("Special characters: (Y/N)").upper()
    if temp == "Y":
        opt1 = True
    else:
        opt1 = False
    temp = input("Numbers: (Y/N)").upper()
    if temp == "Y":
        opt2 = True
    else:
        opt2 = False



    for passw in range(long):
        if opt1 == True and opt2 == False:
            temp = randint(0,2)
            if temp == 1:
                password = password + Caraspe[randint(0, len(Caraspe) - 1)]
            else:
                password = password + lettre[randint(0, len(lettre) - 1)]
        if opt1 == True and opt2 == True:
            temp = randint(0,3)
            if temp == 1:
                password = password + Caraspe[randint(0, len(Caraspe) - 1)]
            elif temp == 2:
                password = password + nombre[randint(0, len(nombre) - 1)]
            else:
                password = password + lettre[randint(0, len(lettre) - 1)]
        if opt1 == False and opt2 == True:
            temp = randint(0,2)
            if temp == 1:
                password = password + nombre[randint(0, len(nombre) - 1)]
            else:
                password = password + lettre[randint(0, len(lettre) - 1)]
        if opt1 == False and opt2 == False:
            password = password + lettre[randint(0, len(lettre) - 1)]
        
    print("\n\nPassword:", password)
    input("\n(quit)")

