import curses
from time import sleep

def main(stdscr):
    # init functions
    curses.noecho()
    stdscr.keypad(True)
    
    # add string hello, call refresh to actually display
    stdscr.addstr('hello')
    stdscr.refresh()
    sleep(2)

    # erase hello and then add a new string, call
    # refresh to update the screen. The resulting
    # effect is hello is replaced by goodbye
    stdscr.erase()
    stdscr.addstr('goodbye')
    stdscr.refresh()
    sleep(2)

if __name__ == '__main__':
    curses.wrapper(main)
    print('done')
