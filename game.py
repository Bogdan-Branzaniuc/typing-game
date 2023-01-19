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
        curses.init_pair(1, curses.COLOR_BLUE, curses.COLOR_YELLOW)
        curses.init_pair(2, curses.COLOR_GREEN, curses.COLOR_BLACK)
        BLUE_AND_YELLOW = curses.color_pair(1)
        GREEN_AND_BLACK = curses.color_pair(2)

        win = curses.newwin(height, width, 0, 0)
        box = Textbox(win)
        rectangle(stdscr, 2, 2, height-2, width-2)
        stdscr.refresh()
        box.edit()
        text = box.gather().strip().replace("\n", "")
        stdscr.addstr(5, 20, self.code_to_type)
        stdscr.getch()

game = Game('rocket_js_code.txt')       
wrapper(game.game_start)