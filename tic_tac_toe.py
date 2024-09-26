from ascii_arts import *

                 
print(header)      
print(board)           

# Choose opponent through user inpute
opponent_input = input("Choose your opponent:\n1. Player (PvP)\n2. Computer (PvC)\n")       

# Check if user is still choosing an opponent
choose_opponent = True
while(choose_opponent):
    if(opponent_input == "1"):
        print("Fighting Player")
        choose_opponent = False
    elif(opponent_input == "2"):
        print("Fighting Computer")
        choose_opponent = False
    else:
        opponent_input = input("Please choose an opponent using the numbers that corresponds with them\n\nChoose your opponent:\n1. Player (PvP)\n2. Computer (PvC)\n")
                           