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
        
        self.input_evaluator()
                 
        curses.endwin()

    def input_evaluator(self):
        """
        evaluates the user key input and reveals the typed content or the original document according to the red-green cases
        """
        enter_key_unix_code = 10
        enter_key_unix_code = 127
        file_map = self.code_to_type_map()
        
        code_tiped=[]
        count_row = 0
        while True:
            row_text = file_map[count_row]['text']
            row_length = file_map[count_row]['length']
            row_indentation = file_map[count_row]['indentation']
            
            stdscr.addstr(count_row, 0, row_indentation * "\t")
            
            char_index = 0
            x_coord = stdscr.getyx()[1] 
            while char_index < row_length:
                self.render_document()
                self.render_user_input()               
                key_press = stdscr.getkey()
                # is it the end
                # is it the beggining
                # is it correct   
                stdscr.addstr(count_row, x_coord, key_press)
                x_coord += 1
                char_index += 1
                stdscr.addstr(50, 10, f'{char_index}')
            count_row += 1

    def render_document(self):
            '''
            renders the part of the document that's left to be typed
            '''
            stdscr.addstr(0, 0, self.code_to_type)

            
    def render_user_input(self, input_tree):
            ''' 
            renders the completed part of the document that the user has typed
            '''
            # the reverse of map
            

    def code_to_type_map(self):
        """
        Creates a map of the text to be typed by the user, that offers the right coordinates for highlighting and typing over the text
        """
        lines = []
        with open(r"rocket_js_code.txt", 'r') as fp:
            for count, line in enumerate(fp): 
                number_of_spaces = line.count('\t')
                line = line.replace('\t', '').replace('\n','')
                lines.append({'text' : [char for char in list(line)],
                              'length' : len(line), 
                              'indentation' : number_of_spaces})
                #print(lines[count],'\n\n')
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

