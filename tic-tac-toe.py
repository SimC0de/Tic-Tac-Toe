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

# Choose opponent
choose_opponent = input("Choose your opponent\n1. Player\n2. Computer\nTo close the program, press 3 or exit\n")
while choose_opponent:
    # Choose player as opponent
    if choose_opponent == "1":
        choose_opponent = input('This is still in devlopment, please choose computer for your opponent\n1. Player\n2. Computer\nTo close the program, press 3 or exit\n')
    # Choose computer as opponent
    elif choose_opponent == "2":
        #Choose computer difficulty
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
                    # Check if areas are all marked before player's turn
                    areas = [gta[13], gta[17], gta[21], gta[61], gta[65], gta[69], gta[109], gta[113], gta[117]]
                    areas_full = False
                    for area in areas:
                        if area == 'X' or area == 'O':
                            areas_full = True
                        else:
                            areas_full = False
                            break
                    if areas_full:
                        gta = ttt_area
                        print("Removing marks, Player 1 will have the first Turn!")
                    # Player 1 Turn
                    player1_choice = input("What area would you like to mark?\n")
                    while player1_choice.isnumeric() == False or player1_choice == " " or player1_choice not in gta:
                        print("No")
                        player1_choice = input("Marked area or invalid input\n")
                    add_mark = gta.replace(player1_choice, "O")
                    gta = add_mark
                    print(gta)
                    print()
                    print("=============================================================")
                    print()
                    # Player 1 Winning Conditions
                    if (gta[13] == 'O' and gta[17] == 'O' and gta[21] == 'O') or (gta[61] == 'O' and gta[65] == 'O' and gta[69] == 'O') or (gta[109] == 'O' and gta[113] == 'O' and gta[117] == 'O') or (gta[13] == 'O' and gta[61] == 'O' and gta[109] == 'O') or(gta[17] == 'O' and gta[65] == 'O' and gta[113] == 'O') or (gta[21] == 'O' and gta[69] == 'O' and gta[117] == 'O') or (gta[13] == 'O' and gta[65] == 'O' and gta[117] == 'O') or (gta[21] == 'O' and gta[65] == 'O' and gta[109] == 'O'):
                        print("Player Won")
                        # Choice to continue or not
                        choose_computer = input('Would you like to continue?\nType \'yes\' to continue, \'no\' to end the game\n').lower()
                        if choose_computer == 'yes':
                            choose_computer = '1'
                        else:
                            choose_computer = 'end'
                        break
                    # Check if areas are all marked before computer's turn
                    areas = [gta[13], gta[17], gta[21], gta[61], gta[65], gta[69], gta[109], gta[113], gta[117]]
                    areas_full = False
                    for area in areas:
                        if area == 'X' or area == 'O':
                            areas_full = True
                        else:
                            areas_full = False
                            break
                    if areas_full:
                        gta = ttt_area
                        print("Removing marks, Player 1 will have the first Turn!")
                    # Computer Turn
                    computer_choice = str(random.randint(1, 9))
                    while computer_choice not in gta:
                        computer_choice = str(random.randint(1, 9))
                    add_mark = gta.replace(computer_choice, "X")
                    gta = add_mark
                    print(f"computer marked area {computer_choice}")
                    print()
                    # Computer winning conditions
                    if (gta[13] == 'X' and gta[17] == 'X' and gta[21] == 'X') or (gta[61] == 'X' and gta[65] == 'X' and gta[69] == 'X') or (gta[109] == 'X' and gta[113] == 'X' and gta[117] == 'X') or (gta[13] == 'X' and gta[61] == 'X' and gta[109] == 'X') or(gta[17] == 'X' and gta[65] == 'X' and gta[113] == 'X') or (gta[21] == 'X' and gta[69] == 'X' and gta[117] == 'X') or (gta[13] == 'X' and gta[65] == 'X' and gta[117] == 'X') or (gta[21] == 'X' and gta[65] == 'X' and gta[109] == 'X'):
                        print(gta)
                        print("Computer Won")
                        # Choose to continue or not
                        choose_computer = input('Would you like to continue?\nType \'yes\' to continue, or any value to end the game\n').lower()
                        if choose_computer == 'yes':
                            choose_computer = '1'
                        else:
                            choose_computer = 'end'
                        break
            # Medium Computer
            elif choose_computer == "2":
                choose_computer = input("\'Easy\' is the only available mode at the moment\n")
            # Hard Computer
            elif choose_computer == "3":
                choose_computer = input("\'Easy\' is the only available mode at the moment\n")
            # Condition to end the terminal game
            elif choose_computer == 'end':
                print("Game over!")
                break
        choose_opponent = False
    # Exit the terminal game
    elif choose_opponent == "3":
        print("3 words")
        choose_opponent = False
        print("Game over!")
    else:
        choose_opponent = input("Not a valid choice\nInput \"1\" to choose another player as an opponent...\nInput \"2\" to choose a computer as an opponent...\nInput \"3\" to to exit the program...\n")