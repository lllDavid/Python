import curses
import time

def main(stdscr):
    stdscr.clear()

    curses.curs_set(0)

    curses.start_color()
    curses.init_pair(1, curses.COLOR_YELLOW, curses.COLOR_BLUE)

    height, width = stdscr.getmaxyx()

    message = "Hello, Curses!"
    x = (width // 2) - (len(message) // 2)
    y = height // 2

    stdscr.attron(curses.color_pair(1))
    stdscr.addstr(y, x, message)
    stdscr.attroff(curses.color_pair(1))

    stdscr.refresh()

    time.sleep(5)

    for i in range(width - 1):
        stdscr.clear()
        stdscr.addstr(y, i, "*")
        stdscr.refresh()
        time.sleep(0.05)

    stdscr.addstr(height - 1, 0, "Press any key to exit...")
    stdscr.refresh()
    stdscr.getch()

curses.wrapper(main)