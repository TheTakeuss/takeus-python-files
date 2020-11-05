from os import system
from time import sleep
from random import randint

#Variables
choice = ""
debug = False

#def
def screen():
    system('cls')
    print("\n\n--------------\n|MultiplyGame|\n--------------\n")
screen()
print("-Veuillez mettre 'la fenètre en grand'\n-Très Très simple\n-Le code n'est pas optimisé (il me semble)\n")
input("> (enter) ")
sleep(0.5)
while True:
    screen()
    print("1 - Révision")
    print("2 - Jeux")
    print("3 - Configuration")
    print("4 - Quitter\n")
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
                    print("Vous avez entré une valeur invalide !")
                choice = input("> (enter)/(quit) ").lower()
                if choice == "quit":
                    break

    if choice == "2":
        score = 0
        value1 = 0
        value2 = 0
        user_number = 0
        while True:
            screen()
            print("Votre Score:", score, "\n")
            value1 = randint(1,11)
            value2 = randint(1,11)
            print(value1, "X", value2)
            user_number = input("= ? ")
            try:
                int(user_number)
            except:
                print("Caractère invalide !")
                sleep(1)
                user_number = 1000
            user_number = int(user_number)
            if user_number == value1*value2:
                print("\nJuste ! ")
                score = score + 1
                sleep(1)
            else:
                print("Mauvaise Réponse !\n la réponse est", value1 * value2)
                sleep(1)
            if score == 10:
                print("Vous avez gagné")
                choice = input("Souhaitez-vous continuer ? (O/N)").lower()
                if choice == "n":
                    sleep(1)
                    break
                sleep(1.5)
                break
            
    
    if choice == "3" and debug == True:
        while True:
            screen()
            print("EN DEV RIEN")
            sleep(1.5)
            break
    if choice == "4":
        screen()
        print("Fermeture du programme...")
        sleep(1.5)
        break

    else:
        print("Non Trouver/Non Disponible")
        sleep(1.5)
                
