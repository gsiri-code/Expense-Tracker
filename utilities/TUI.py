import curses



def create_view(content):
    def main(stdscr):
        curses.curs_set(0)  # Hide cursor
        stdscr.nodelay(0)  # Set to blocking mode
        stdscr.timeout(100)  # Set a timeout

        lines = str(content).split('\n')
        current_line = 0

        while True:
            stdscr.clear()

            # Display text
            height, width = stdscr.getmaxyx()
            for i, line in enumerate(lines[current_line:current_line + height]):
                stdscr.addstr(i, 0, line)

            stdscr.refresh()

            # Get user input
            key = stdscr.getch()

            # Quit
            if key == ord('q'):
                break

            # Scroll down
            elif key == curses.KEY_DOWN and current_line < len(lines) - height:
                current_line += 1

            # Scroll up
            elif (key == curses.KEY_UP) and current_line > 0:
                current_line -= 1

    curses.wrapper(main)