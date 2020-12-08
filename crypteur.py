import os
import time
from random import randint
try:
    import PySimpleGUI as sg
    gui = True
except:
    os.system('cls')
    print("Failed to load 'PySimpleGUI', please install it for better exeperience\n\ncopy and paste in 'cmd': pip install PySimpleGUI\n")
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
    print("1 - Encode\n2 - Decode\n3 - MoreSecureMode\n4 - quit\n\n")
    temp = input("> ")
    if temp == "1":
        os.system('cls')
        print("----------\n|Encrypter|\n----------\n")
        message = input("message: ")
        if len(message) >= 10:
            temp2 = 1
        elif len(message) >= 6:
            temp2 = 0.5
        else:
            temp2 = 0.25
        os.system('cls')
        print("generating.")
        time.sleep(temp2)
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
            print("generating..")
            time.sleep(temp2)
            os.system('cls')
            print("generating...")
            os.system('cls')
            time.sleep(temp2)
            os.system('cls')
            if gui == True:
                event, values = sg.Window('Encrypter - Encode', [[sg.Text("Result: ")],[sg.Input(encoded_message)],[sg.Button('Ok')]]).read(close=True)
            else:
                print("----------\n|Encrypter|\n----------\n")
                print("result:", encoded_message)
                input("\n> (quit)")
        except:
            print("\nError, Invalid character(s) detected...")
            input("\n> (quit)")

    elif temp == "2":
        os.system('cls')
        encoded_message = input("Encoded Message: ")
        if len(encoded_message) >= 15:
            temp2 = 1
        elif len(encoded_message) >= 10:
            temp2 = 0.5
        else:
            temp2 = 0.25
        os.system('cls')
        print("decoding.")
        time.sleep(temp2)
        os.system('cls')
        try:
            message = ""
            temp = ""
            for lettre in encoded_message:
                temp = data_decoded.get(lettre)
                if lettre not in code:
                    message = message + temp
            print("decoding..")
            time.sleep(temp2)
            os.system('cls')
            print("decoding...")
            os.system('cls')
            time.sleep(temp2)
            os.system('cls')
            if gui == True:
                event, values = sg.Window('Encrypter - Decode', [[sg.Text("Message: ")],[sg.Input(message)],[sg.Button('Ok')]]).read(close=True)
            else:
                print("----------\n|Encrypter|\n----------\n")
                print("\nmessage:", message)
                input("\n> (quit)")          
        except:
            print("\nError, Unable to decrypt the message...")
            input("\n> (quit)")



    #More secure Mode
    elif temp == "3":
        os.system('cls')
        print("----------\n|Encrypter|\n----------\nMoreSecureMode\n\n1 - Encode\n2 - Decode\n3 - Quit")
        temp = input("> ")

        #Encode
        if temp == "1":
            os.system('cls')
            print("----------\n|Encrypter|\n----------\n")
            print("More Secure Mode\nthe message may not contain any special characters or number.\ntype twice the last letter of your message\n")
            message = input("message: ")
            if len(message) >= 10:
                temp2 = 1
            elif len(message) >= 6:
                temp2 = 0.5
            else:
                temp2 = 0.25
            os.system('cls')
            print("generating.")
            time.sleep(temp2)
            os.system('cls')
            try:
                message2 = ""
                for element in message:
                    if element in code or element == " ":
                        print(""+1)
                message = ' '.join(format(ord(x), 'b') for x in message)
                for lettre in message:
                    temp = data_encoded.get(lettre)
                    temp2 = randint(0,1)
                    if temp2 == 1:
                        encoded_message = encoded_message + codel[randint(1,len(codel) - 1)]
                        encoded_message = encoded_message + temp
                    else:
                        encoded_message = encoded_message + code[randint(1,len(code) - 1)]
                        encoded_message = encoded_message + temp
                print("generating..")
                time.sleep(temp2)
                os.system('cls')
                print("generating...")
                os.system('cls')
                time.sleep(temp2)
                os.system('cls')
                if gui == True:
                    event, values = sg.Window('Encrypter - Encode (More Secure Mode)', [[sg.Text("result: ")],[sg.Input(encoded_message)],[sg.Button('Ok')]]).read(close=True)
                else:
                    print("----------\n|Encrypter|\n----------\n")
                    print("result:", encoded_message)
                    input("\n> (quit)")
            except:
                print("\nError, Invalid character(s) detected...")
                input("\n> (quit)")


        #Decode
        elif temp == "2":
            os.system('cls')
            print("----------\n|Encrypter|\n----------\n")
            print("More Secure Mode\n")
            encoded_message = input("Encoded Message: ")
            if len(encoded_message) >= 15:
                temp2 = 1
            elif len(encoded_message) >= 10:
                temp2 = 0.5
            else:
                temp2 = 0.25
            os.system('cls')
            print("decoding.")
            time.sleep(temp2)
            os.system('cls')
            try:
                message = ""
                message2 = ""
                for lettre in encoded_message:
                    temp = data_decoded.get(lettre)
                    if lettre not in code:
                        if lettre not in codel:
                            message = message + temp
                message2 = ''.join(chr(int(message[i*8:i*8+8],2)) for i in range(len(message)//8))
                print("decoding..")
                time.sleep(temp2)
                os.system('cls')
                print("decoding...")
                os.system('cls')
                time.sleep(temp2)
                os.system('cls')
                if gui == True:
                    event, values = sg.Window('Encrypter - Decode (More Secure Mode)', [[sg.Text("Message: ")],[sg.Input(message2)],[sg.Button('Ok')]]).read(close=True)
                else:
                    print("----------\n|Encrypter|\n----------\n")
                    print("\nmessage:", message2)
                    input("\n> (quit)")          
            except:
                print("\nError, Unable to decrypt the message...")
                input("\n> (quit)")

    
        else:
            quit
        
    else:
        break


