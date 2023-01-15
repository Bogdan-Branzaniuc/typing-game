import curses
import os
from curses import wrapper
from curses.textpad import Textbox, rectangle


print('This is a typing game to enhance your programming typing skills:')
#user_name = input('What is your username?\n')

# build the login logic
def auth():
    """
    auth will display input messages to the user to lig into their account or create a new one
    with the appropriate exceptions and permissions
    """    
    username = input("")
    

def main(stdscr):
    width = os.get_terminal_size()[0]
    height =  os.get_terminal_size()[1]
    #  curses.init_pair(1, curses.COLOR_BLUE, curses.COLOR_YELLOW)
    #  curses.init_pair(2, curses.COLOR_GREEN, curses.COLOR_BLACK)
    #  BLUE_AND_YELLOW = curses.color_pair(1)
    #  GREEN_AND_BLACK = curses.color_pair(2)

    win = curses.newwin(height, width, 0, 0)
    box = Textbox(win)
    rectangle(stdscr, 2, 2, height-2, width-2)
    stdscr.refresh()
    box.edit()
    input('tell me something')
    text = box.gather().strip().replace("\n", "")
    stdscr.addstr(5, 20, text)
    stdscr.addstr('message')
    stdscr.getch()    


auth()
#wrapper(main)
