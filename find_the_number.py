import os
from time import sleep
from random import randint

#Variables
game_status = True
debug_mode = True
error_code = 0

number = randint(0,1000)
number_choice = 0
choice = ""

life = 20
status = ""
#Game
os.system('cls')
while game_status == True:
    os.system('cls')
    print("\n----------------\n|Find_The_Numer|\n----------------\n")
    print(status, "\n\n", "essais restants:",life, "\n")
    number_choice = input("Nombre > ")
    try:
        int(number_choice)
    except:
        error_code = 1
        print("erreur, code", error_code)
        sleep(1)
        break
    number_choice = int(number_choice)
    if number_choice < number:
        status = "      +"
        life = life - 1
    elif number_choice > number:
        status = "      -"
        life = life - 1
    elif number_choice == number:
        status = "      Gagné"
        sleep(1)
        print("\nGagné !")
        choice = input("\nVoulez vous recommencer ? (O/N)").lower()
        if choice == "o"  or "":
            number = randint(0,1000)
            life = 20
            status = ""
        else:
            os.system('cls')
            print("\n OK")
            sleep(1)
            break

    if life == 0:
        status = "      Perdu"
        sleep(1)
        print("\nperdu !")
        choice = input("\nVoulez vous recommencer ? (O/N)").lower()
        if choice == "o"  or "":
            number = randint(0,1000)
            life = 20
            status = ""
        else:
            os.system('cls')
            print("\n OK")
            sleep(1)
            break


input()
