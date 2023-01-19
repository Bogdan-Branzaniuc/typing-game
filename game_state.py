import curses
from curses.textpad import Textbox, rectangle
from curses import wrapper
import os

# class Game
# methods: read the source code and return it
# create indentation map based on the text file
# use the map for the typing overlay method
# create access to backspace, capsLock and shift keys 

class Game:
    def __init__(self, filename):
        self.rocket_file = open(filename)    
        self.code_to_type = self.rocket_file.read()
        self.rocket_file.close()


    def game_start(self, stdscr):
        """
        Initialisez the curses window where all the game-related flow will run 
        """
        width = os.get_terminal_size()[0]
        height = os.get_terminal_size()[1]
       
        
        stdscr.refresh()        
        stdscr.addstr(0, 0, self.code_to_type)
        stdscr.getch()

    def code_to_type_map(self):
        """
        Creates a map of the text to be typed by the user, that offers the right coordinates for highlighting and typing over the text
        """
        with open(r"rocket_js_code.txt", 'r') as fp:
            for count, line in enumerate(fp):
                pass
        print('Total Lines', count + 1)
        

##notes
        # curses.init_pair(1, curses.COLOR_BLUE, curses.COLOR_YELLOW)
        # curses.init_pair(2, curses.COLOR_GREEN, curses.COLOR_BLACK)
        # BLUE_AND_YELLOW = curses.color_pair(1)
        # GREEN_AND_BLACK = curses.color_pair(2)