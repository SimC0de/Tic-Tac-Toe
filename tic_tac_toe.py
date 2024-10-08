from ascii_arts import *
from messages import *
import os
import time

os.system('cls')
print(header)      
print(title_board)           

input("Press enter to start:\n")
os.system('cls')

# Choose opponent through user input
choose_opponent_input = input(message)       

# Checks the chosen opponent
opponent = ""
while (bool(choose_opponent_input) != True):
    os.system('cls')
    choose_opponent_input = input(warning_message)

if (choose_opponent_input == "1"):
    print("Fighting Player")
    opponent = "Player"
elif (choose_opponent_input == "2"):
    print("Fighting Computer")
    opponent = "Computer"

os.system('cls')

if (opponent == "Player"):
    game_is_over = False
    #Temporary numbered board
    lsb = list_number_board
    #Temporary block references
    tbr = block_references
    #Temporary block list
    tbs = block_list
    while (game_is_over != True):
        # Checks if all the blocks are Xs or Os
        if all(i == 'X' or i == 'O' for i in tbr):
            tbr = block_references
            lsb = list(numbered_board)
        
        # Joins and print the listed numbered board
        game_board = "".join(lsb)
        print(game_board)
        
        # Check if Player 1's turn is valid
        player_1_turn = input(player_1_turn_message).strip()
        while bool(player_1_turn in tbr) == False:
            os.system('cls')
            print(game_board)
            player_1_turn = input(turn_warning_message)
        
        # Updates the board
        tbr = list(map(lambda x: x.replace(player_1_turn, 'O'), tbr))
        tbr_winning_conditions = [[tbr[0], tbr[1], tbr[2]],
                      [tbr[3], tbr[4], tbr[5]],
                      [tbr[6], tbr[7], tbr[8]],
                      [tbr[0], tbr[3], tbr[6]],
                      [tbr[1], tbr[4], tbr[7]],
                      [tbr[2], tbr[5], tbr[8]],
                      [tbr[0], tbr[4], tbr[8]],
                      [tbr[2], tbr[4], tbr[6]],]
        
        # Changes the chosen numbered block to X
        for i in range(0,11):
            for j in range(0, 19):
                lsb[tbs[int(player_1_turn)-1][i][j]] = o_s[block_x_o[i][j]]
                
        # Checks if there is a win condition in 'check_winning_conditions'
        check_winning_conditions = any(len(set(win_condition)) == 1 for win_condition in tbr_winning_conditions)
        if  check_winning_conditions:
            os.system('cls')
            game_board = "".join(lsb)
            print(game_board)
            print("Player 1 Wins!")
            game_is_over = True
            break
        
        # Clears the board to see that lsb(temporary list_numbered board) is updated
        os.system('cls')
        
        #Checks if all the blocs are either Xs or Os
        if all(i == 'X' or i == 'O' for i in tbr):
            tbr = block_references
            lsb = list(numbered_board)
            
        # Joins and print the listed numbered board
        game_board = "".join(lsb)
        print(game_board)
        
        # Check if Player 2's turn is valid
        player_2_turn = input(player_2_turn_message).strip()
        while bool(player_2_turn in tbr and player_2_turn) == False:
            os.system('cls')
            print(game_board)
            player_2_turn = input(turn_warning_message)
            
        # Updates the board
        tbr = list(map(lambda x: x.replace(player_2_turn, 'X'), tbr))
        tbr_winning_conditions = [[tbr[0], tbr[1], tbr[2]],
                      [tbr[3], tbr[4], tbr[5]],
                      [tbr[6], tbr[7], tbr[8]],
                      [tbr[0], tbr[3], tbr[6]],
                      [tbr[1], tbr[4], tbr[7]],
                      [tbr[2], tbr[5], tbr[8]],
                      [tbr[0], tbr[4], tbr[8]],
                      [tbr[2], tbr[4], tbr[6]],]
        
        # Changes the chosen numbered block to X
        for i in range(0,11):
            for j in range(0, 19):
                lsb[tbs[int(player_2_turn)-1][i][j]] = x_s[block_x_o[i][j]]
                
        # Checks if there is a win condition in 'check_winning_conditions'
        check_winning_conditions = any(len(set(win_condition)) == 1 for win_condition in tbr_winning_conditions)
        if  check_winning_conditions:
            os.system('cls')
            game_board = "".join(lsb)
            print(game_board)
            print("Player 2 Wins!")
            game_is_over = True
            break
        
        # Clears the board to see that lsb(temporary list_numbered board) is updated
        os.system('cls')