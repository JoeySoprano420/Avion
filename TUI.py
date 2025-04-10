import curses
import time

# Initialize curses screen
def init_screen(stdscr):
    curses.curs_set(0)  # Hide cursor
    stdscr.nodelay(1)  # Non-blocking input
    stdscr.timeout(100)  # Set timeout for non-blocking input
    stdscr.clear()

    # Set up colors
    curses.start_color()
    curses.init_pair(1, curses.COLOR_CYAN, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_YELLOW, curses.COLOR_BLACK)

    # Main loop
    while True:
        stdscr.clear()
        # Get user input
        key = stdscr.getch()

        # Show example pulse animation
        stdscr.addstr(2, 0, ">> Pulse Feed: ", curses.color_pair(3))
        stdscr.addstr(3, 0, "~ * > -", curses.color_pair(1))

        # Stack display example
        stdscr.addstr(6, 0, ">> Stack: ", curses.color_pair(3))
        stdscr.addstr(7, 0, "R0: 0001   R1: 0002   R2: 0003", curses.color_pair(1))

        # Display errors in Avion glyphs
        stdscr.addstr(10, 0, "Error: !err::Pulse[bit-slip] #EID:22FC", curses.color_pair(2))
        stdscr.addstr(11, 0, "Execution Drift level: Medium", curses.color_pair(2))

        # Epoch Clock
        stdscr.addstr(13, 0, f"Epoch: {int(time.time()) % 100}", curses.color_pair(1))

        # Refresh screen
        stdscr.refresh()

        # Exit on 'q'
        if key == ord('q'):
            break

# Run the curses application
if __name__ == "__main__":
    curses.wrapper(init_screen)
