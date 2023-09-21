import curses
from time import sleep


class Screen:
    def __init__(self, stdscr, w, h):
        self._stdscr = stdscr
        self.w = w
        self.h = h

    def refresh(self, points):
        screen = [["·" for _ in range(self.w)] for _ in range(self.h)]

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
