import os
import time
from random import randint

#Variables
message = ""
encoded_message = ""

temp = ""
temp2 = ""
temp3 = 0
v2 = ""

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
os.system('cls')
print("----------\n|Encrypter|\n----------\n")
print("1 - Encode\n2 - Decode\n3 - Lists\n4 - MoreSecureMode (IN DEV)\n5 - quit\n\n")
temp = input("> ")
if temp == "1":
    os.system('cls')
    print("----------\n|Encrypter|\n----------\n")
    message = input("message: ")
    if len(message) >= 10:
        temp3 = 1
    elif len(message) >= 6:
        temp3 = 0.5
    else:
        temp3 = 0.25
    os.system('cls')
    print("generating.")
    time.sleep(temp3)
    os.system('cls')
    try: 
        for lettre in message:
            temp = data_encoded.get(lettre)
            temp3 = randint(0,1)
            if temp3 == 1:
                encoded_message = encoded_message + code[randint(1,len(code) - 1)]
                encoded_message = encoded_message + temp
            else:
                encoded_message = encoded_message + temp
        print("generating..")
        time.sleep(temp3)
        os.system('cls')
        print("generating...")
        os.system('cls')
        time.sleep(temp3)
        os.system('cls')
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
        temp3 = 1
    elif len(encoded_message) >= 10:
        temp3 = 0.5
    else:
        temp3 = 0.25
    os.system('cls')
    print("decoding.")
    time.sleep(temp3)
    os.system('cls')
    try:
        for lettre in encoded_message:
            temp = data_decoded.get(lettre)
            if lettre not in code:
                message = message + temp
        print("decoding..")
        time.sleep(temp3)
        os.system('cls')
        print("decoding...")
        os.system('cls')
        time.sleep(temp3)
        os.system('cls')
        print("----------\n|Encrypter|\n----------\n")
        print("\nmessage:", message)
        input("\n> (quit)")          
    except:
        print("\nError, Unable to decrypt the message...")
        input("\n> (quit)")



elif temp == "3":
    while True:
        os.system('cls')
        temp = input("Letter:")
        print(data_encoded.get(temp))
        temp = input("\n> Continue? (Y/N) ").lower()
        if temp != "y":
            break

elif temp == "4":
    print("----------\n|Encrypter|\n----------\n1 - Encode\n2 - Decode\n3 - Quit")
    temp = input("> ")
    if temp == "1":
        os.system('cls')
        print("----------\n|Encrypter|\n----------\n")
        print("More Secure Mode\nthe message may not contain any special characters.\n")
        message = input("message: ")
        if len(message) >= 10:
            temp3 = 1
        elif len(message) >= 6:
            temp3 = 0.5
        else:
            temp3 = 0.25
        os.system('cls')
        print("generating.")
        time.sleep(temp3)
        os.system('cls')
        try: 
            message = ' '.join(format(ord(x), 'b') for x in message)
            for lettre in message:
                temp = data_encoded.get(lettre)
                temp3 = randint(0,1)
                if temp3 == 1:
                    encoded_message = encoded_message + codel[randint(1,len(codel) - 1)]
                    encoded_message = encoded_message + temp
                else:
                    encoded_message = encoded_message + code[randint(1,len(code) - 1)]
                    encoded_message = encoded_message + temp
            print("generating..")
            time.sleep(temp3)
            os.system('cls')
            print("generating...")
            os.system('cls')
            time.sleep(temp3)
            os.system('cls')
            print("----------\n|Encrypter|\n----------\n")
            print("result:", encoded_message)
            input("\n> (quit)")
        except:
            print("\nError, Invalid character(s) detected...")
            input("\n> (quit)")



    elif temp == "2":
        os.system('cls')
        print("----------\n|Encrypter|\n----------\n")
        print("More Secure Mode\n")
        encoded_message = input("Encoded Message: ")
        if len(encoded_message) >= 15:
            temp3 = 1
        elif len(encoded_message) >= 10:
            temp3 = 0.5
        else:
            temp3 = 0.25
        os.system('cls')
        print("decoding.")
        time.sleep(temp3)
        os.system('cls')
        try:
            for lettre in encoded_message:
                temp = data_decoded.get(lettre)
                if lettre not in code or lettre not in codel:
                    message = message + temp
            v2 = ''.join(chr(int(message[i*8:i*8+8],2)) for i in range(len(message)//8))
            print("decoding..")
            time.sleep(temp3)
            os.system('cls')
            print("decoding...")
            os.system('cls')
            time.sleep(temp3)
            os.system('cls')
            print("----------\n|Encrypter|\n----------\n")
            print("\nmessage:", message)
            input("\n> (quit)")          
        except:
            print("\nError, Unable to decrypt the message...")
            input("\n> (quit)")






        
    else:
        quit
    
else:
    quit


