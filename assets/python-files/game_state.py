import curses
from curses.textpad import Textbox, rectangle
from curses import wrapper
import os
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
    """
    def __init__(self, users_db):
        self.rocket_file = open('rocket_js_code.txt')    
        self.code_to_type = self.rocket_file.read()
        self.rocket_file.close()
        self.users_credentials = users_db
        

    def game_start(self):
        """
        Initialisez the curses window where all the typing-related flow will run 
        """
        width = os.get_terminal_size()[0]
        height = os.get_terminal_size()[1]
        stdscr = curses.initscr()
        curses.noecho()
        stdscr.refresh()        
        stdscr.addstr(0, 0, self.code_to_type)

        
        file_map = self.code_to_type_map()
        for count_row in range(len(file_map)):
            for char in file_map[count_row]['text']:
                key_press = stdscr.getkey()
                stdscr.addstr(count_row, char['x_coord'], key_press)
                # if char['char'] = stdscr.getkey() yada yada xD 
        curses.endwin()




    def code_to_type_map(self):
        """
        Creates a map of the text to be typed by the user, that offers the right coordinates for highlighting and typing over the text
        """
        lines = []
        with open(r"rocket_js_code.txt", 'r') as fp:
            for count, line in enumerate(fp): 
                number_of_spaces = line.count('\t') * 8
                line = line.replace('\t','').replace('\n','')
                lines.append({'text' : [{'char':char, 'x_coord':index + number_of_spaces} for char, index in zip(list(line), range(len(line)))],
                              'length' : len(line), 
                              'indentation' : number_of_spaces})
                #spearate and make out the number of \t
                #separate and store the \n at the end
                #
                #print(lines[count])
        #print('Total Lines', count + 1)
        #print(lines,'\n')
        
        return lines
        



    def view_progress(self):
        """
        will display the user's Dashboard 
        runs home_menu after displaying the user's progress 
        """
        print(self.users_credentials.col_values(1))
        self.code_to_type_map()
                
    def home_menu(self):
        """
        Brings up a home menu with 3 options: 
        Start typing
        View your progress
        Log Out
        """
        print("1. Start typing") 
        print("2. View your progress") 
        print("3. Log Out")
        
        user_home_menu_choice =input('Type in one of the above options:')
        if user_home_menu_choice == '1':
            self.game_start()
        elif user_home_menu_choice == '2':
            self.view_progress()
        elif user_home_menu_choice == '3':
            GREEN_MESSAGE = colored('\n\nSuccessfuly logged out', 'green', attrs=['reverse', 'blink']) 
            print(GREEN_MESSAGE)
            return False
        else:
            ERROR = colored('please type in one of the options in the menu', 'red', attrs=['reverse', 'blink'])
            print(ERROR)

##notes
        # curses.init_pair(1, curses.COLOR_BLUE, curses.COLOR_YELLOW)
        # curses.init_pair(2, curses.COLOR_GREEN, curses.COLOR_BLACK)
        # BLUE_AND_YELLOW = curses.color_pair(1)
        # GREEN_AND_BLACK = curses.color_pair(2)

