import os
import time

# Welcome message to display
welcome_message = "Welcome to Survival of the Fittest\nThis is a game made by Downward Spiral Studios\n\n"

# The name for the windows OS
windows_os_name = "nt"

# Commands for each OS to clear the terminal
clear_screen_command_windows = "cls"
clear_screen_command_other = "clear"


# Clear the terminal screen
def clear_screen():
    # Sleep for a second
    time.sleep(1)
    # Call clear screen command
    os.system(clear_screen_command_windows if os.name==windows_os_name else clear_screen_command_other)
    
# Welcome the player with the welcome message
def welcome():
    print(welcome_message)
    

def main():    
    clear_screen()
    welcome()
    
# Called if script is run
if __name__ == '__main__':
    main()
