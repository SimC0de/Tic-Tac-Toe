from ascii_arts import *
from messages import *
                 
print(header)      
print(empty_board)           

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
        print(tbr_winning_conditions)
        for win_condition in tbr_winning_conditions:
            if (len(set(win_condition)) == 1):
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
        print(tbr_winning_conditions)
        for win_condition in tbr_winning_conditions:
            if (len(set(win_condition)) == 1):
                print("Player 2 Wins!")
                game_is_over = True
                break
                
                
                
                
        # player2_turn = input(player2_turn_message)
        # player_2_turn_validation = player2_turn in tbr and player2_turn != "".strip()
        # while (player_2_turn_validation):
        #     if player_1_turn_validation:
        #         tbr = list(map(lambda x: x.replace(player2_turn, 'X'), tbr))
        #         print(tbr)
        #         tbr_winning_conditions = [[tbr[0], tbr[1], tbr[2]],
        #                       [tbr[3], tbr[4], tbr[5]],
        #                       [tbr[6], tbr[7], tbr[8]],
        #                       [tbr[0], tbr[3], tbr[6]],
        #                       [tbr[1], tbr[4], tbr[7]],
        #                       [tbr[2], tbr[5], tbr[8]],
        #                       [tbr[0], tbr[4], tbr[8]],
        #                       [tbr[2], tbr[4], tbr[6]],]
        #         tbr_winning_conditions
        #         print(tbr_winning_conditions)
        #         break
        #     else:
        #         player2_turn = (turn_warning_message)
            
            
                
            
            
        
        
        
        


                           