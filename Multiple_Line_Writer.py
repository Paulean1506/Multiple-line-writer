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
        add_lines = input("Are there more lines y/n? ")

        # Prompts user to only enter 'y' and 'n'
        while not add_lines or add_lines[0].lower() not in ['y', 'n']:
            add_lines=input("Invalid input, please only enter 'y', or 'n'")

        # Allows user to input another line if 'y' is entered
        while add_lines.lower() == 'y':
            line = input("Enter line: ")
            file.write(line + "\n")
            add_lines = input("Are there more lines y/n? ")

    # Ends the program if 'n' is entered
            if add_lines.lower() == 'n':
                print("Hope you enjoyed this little activity<3!")
                print("")
                break    

des = pyfiglet.figlet_format("You can find what you've entered in the mylife.txt file", font = "digital")
print(des)

r = Figlet(font = "banner3-d")
print(colored(r.renderText('Thank you!'), 'red'))

# Call the method to run the code
write_to_file()