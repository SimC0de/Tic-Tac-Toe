from ascii_arts import *
from messages import *
import os
import time

os.system('cls')
print(header)      
print(empty_board)           

input("Press enter to start:\n")
os.system('cls')

# Choose opponent through user input
choose_opponent_input = input(message)       

# Checks the chosen opponent
opponent = ""
while (choose_opponent_input):
    if (choose_opponent_input == "1"):
        print("Fighting Player")
        opponent = "Player"
        break
    elif (choose_opponent_input == "2"):
        print("Fighting Computer")
        opponent = "Computer"
        break
    else:
        choose_opponent_input = input(warning_message)

if (opponent == "Player"):
    game_is_over = False
    #Temporary numbered board
    tnb = numbered_board
    #Temporary block references
    tbr = block_references
    while (game_is_over != True):
        player_1_turn = input(player_1_turn_message)
        while bool(player_1_turn in tbr and player_1_turn != "".strip()) == False:
            player_1_turn = input(turn_warning_message)
        tbr = list(map(lambda x: x.replace(player_1_turn, 'O'), tbr))
        tbr_winning_conditions = [[tbr[0], tbr[1], tbr[2]],
                      [tbr[3], tbr[4], tbr[5]],
                      [tbr[6], tbr[7], tbr[8]],
                      [tbr[0], tbr[3], tbr[6]],
                      [tbr[1], tbr[4], tbr[7]],
                      [tbr[2], tbr[5], tbr[8]],
                      [tbr[0], tbr[4], tbr[8]],
                      [tbr[2], tbr[4], tbr[6]],]
        os.system('cls')
        print(tbr_winning_conditions)
        check_winning_conditions = any(len(set(win_condition)) == 1 for win_condition in tbr_winning_conditions)
        if  check_winning_conditions:
            print("Player 1 Wins!")
            game_is_over = True
            break
        player_2_turn = input(player_2_turn_message)
        while bool(player_2_turn in tbr and player_2_turn != "".strip()) == False:
            player_2_turn = input(turn_warning_message)
        tbr = list(map(lambda x: x.replace(player_2_turn, 'X'), tbr))
        tbr_winning_conditions = [[tbr[0], tbr[1], tbr[2]],
                      [tbr[3], tbr[4], tbr[5]],
                      [tbr[6], tbr[7], tbr[8]],
                      [tbr[0], tbr[3], tbr[6]],
                      [tbr[1], tbr[4], tbr[7]],
                      [tbr[2], tbr[5], tbr[8]],
                      [tbr[0], tbr[4], tbr[8]],
                      [tbr[2], tbr[4], tbr[6]],]
        os.system('cls')
        print(tbr_winning_conditions)
        check_winning_conditions = any(len(set(win_condition)) == 1 for win_condition in tbr_winning_conditions)
        if  check_winning_conditions:
            print("Player 2 Wins!")
            game_is_over = True
            break