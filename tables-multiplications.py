from os import system
from time import sleep
from random import randint

#Variables
choice = ""
debug = False
affichage = 1

#def
def screen():
    system('cls')
    print("\n\n--------------------------\n|Tables de Multiplication|\n--------------------------\n")
screen()
print("-Veuillez mettre 'la fenètre en grand'\n-Très Très simple\n")
input("> (enter) ")
sleep(0.5)
while True:
    screen()
    print("1 - Révision")
    print("2 - Jeux")
    print("3 - Configuration\n")
    choice = input("> ")
    if choice == "1":
        while True:
                screen()
                choice = input("Choisissez une table (1-10/all) > ").lower()
                print("\n")
                if choice == "1":
                    print([i for i in range (0, 11) if i % 1 == 0])
                elif choice == "2":
                    print([i for i in range (1, 21) if i % 2 == 0])
                elif choice == "3":
                    print([i for i in range (2, 31) if i % 3 == 0])
                elif choice == "4":
                    print([i for i in range (3, 41) if i % 4 == 0])
                elif choice == "5":
                    print([i for i in range (4, 51) if i % 5 == 0])
                elif choice == "6":
                    print([i for i in range (5, 61) if i % 6 == 0])
                elif choice == "7":
                    print([i for i in range (6, 71) if i % 7 == 0])
                elif choice == "8":
                    print([i for i in range (7, 81) if i % 8 == 0])
                elif choice == "9":
                    print([i for i in range (8, 91) if i % 9 == 0])
                elif choice == "10":
                    print([i for i in range (9, 101) if i % 10 == 0])
                elif choice == "all":
                    print("Table de 1", [i for i in range (0, 11) if i % 1 == 0])
                    print("Table de 2", [i for i in range (1, 21) if i % 2 == 0])
                    print("Table de 3", [i for i in range (2, 31) if i % 3 == 0])
                    print("Table de 4", [i for i in range (3, 41) if i % 4 == 0])
                    print("Table de 5", [i for i in range (4, 51) if i % 5 == 0])
                    print("Table de 6", [i for i in range (5, 61) if i % 6 == 0])
                    print("Table de 7", [i for i in range (6, 71) if i % 7 == 0])
                    print("Table de 8", [i for i in range (7, 81) if i % 8 == 0])
                    print("Table de 9", [i for i in range (8, 91) if i % 9 == 0])
                    print("Table de 10", [i for i in range (9, 101) if i % 10 == 0], "\n")
                else:
                    print("Vous avez entrer une valeur invalide !")
                choice = input("> (enter)/(quit) ").lower()
                if choice == "quit":
                    break

    if choice == "":
        print("")
    if choice == "2" and debug == True:
        while True:
            print("ok")
    
    if choice == "3" and debug == True:
        while True:
            screen()
            print("C1 =", affichage, "\n(1 = [10, 20, ...] | 2 = 1X10=10,2X10=20,...)\n")
            choice = input("> (choisissez un paramètre à modifier (exemple: C1) ")
    else:
        print("Fonctionnalité en developpement/Non Trouvé")
        sleep(1.5)
                