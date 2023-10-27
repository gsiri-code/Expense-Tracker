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
            for i, line in enumerate(lines[current_line:current_line + height - 1]):  # Reserve 1 line for instructions
                stdscr.addstr(i, 0, line)

            # Display instructions
            instructions = "Use 'j' or arrow down to scroll down, 'k' or arrow up to scroll up, and 'q' to quit."
            stdscr.addstr(height - 1, 0, instructions)

            stdscr.refresh()

            # Get user input
            key = stdscr.getch()

            # Quit
            if key == ord('q'):
                break

            # Scroll down with 'j'
            elif (key == curses.KEY_DOWN or key == ord('j')) and current_line < len(lines) - height + 1:
                current_line += 1

            # Scroll up with 'k'
            elif (key == curses.KEY_UP or key == ord('k')) and current_line > 0:
                current_line -= 1

    curses.wrapper(main)


