import time
import os

os.system('cls||clear') # Clear terminal everytime py file is executed

#Input messages
choose_opponent_msg = "\nChoose your opponent!\n1. Computer (PvC)\n2. Player (PvP)\n"
choose_opponent_x_msg = "\nPlease select No. 1 or No.2:\n1. Computer (PvC)\n2. Player (PvP)\n"
choose_pvp_msg = "Computer is still in progress, do you want to play pvp?(y/n):\n"
choose_pvp_x_msg = "Please choose between 'y' (yes) or 'n' (no) to choose PVP.(y/n):\n"

# Tic-Tac-Toe Block
block = """.--------------..--------------..--------------.
|  _________   ||     _____    ||     ______   |
| |  _   _  |  ||    |_   _|   ||   .' ___  |  |
| |_/ | | \_|  ||      | |     ||  / .'   \_|  |
|     | |      ||      | |     ||  | |         |
|    _| |_     ||     _| |_    ||  \ `.___.'\  |
|   |_____|    ||    |_____|   ||   `._____.'  |
|              ||              ||              |
'--------------''--------------''--------------'
.--------------..--------------..--------------.
|  _________   ||      __      ||     ______   |
| |  _   _  |  ||     /  \     ||   .' ___  |  |
| |_/ | | \_|  ||    / /\ \    ||  / .'   \_|  |
|     | |      ||   / ____ \   ||  | |         |
|    _| |_     || _/ /    \ \_ ||  \ `.___.'\  |
|   |_____|    |||____|  |____|||   `._____.'  |
|              ||              ||              |
'--------------''--------------''--------------'
.--------------..--------------..--------------.
|  _________   ||     ____     ||  _________   |
| |  _   _  |  ||   .'    `.   || |_   ___  |  |
| |_/ | | \_|  ||  /  .--.  \  ||   | |_  \_|  |
|     | |      ||  | |    | |  ||   |  _|  _   |
|    _| |_     ||  \  `--'  /  ||  _| |___/ |  |
|   |_____|    ||   `.____.'   || |_________|  |
|              ||              ||              |
'--------------''--------------''--------------'"""

# Animate print statement
for i in block:
  print(i, end="", flush=True)
  time.sleep(0.001)

time.sleep(1) # Add delay before executing input

# Choose 1 or 2 to pick opponent
choose_opponent = input(choose_opponent_msg).strip()

# If 1 or 2 is not chosen, execute this code:
while choose_opponent not in ["1", "2"]:
  print("\033[A", end="\r") # Moves the cursor up by one line
  print("\033[K", end="\r") # Clears the whole line
  
  # Moves the cursor up by four lines
  for i in range(4):
    print("\033[A", end="\r")
  
  # Choose 1 or 2 to pick opponent
  choose_opponent = input(choose_opponent_x_msg).strip()
# End of While Loop

# Computer Opponent
if choose_opponent == "1":
  print("\033[A", end="\r") # Moves the cursor up by one line
  print("\033[K", end="\r") # Clears the whole line
  
  # Moves the cursor up and clear the lines by 2
  for i in range(3):
    print("\033[A", end="\r")
    print("\033[K", end="\r")
    
  choose_pvp = input(choose_pvp_msg).strip()

  while choose_pvp not in ["y", "n"]:
    print("\033[A", end="\r") # Moves the cursor up by one line
    print("\033[K", end="\r") # Clears the whole line
  
    # Moves the cursor up by 1 lines
    for i in range(1):
      print("\033[A", end="\r")
    choose_pvp = input(choose_pvp_x_msg).strip()
  
  if choose_pvp == 'y':
    choose_opponent = "2"
  elif choose_pvp == 'n':
    os.system('cls||clear')
    print('buh-bye!')

# Player Opponent
if choose_opponent == "2":
  print("No. 2")