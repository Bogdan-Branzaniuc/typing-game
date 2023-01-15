import curses
from curses import wrapper
from curses.textpad import Textbox, rectangle


print('This is a typing game to enhance your programming typing skills:')
user_name = input('What is your username?\n')


def main(stdscr):
    #  curses.init_pair(1, curses.COLOR_BLUE, curses.COLOR_YELLOW)
    #  curses.init_pair(2, curses.COLOR_GREEN, curses.COLOR_BLACK)
    #  BLUE_AND_YELLOW = curses.color_pair(1)
    #  GREEN_AND_BLACK = curses.color_pair(2)

    win = curses.newwin(8, 100, 2, 2)
    box = Textbox(win)
    rectangle(stdscr, 2, 2, 8, 100)
    stdscr.refresh()
    box.edit()
    text = box.gather().strip().replace("\n", "")
    stdscr.addstr(5, 20, text)
    stdscr.addstr('message')
    stdscr.getch()
     

wrapper(main)