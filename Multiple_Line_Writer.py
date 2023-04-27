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

# Open mylife.txt in write mode
with open("mylife.txt", "w") as file:

    # Ask user for input
    line = input(str("\033[95mEnter line: "))

    # Writes the input into the file
    file.write(line + "\n")

    # Asks user if they want to input more lines
    more_lines = input(str("Are there more lines", user_name, "?"))