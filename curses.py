import curses
from curses import wrapper
import os
from curses.textpad import Textbox, rectangle

def main(stdscr):
    width = os.get_terminal_size()[0]
    height = os.get_terminal_size()[1]
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
wrapper(main)