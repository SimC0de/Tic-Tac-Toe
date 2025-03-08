import time
import os

os.system('cls||clear') # Clear terminal everytime py file is executed

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
choose_opponent = input("""
Choose your opponent!
1. Computer (PvC)
2. Player (PvP)
""").strip()

# If 1 or 2 is not chosen, execute this code:
while choose_opponent != ("1" or "2"):
  print("\033[A", end="\r") # Moves the cursor up by one line
  print("\033[K", end="\r") # Clears the whole line
  
  # Moves the cursor up by four lines
  for i in range(4):
    print("\033[A", end="\r")
  
  # Choose 1 or 2 to pick opponent
  choose_opponent = input("""
Please select No. 1 or No.2:
1. Computer (PvC)
2. Player (PvP)
"""
).strip()
# End of While Loop