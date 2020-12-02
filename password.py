import os
import time
from random import randint

temp = ""
long = 0
opt1 = False
opt2 = False

lettre = ["a", "z", "e", "r", "t", "y", "u", "i", "o", "p", "q", "s", "d", "f", "g", "h", "j", "k", "l", "m", "uw", "x", "c", "v", "b", "n"]
Caraspe = ["&", "#", "{", "}", "(", ")", "/", "@", "|", "[", "]", ":", ";", "?", ".", "!"]
nombre = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
password = ""

temp = input("Longueur: ")
try:
    int(temp)
except:
    temp = 8

long = int(temp)
if long <= 3:
    long = 8
temp = input("Caractères Spéciaux: (Y/N)").upper()
if temp == "Y":
    opt1 = True
else:
    opt1 = False
temp = input("Nombre: (Y/N)").upper()
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
        




print("Password:", password)

