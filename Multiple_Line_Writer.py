# Paulean Marguerette F. Parrish
# Bscpe 1-4
# Problem no. 3
# Write a method in python to write multiple line of text contents into a text file mylife.txt.

# Header design
import pyfiglet

from termcolor import colored
from pyfiglet import Figlet
f = Figlet(font = "digital")
print(colored(f.renderText('Oh, Hello there!'), 'yellow'))

# Ask for the name of the user
user_name = input("\033[95mMay I know your name? \033[0m")
print("\n\033[94mThank you", user_name,  "enjoy the program!\n")

# Define write_to_file
def write_to_file():