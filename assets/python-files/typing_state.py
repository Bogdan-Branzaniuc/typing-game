import curses
from curses.textpad import Textbox, rectangle
from curses import wrapper
import os
import colorama
from colorama import Fore 
from termcolor import colored, cprint

from game import Game

# class Game
# methods: read the source code and return it
# create indentation map based on the text file
# use the map for the typing overlay method
# create access to backspace, capsLock and shift keys 

class Typing_state():
    """
    Contains all the game-related methods 
    """
    def __init__(self):  
        self.file_name = ''  

        self.mistakes = 0
        self.time = 0
        self.wpm = 0

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
        file_map = self.code_to_type_map(self.file_name)

        code_typed= []
        wrong_typed= 0
        typeable_characters = 0
        typed_characters = 0
        
        count_row = 0       
        while count_row <= len(file_map)-1:
            code_typed.append([])
            char_index = 0
            
            while char_index < file_map[count_row]['length']:
                screen.move(count_row, char_index + file_map[count_row]['indentation']*8)
                key_press = screen.getkey()
                typed_characters += 1 
                
                if ord(key_press) == enter_key_unix_code:
                    key_press = '\n'     
                if ord(key_press)== backspace_key_unix_code:
                    if wrong_typed > 0:
                        wrong_typed -= 1
                        code_typed[count_row].pop() 
                        self.render_document(screen)
                        self.render_user_input(file_map, code_typed, wrong_typed, screen)
                    elif char_index == 0 and count_row > 0:
                        code_typed.pop()
                        while  code_typed[-1] == []:
                            count_row -= 1
                            code_typed.pop()
                        code_typed[-1].pop()  
                        count_row -= 1
                        char_index = len(code_typed[-1])                             
                        self.render_document(screen)
                        self.render_user_input(file_map, code_typed, wrong_typed, screen)
 
                    elif char_index > 0:
                        code_typed[-1].pop() 
                        char_index -= 1      
                        self.render_document(screen)
                        self.render_user_input(file_map, code_typed, wrong_typed, screen)
                    
                elif key_press == file_map[count_row]['text'][char_index] and wrong_typed == 0:    
                    code_typed[count_row].append(key_press)
                    char_index += 1
                    self.render_document(screen)
                    self.render_user_input(file_map, code_typed, wrong_typed, screen)
                                       
                elif key_press != file_map[count_row]['text'][char_index] and wrong_typed <= 5:  
                    wrong_typed += 1 
                    code_typed[count_row].append('X')
                    self.mistakes += 1
                    self.render_document(screen)
                    self.render_user_input(file_map, code_typed, wrong_typed, screen)
            count_row += 1
       
            

    def render_document(self, screen):
            '''
            renders the base document underneath the user input
            '''
            file = open(self.file_name)    
            code_to_type = file.read()
            file.close()
            screen.addstr(0, 0, code_to_type)

            
    def render_user_input(self,file_map, input_tree,wrong_typed, screen):
            ''' 
            renders the completed part of the document that the user has typed
            '''
            curses.start_color()
            curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
            curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
            GREEN = curses.color_pair(1)
            RED = curses.color_pair(2) 
            color = RED if wrong_typed > 0 else GREEN
            count = 0
            for file_row, input_row in zip(file_map, input_tree):    
                screen.addstr(count, file_row['indentation']*8 + len(file_row['text']), '      ')
                screen.addstr(count, file_row['indentation']*8, ''.join(input_row), color)
                count += 1
                

    def code_to_type_map(self, file):
        """
        Creates a map of the text to be typed by the user, that offers the right coordinates for highlighting and typing over the text
        """
        lines = []
        with open(file, 'r') as fp:
            for count, line in enumerate(fp): 
                number_of_spaces = line.count('\t')
                line = line.replace('\t', '')
                if line[0] == '\n':
                    line = line.replace('\n', '')
                lines.append({'text' : [char for char in list(line)],
                              'length' : len(line), 
                              'indentation' : number_of_spaces})
        return lines