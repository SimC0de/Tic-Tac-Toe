import os
import sys
import random

print("##### #####  ###      #####  ###   ###      ##### ##### #####") 
print("  #     #   #   #       #   #   # #   #       #   #   # #    ")
print("  #     #   #     ###   #   ##### #     ###   #   #   # #####")
print("  #     #   #   #       #   #   # #   #       #   #   # #    ")
print("  #   #####  ###        #   #   #  ###        #   ##### #####")  
print()
print("=============================================================")

# #1 = index #14, #2 = index #18, #3 = index #22
# #4 = index #62, #5 = index #66, #6 = index #70
# #7 = index #110, #8 = index #114, #9 = index #118
ttt_area = """
   |   |   
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
        print("1 works")
        choose_opponent = False
    elif choose_opponent == "2":
        choose_computer = input("Choose computer difficulty\n1. Easy\n2. Medium(Not Available)\n3. Hard\n")
        while choose_computer:
            if choose_computer == "1":
                game_done = False
                while game_done == False:
                    print("=============================================================")
                    print()
                    print(ttt_area)
                    player1_choice = input("What area would you like to mark?\n")
                    computer_choice = random.randint(1, 9)
                    print(f"computer marked area {computer_choice}")
        choose_opponent = False
    elif choose_opponent == "3":
        print("3 words")
        choose_opponent = False
    else:
        choose_opponent = input("Not a valid choice\nInput \"1\" to choose another player as an opponent...\nInput \"2\" to choose a computer as an opponent...\nInput \"3\" to to exit the program...\n")