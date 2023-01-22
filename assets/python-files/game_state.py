import curses
from curses.textpad import Textbox, rectangle
from curses import wrapper
import os
from auth import Auth
import colorama
from colorama import Fore 
from termcolor import colored, cprint
# class Game
# methods: read the source code and return it
# create indentation map based on the text file
# use the map for the typing overlay method
# create access to backspace, capsLock and shift keys 

class Game:
    """
    Contains all the game-functions
    uses auth object when logged out 
    """
    def __init__(self, auth_object, users_db):
        self.rocket_file = open('rocket_js_code.txt')    
        self.code_to_type = self.rocket_file.read()
        self.rocket_file.close()
        self.auth_object = auth_object
        self.users_credentials = users_db
        

    def game_start(self):
        """
        Initialisez the curses window where all the typing-related flow will run 
        """
        width = os.get_terminal_size()[0]
        height = os.get_terminal_size()[1]
        stdscr = curses.initscr()
        stdscr.refresh()        
        stdscr.addstr(0, 0, self.code_to_type)
        stdscr.getch()
        curses.endwin()

    def code_to_type_map(self):
        """
        Creates a map of the text to be typed by the user, that offers the right coordinates for highlighting and typing over the text
        """
        with open(r"rocket_js_code.txt", 'r') as fp:
            for count, line in enumerate(fp): 
                pass
        print('Total Lines', count + 1)

    def view_progress(self):
        """
        will display the user's Dashboard 
        runs home_menu after displaying the user's progress 
        """
        print(self.users_credentials.col_values(1))
        self.home_menu()
            

    def home_menu(self):
        """
        Brings up a home menu with 3 options: 
        Start typing
        View your progress
        Log Out
        """
        print('\n\n')
        print("1. Start typing") 
        print("2. View your progress") 
        print("3. Log Out")
        user_selection_input = input('Type in one of the above options:')
        if user_selection_input == '1':
            self.game_start()
        elif user_selection_input == '2':
            self.view_progress()
        elif user_selection_input == '3':
            GREEN_MESSAGE = colored('Successfuly logged out', 'green', attrs=['reverse', 'blink']) 
            print(GREEN_MESSAGE)
            self.auth_object.auth()
        else:
            ERROR = colored('please type in one of the options in the menu', 'red', attrs=['reverse', 'blink'])
            print(ERROR)
            self.home_menu()

##notes
        # curses.init_pair(1, curses.COLOR_BLUE, curses.COLOR_YELLOW)
        # curses.init_pair(2, curses.COLOR_GREEN, curses.COLOR_BLACK)
        # BLUE_AND_YELLOW = curses.color_pair(1)
        # GREEN_AND_BLACK = curses.color_pair(2)