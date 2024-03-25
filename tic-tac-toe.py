import os
import sys
import time
import random

print("##### #####  ###      #####  ###   ###      ##### ##### #####") 
print("  #     #   #   #       #   #   # #   #       #   #   # #    ")
print("  #     #   #     ###   #   ##### #     ###   #   #   # #####")
print("  #     #   #   #       #   #   # #   #       #   #   # #    ")
print("  #   #####  ###        #   #   #  ###        #   ##### #####")  
print()
print("=============================================================")
print()
# #1 = index #13, #2 = index #17, #3 = index #21
# #4 = index #61, #5 = index #65, #6 = index #69
# #7 = index #109, #8 = index #113, #9 = index #117
ttt_area = """   |   |   
 1 | 2 | 3 
   |   |   
-----------
   |   |   
 4 | 5 | 6 
   |   |   
-----------
   |   |   
 7 | 8 | 9 
   |   |    """

print(ttt_area)
print()

choose_opponent = input("Choose your opponent\n1. Player\n2. Computer\nTo close the program, press 3 or exit\n")

while choose_opponent:
    if choose_opponent == "1":
        choose_opponent = input('This is still in devlopment, please choose computer for your opponent\n1. Player\n2. Computer\nTo close the program, press 3 or exit\n')
    elif choose_opponent == "2":
        choose_computer = input("Choose computer difficulty\n1. Easy\n2. Medium(Not Available)\n3. Hard\n")
        while choose_computer:
            # Easy Computer
            if choose_computer == "1":
                # gta, short for game tic-tac-toe area
                gta = ttt_area
                while True:
                    print("=============================================================")
                    print()
                    print(gta)
                    # Player 1 Turn
                    player1_choice = input("What area would you like to mark?\n")
                    while player1_choice.isnumeric() == False or player1_choice == " " or player1_choice not in gta:
                        print("No")
                        player1_choice = input("Marked area or invalid input\n")
                    add_mark = gta.replace(player1_choice, "O")
                    gta = add_mark
                    if gta[13] == 'O' and gta[17] == 'O' and gta[21] == 'O':
                        print(gta)
                        print("Player Won")
                        choose_computer = 'end'
                        break
                    # Computer Turn
                    computer_choice = str(random.randint(1, 9))
                    while computer_choice not in gta:
                        computer_choice = str(random.randint(1, 9))
                    add_mark = gta.replace(computer_choice, "X")
                    gta = add_mark
                    print(f"computer marked area {computer_choice}")
            elif choose_computer == "2":
                choose_computer = input("\'Easy\' is the only available mode at the moment\n")
            elif choose_computer == "3":
                choose_computer = input("\'Easy\' is the only available mode at the moment\n")
            elif choose_computer == 'end':
                print("Game over!")
                break
        choose_opponent = False
    elif choose_opponent == "3":
        print("3 words")
        choose_opponent = False
        print("Game over!")
    else:
        choose_opponent = input("Not a valid choice\nInput \"1\" to choose another player as an opponent...\nInput \"2\" to choose a computer as an opponent...\nInput \"3\" to to exit the program...\n")