import os
import time
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


#Variables
message = ""
encoded_message = ""

temp = ""
temp2 = 0
message2 = ""



# DICTIONNAIRE
data_encoded = {
"a": "n", 
"z": "b", 
"e": "v", 
"r": "c", 
"t": "x", 
"y": "w",
"u": "m",
"i": "l",
"o": "k",
"p": "j",
"q": "h",
"s": "g",
"d": "f",
"f": "d",
"g": "s",
"h": "q",
"j": "p",
"k": "o",
"l": "i",
"m": "u",
"w": "y",
"x": "t",
"c": "r",
"v": "e",
"b": "z",
"n": "a",

"A": "N", 
"Z": "B", 
"E": "V", 
"R": "C", 
"T": "X", 
"Y": "W",
"U": "M",
"I": "L",
"O": "K",
"P": "J",
"Q": "H",
"S": "G",
"D": "F",
"F": "D",
"G": "S",
"H": "Q",
"J": "P",
"K": "O",
"L": "I",
"M": "U",
"W": "Y",
"X": "T",
"C": "R",
"V": "E",
"B": "Z",
"N": "A",

" ": ".",
"?": "*",
".": "^",
"ç": "ç",
"!": "ù",
"1": "5",
"2": "9",
"3": "4",
"4": "7",
"5": "3",
"6": "2",
"7": "1",
"8": "0",
"9": "6",
"0": "8",
"-": "'",
"(": "è",
")": "é",
":": "%",
",": "§"}
data_decoded = {
"n": "a", 
"b": "z", 
"v": "e", 
"c": "r", 
"x": "t", 
"w": "y",
"m": "u",
"l": "i",
"k": "o",
"j": "p",
"h": "q",
"g": "s",
"f": "d",
"d": "f",
"s": "g",
"q": "h",
"p": "j",
"o": "k",
"i": "l",
"u": "m",
"y": "w",
"t": "x",
"r": "c",
"e": "v",
"z": "b",
"a": "n",

"N": "A", 
"B": "Z", 
"V": "E", 
"C": "R", 
"X": "T", 
"W": "Y",
"M": "U",
"L": "I",
"K": "O",
"J": "P",
"H": "Q",
"G": "S",
"F": "D",
"D": "F",
"S": "G",
"Q": "H",
"P": "J",
"O": "K",
"I": "L",
"U": "M",
"Y": "W",
"T": "X",
"R": "C",
"E": "V",
"Z": "B",
"A": "N",

".": " ",
"*": "?",
"^": ".",
"ç": "ç",
"ù": "!",
"5": "1",
"9": "2",
"4": "3",
"7": "4",
"3": "5",
"2": "6",
"1": "7",
"0": "8",
"6": "9",
"8": "0",
"'": "-",
"é": ")",
"è": "(",
"%": ":",
"§": ","}

code = ["(", "[", "{", "$", "|", "-", "_",  "#", "=", "&", "/", "}", "]", ")"]
codel = ["A", "g", "K", "P", "d", "P", "Z",  "r", "o", "h", "s", "l", "g", "v"]


#Programme
while True:
    os.system('cls')
    print("----------\n|Encrypter|\n----------\n")
    print("1 - Encode\n2 - Decode\n3 - About\n4 - quit\n")
    temp = input("> ")


    #Encode
    if temp == "1":
        if gui == True:
            layout = [ [sg.Text('Your message: ')],[sg.Input()],[sg.OK()] ]
            window = sg.Window('Encrypter - Encode', layout)
            event, values = window.read()
            window.close()
            message = values[0]
        else:
            os.system('cls')
            print("----------\n|Encrypter|\n----------\n")
            message = input("message: ")
            os.system('cls')
            print("Encoding.")
            time.sleep(1)
            os.system('cls')
        try:
            temp = ""
            encoded_message = ""
            for lettre in message:
                temp = data_encoded.get(lettre)
                temp2 = randint(0,1)
                if temp2 == 1:
                    encoded_message = encoded_message + code[randint(1,len(code) - 1)]
                    encoded_message = encoded_message + temp
                else:
                    encoded_message = encoded_message + temp
            
            #GUI LOADING
            if gui == True:
                layout = [[sg.Text('Encoding...')],[sg.ProgressBar(200, orientation='h', size=(20, 20), key='progressbar')],[sg.Cancel()]]
                window = sg.Window('Encrypter - Encode', layout)
                progress_bar = window['progressbar']
                for i in range(200):
                    event, values = window.read(timeout=10)
                    if event == 'Cancel'  or event == sg.WIN_CLOSED:
                        break
                    progress_bar.UpdateBar(i + 1)
                window.close()
            else:
                print("Encoding..")
                time.sleep(1)
                os.system('cls')
                print("Encoding...")
                os.system('cls')
                time.sleep(1)
                os.system('cls')
            if gui == True:
                event, values = sg.Window('Encrypter - Encode', [[sg.Text("Result: ")],[sg.Input(encoded_message)],[sg.Button('Ok')]]).read(close=True)
            else:
                print("----------\n|Encrypter|\n----------\n")
                print("result:", encoded_message)
                input("\n> (quit)")
        except:
            if gui == True:
                sg.popup_error('Error, Invalid character(s) detected...')
            else:
                print("\nError, Invalid character(s) detected...")
                input("\n> (quit)")


    #Decode
    elif temp == "2":
        if gui == True:
            layout = [ [sg.Text('Encoded Message: ')],[sg.Input()],[sg.OK()] ]
            window = sg.Window('Encrypter - Decode', layout)
            event, values = window.read()
            window.close()
            encoded_message = values[0]
        else:
            os.system('cls')
            encoded_message = input("Encoded Message: ")
            os.system('cls')
            print("decoding.")
            time.sleep(1)
            os.system('cls')
        try:
            message = ""
            temp = ""
            for lettre in encoded_message:
                temp = data_decoded.get(lettre)
                if lettre not in code:
                    message = message + temp

            #GUI LOADING
            if gui == True:
                layout = [[sg.Text('Decoding...')],[sg.ProgressBar(200, orientation='h', size=(20, 20), key='progressbar')],[sg.Cancel()]]
                window = sg.Window('Encrypter - Decode', layout)
                progress_bar = window['progressbar']
                for i in range(200):
                    event, values = window.read(timeout=10)
                    if event == 'Cancel'  or event == sg.WIN_CLOSED:
                        break
                    progress_bar.UpdateBar(i + 1)
                window.close()
            else:
                print("decoding..")
                time.sleep(1)
                os.system('cls')
                print("decoding...")
                os.system('cls')
                time.sleep(1)
                os.system('cls')
            if gui == True:
                event, values = sg.Window('Encrypter - Decode', [[sg.Text("Message: ")],[sg.Input(message)],[sg.Button('Ok')]]).read(close=True)
            else:
                print("----------\n|Encrypter|\n----------\n")
                print("\nmessage:", message)
                input("\n> (quit)")          
        except:
            if gui == True:
                sg.popup_error('Error, Unable to decrypt the message...')
            else:
                print("\nError, Unable to decrypt the message...")
                input("\n> (quit)")


    elif temp == "3":
        if gui == True:
            event, values = sg.Window('Encrypter - About', [[sg.Text("Takeus in 2020")], [sg.Text("Module: OS, RANDOM, TIME, PYSIMPLEGUI")],[sg.Button('Ok')]]).read(close=True)
        else:
            os.system('cls')
            print("----------\n|Encrypter|\n----------\n")
            print("Takeus\n2020\n\nModule: OS, RANDOM, TIME, PYSIMPLEGUI\n")
            input("> (menu) ")
            

        
        
    else:
        break


