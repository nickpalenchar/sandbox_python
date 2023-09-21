import curses
from time import sleep

WALL = "#"

class Screen:
    def __init__(self, stdscr, w, h):
        self._stdscr = stdscr
        self.w = w
        self.h = h

    def refresh(self, points, strict=False):

        for y, x, char in self.get_border_points():
            self._stdscr.addstr(y, x, char)
        for y, x, char in points:
            self._stdscr.addstr(y, x, char[0])
        
        self._stdscr.refresh()

    def get_border_points(self):
        
        #return  [(40, y, WALL) for y in range(self.h)] #+ [(y, self.w-1, WALL) for y in range(self.h)]
        return [(0, x, WALL) for x in range(self.w)] + [(y, 0, WALL) for y in range(self.h)] + [(y, self.w-1, WALL) for y in range(self.h)] + [(self.h-1, x, WALL) for x in range(self.w)]


def main(stdscr):
    # init functions
    curses.noecho()
    stdscr.keypad(True)

    screen = Screen(stdscr, 40, 20)

    screen.refresh([(0,0, 'X')])
    sleep(2)

if __name__ == '__main__':
    curses.wrapper(main)
    print('done')
