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
        self.input_evaluator(stdscr)        
        curses.endwin()

    def input_evaluator(self, screen):
        """
        parses and evaluates the user input and sends the screen, file_map, and the user input to the render functions
        """
        self.render_document(screen)
        enter_key_unix_code = 10
        backspace_key_unix_code = 127
        file_map = self.code_to_type_map()

        code_tiped= []
        count_row = 0
        
        while True:
            code_tiped.append([])
            char_index = 0
            
            while char_index < file_map[count_row]['length']:
                screen.addstr(50, 10, '  ')
                screen.addstr(50, 10, f'{char_index}')
                key_press = screen.getkey() 
                if ord(key_press) == enter_key_unix_code:
                    key_press = '\n'

                if ord(key_press)== backspace_key_unix_code:
                    if char_index == 0 and count_row > 0:
                        code_tiped.pop()
                        while  code_tiped[-1] == []:
                            count_row -= 1
                            code_tiped.pop()
                        code_tiped[-1].pop()  
                        count_row -= 1
                        char_index = len(code_tiped[-1])
                        self.render_document(screen)
                        self.render_user_input(file_map, code_tiped, screen)
                     
                    elif char_index > 0:
                        code_tiped[-1].pop() 
                        char_index -= 1      
                        self.render_document(screen)
                        self.render_user_input(file_map, code_tiped, screen)
                    
                elif key_press == file_map[count_row]['text'][char_index]:    
                    code_tiped[count_row].append(key_press)
                    char_index += 1
                    self.render_document(screen)
                    self.render_user_input(file_map, code_tiped, screen)
                    
                
                        
                
            count_row += 1

    def render_document(self, screen):
            '''
            renders the base document underneath the user input
            '''
            screen.addstr(0, 0, self.code_to_type)

            
    def render_user_input(self,file_map, input_tree, screen):
            ''' 
            renders the completed part of the document that the user has typed
            '''
            curses.start_color()
            curses.init_pair(1, curses.COLOR_BLUE, curses.COLOR_YELLOW)
            BLUE_AND_YELLOW = curses.color_pair(1)
            count = 0
            for file_row, input_row in zip(file_map, input_tree):
                screen.addstr(count, file_row['indentation']*8, ''.join(input_row), BLUE_AND_YELLOW)
                    
                count += 1
            
            

    def code_to_type_map(self):
        """
        Creates a map of the text to be typed by the user, that offers the right coordinates for highlighting and typing over the text
        """
        lines = []
        with open(r"rocket_js_code.txt", 'r') as fp:
            for count, line in enumerate(fp): 
                number_of_spaces = line.count('\t')
                line = line.replace('\t', '')
                if line[0] == '\n':
                    line = line.replace('\n', '')
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
       

        # curses.init_pair(2, curses.COLOR_GREEN, curses.COLOR_BLACK)
        # GREEN_AND_BLACK = curses.color_pair(2)

