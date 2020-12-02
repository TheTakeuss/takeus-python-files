import os
import time
from random import randint

#Variables
message = ""
encoded_message = ""

temp = ""
temp2 = ""
temp3 = 0

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
"0": "8"}

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
"8": "0"}

code = ["(", "[", "{", "$", "|", "-", "_", "#", "=", "&", "/", "}", "]", ")"]


#Programme
os.system('cls')
print("----------\n|Crypteur|\n----------\n")
print("1 - Encode\n2 - Decode\n3 - dico\n4 - quit\n\n")
temp = input("> ")
if temp == "1":
    os.system('cls')
    message = input("Votre message: ").lower()
    for lettre in message:
        temp = data_encoded.get(lettre)
        temp3 = randint(0,2)
        if temp3 == 1:
            encoded_message = encoded_message + code[randint(1,len(code) - 1)]
            encoded_message = encoded_message + temp
        else:
            encoded_message = encoded_message + temp
    print(encoded_message)


elif temp == "2":
    os.system('cls')
    encoded_message = input("Votre message encoded: ")
    for lettre in encoded_message:
        temp = data_decoded.get(lettre)
        if lettre not in code:
            message = message + temp
    print(message)


elif temp == "3":
    os.system('cls')
    temp = input("Lettre:")
    print(data_encoded.get(temp))
else:
    quit

