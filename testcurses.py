import curses 

from curses import wrapper

title = """
  _____              _    _          _ _                   _            
 |_   _|__ _ _  _ _ (_)__| |__  __ _| | |__ _ _  _ _ _  __| |_  ___ _ _ 
   | |/ -_) ' \| ' \| (_-< '_ \/ _` | | / _` | || | ' \/ _| ' \/ -_) '_|
   |_|\___|_||_|_||_|_/__/_.__/\__,_|_|_\__,_|\_,_|_||_\__|_||_\___|_|  
                                                                        """

def main(stdscr):
    stdscr.clear()
    stdscr.addstr(title)
    stdscr.refresh()
    stdscr.getch()

wrapper(main)