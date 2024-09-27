from ascii_arts import *
from messages import *
                 
print(header)      
print(numbered_board)           

# Choose opponent through user input
opponent_input = input(message)       

# Checks the chosen opponent
opponent = ""
while(opponent_input):
    if(opponent_input == "1"):
        print("Fighting Player")
        opponent = "Player"
        break
    elif(opponent_input == "2"):
        print("Fighting Computer")
        opponent = "Computer"
        break
    else:
        opponent_input = input(warning_message)
                           