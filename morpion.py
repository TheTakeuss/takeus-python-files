import os
import time
from random import randint

# Variables
comput_status = False
win = False

temp = 0

player_choice = 0
comput_choice = 0

player_score =  0
comput_score = 0

player_token = ""
comput_token = ""
terrain = []

A1 = " "
A2 = " "
A3 = " "

B1 = " "
B2 = " "
B3 = " "

C1 = " "
C2 = " "
C3 = " "

answer = ""
# Configuration
game_start = True
game_lenght = 5
debug_mode = False
error_type = 0


#Game
os.system('cls')
print("\n------------\nMorpion Game\n------------\n")
print("- Il est préférable de jouer avec le terminal de votre IDE 'en grand'")
print("- Vous devrez chosiri votre 'case' par le biais de numéro de 1 à 9...")
print("- Jeu du morpion, un grand classique des jeux en permanence au collège\n")
player_token = str(input("Votre Signe: (X/O) ").upper())
if player_token == "X" or player_token == "O":
    if player_token == "X":
        comput_token = "O"
    else:
        comput_token = "X"
elif player_token == "":
    player_token = "X"
    comput_token = "O"
else:
    error_type = 1
    game_start = False
    print("Erreur, code", error_type)
if debug_mode == True:
    print("\n\nDebug\n--\nplayer_token=", player_token, "\ncomput_token=", comput_token)
time.sleep(0.5)
terrain.clear()
terrain.append(A1)
terrain.append(A2)
terrain.append(A3)
terrain.append(B1)
terrain.append(B2)
terrain.append(B3)
terrain.append(C1)
terrain.append(C2)
terrain.append(C3)
print(terrain)
while game_start == True:
    #Screen
    os.system('cls')
    print("------------\nMorpion Game\n------------")
    print("\n−−−−−−−−−−−−−")
    print("|", A1, "|", A2, "|", A3, "|")
    print("−−−−−−−−−−−−−")
    print("|", B1, "|", B2, "|", B3, "|")
    print("−−−−−−−−−−−−−")
    print("|", C1, "|", C2, "|", C3, "|")
    print("−−−−−−−−−−−−−\n")
    if debug_mode == True:
        print(terrain)
    #Player
    while True:
        player_choice = input("Case: (1-9) ")
        try:
            int(player_choice)
        except:
            error_type = 2
            print("Erreur, code", error_type)
            time.sleep(0.5)
            break
        player_choice = int(player_choice)

        if terrain[player_choice-1] == comput_token:
            print("\nLa case est déjà rempli, veuillez refaire...\n\n")
        else:
            break
    if player_choice == 1:
        A1 = player_token
        terrain[0] = A1
    elif player_choice == 2:
        A2 = player_token
        terrain[1] = A2
    elif player_choice == 3:
        A3 = player_token
        terrain[2] = A3
    elif player_choice == 4:
        B1 = player_token
        terrain[3] = B1
    elif player_choice == 5:
        B2 = player_token
        terrain[4] = B2
    elif player_choice == 6:
        B3 = player_token
        terrain[5] = B3
    elif player_choice == 7:
        C1 = player_token
        terrain[6] = C1
    elif player_choice == 8:
        C2 = player_token
        terrain[7] = C2
    elif player_choice == 9:
        C3 = player_token
        terrain[8] = C3
    #Comput
    for positions in terrain:
        temp = randint(1,9)
        if terrain[temp-1] == " ":
            comput_choice = temp

            if comput_choice == 1:
                A1 = comput_token
                terrain[0] = A1
            elif comput_choice == 2:
                A2 = comput_token
                terrain[1] = A2
            elif comput_choice == 3:
                A3 = comput_token
                terrain[2] = A3
            elif comput_choice == 4:
                B1 = comput_token
                terrain[3] = B1
            elif comput_choice == 5:
                B2 = comput_token
                terrain[4] = B2
            elif comput_choice == 6:
                B3 = comput_token
                terrain[5] = B3
            elif comput_choice == 7:
                C1 = comput_token
                terrain[6] = C1
            elif comput_choice == 8:
                C2 = comput_token
                terrain[7] = C2
            elif comput_choice == 9:
                C3 = comput_token
                terrain[8] = C3
            break
        
    #Score
    win = False
    #Lignes
    if A1 == A2 == A3 and A1 !=' ':
        win=True
        if A1==player_token:
            player_score+=1
        else:
            comput_score+=1
    elif B1 == B2 == B3 and B1 != ' ':
        win=True
        if B1==player_token:
            player_score+=1
        else:
            comput_score+=1
    elif C1 == C2 == C3 and C1 != ' ':
        win=True
        if C1==player_token:
            player_score+=1
        else:
            comput_score+=1
    #Colonne
    if A1 == B1 == C1 and A1 != ' ':
        win=True
        if A1==player_token:
            player_score+=1
        else:
            comput_score+=1
    if A2 == B2 == C2 and A2 != ' ':
        win=True
        if A2==player_token:
            player_score+=1
        else:
            comput_score+=1
    if A3 == B3 == C3 and A3 != ' ':
        win=True
        if A3==player_token:
            player_score+=1
        else:
            comput_score+=1
    #Diagonal
    if A1 == B2 == C3 and A1 != ' ':
        win=True
        if A1==player_token:
            player_score+=1
        else:
            comput_score+=1
    if A3 == B2 == C1 and A3 != ' ':
        win=True
        if A3==player_token:
            player_score+=1
        else:
            comput_score+=1
    #Egalité
        #Pas fini
    
    #CheckPoint
    if win:
        os.system('cls')
        print("------------\nMorpion Game\n------------")
        print("\n−−−−−−−−−−−−−")
        print("|", A1, "|", A2, "|", A3, "|")
        print("−−−−−−−−−−−−−")
        print("|", B1, "|", B2, "|", B3, "|")
        print("−−−−−−−−−−−−−")
        print("|", C1, "|", C2, "|", C3, "|")
        print("−−−−−−−−−−−−−\n")
        if debug_mode == True:
            print(terrain)
        if player_score > comput_score:
            print("\n\nVous avez Gagné")
        else:
            print("\n\nVous avez Perdu")
        print("Ordinateur :", comput_score)
        print("Vous :", player_score, "\n\n")
        time.sleep(1)
        if player_score == game_lenght:
            break
        elif comput_score == game_lenght:
            break
        answer = input("Voulez-vous continuer ? (O/N)").upper()
        if answer == "O":
            print("\nLa partie continue")
            time.sleep(0.5)
            A1 = " "
            A2 = " "
            A3 = " "

            B1 = " "
            B2 = " "
            B3 = " "

            C1 = " "
            C2 = " "
            C3 = " "
            terrain.clear()
            terrain.append(A1)
            terrain.append(A2)
            terrain.append(A3)
            terrain.append(B1)
            terrain.append(B2)
            terrain.append(B3)
            terrain.append(C1)
            terrain.append(C2)
            terrain.append(C3)
        else:
            break
print("Fin de Partie")

        

            



    

