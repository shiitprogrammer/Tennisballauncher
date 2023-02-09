import curses 
import time
from datetime import datetime
from curses.textpad import Textbox, rectangle
from curses import wrapper
import sys

import subprocess
import platform
import socket
import time
import os
import Launcher
import serial


title = """
  _____              _    _          _ _                   _            
 |_   _|__ _ _  _ _ (_)__| |__  __ _| | |__ _ _  _ _ _  __| |_  ___ _ _ 
   | |/ -_) ' \| ' \| (_-< '_ \/ _` | | / _` | || | ' \/ _| ' \/ -_) '_|
   |_|\___|_||_|_||_|_/__/_.__/\__,_|_|_\__,_|\_,_|_||_\__|_||_\___|_|  
                                                                        """
cursur = """
-----------------------------------------------------------------------------------------------------------------------"""
global i 


def main(stdscr):
    
    

    ##################HEADER####################
    date = datetime.now().ctime()
    stdscr.refresh()
    curses.init_pair(1, curses.COLOR_MAGENTA, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_CYAN, curses.COLOR_BLACK)
    header = curses.newwin(10, 120, 0, 0)
    header.clear()
    
    header.addstr(title, curses.color_pair(1)) 
    header.addstr(6,0, cursur, curses.color_pair(2))
    header.addstr(6,45, date, curses.color_pair(1))
    header.addstr(6,2, "Shiitprogrammer", curses.color_pair(1))
    header.addstr(6,103, "7IW", curses.color_pair(1))
    header.refresh()
    stdscr.addstr(10,1,">>>")
    stdscr.refresh()
   ####################INPUT####################
    bottom = curses.newwin(1, 20, 29, 0)
    k = 1
    type = ""
    while True: 
      bottom.clear()
      bottom.addstr("[Idle]")
      bottom.refresh()
      key = stdscr.getkey()
      if k > 18:
         inputwin.clear()
         inputwin.refresh()
         k = 1
      if key == 'q':
         break
      if key == 'd':
         bottom.clear()
         bottom.addstr("[Var Input]")
         bottom.refresh()
         inputwin = curses.newwin(1,15,9+k,12)
         
         stdscr.addstr(9+k,1,"Distance>>>", curses.color_pair(1))
         box = Textbox(inputwin)
         stdscr.refresh()
         box.edit()
         distance = box.gather().strip()

         inputwin.clear()
         stdscr.addstr(10,45,("Distance is:"), curses.color_pair(2))
         stdscr.addstr(10,58, distance, curses.color_pair(2))
         stdscr.refresh()
         inputwin.refresh()
      if key == 'a':
         bottom.clear()
         bottom.addstr("[Var Input]")
         bottom.refresh()
         inputwin = curses.newwin(1,15,9+k,12)
         
         stdscr.addstr(9+k,1,"Angle>>>", curses.color_pair(1))
         box = Textbox(inputwin)
         stdscr.refresh()
         box.edit()
         angle = box.gather().strip()

         inputwin.clear()
         stdscr.addstr(11,45,("Angle is:"), curses.color_pair(2))
         stdscr.addstr(11,58, angle, curses.color_pair(2))
         stdscr.refresh()
         inputwin.refresh()
      if key == 's':
       bottom.clear()
       bottom.addstr("[Calculating]")  
       bottom.refresh()
       rpm = int(Launcher.start_program(distance,angle))
       displayrpm = str(rpm)
       stdscr.addstr(12,45,("Rpm required:"), curses.color_pair(2))
       stdscr.addstr(12,58, displayrpm, curses.color_pair(2))
       stdscr.refresh()
      else:
        bottom.clear()
        bottom.addstr("[Text Input]")
        bottom.refresh()
        text = ""
        inputwin = curses.newwin(1,15,9+k,4)
        stdscr.addstr(9+k,1,">>>", curses.color_pair(1))
        stdscr.refresh()
        box = Textbox(inputwin)
        stdscr.refresh()
        box.edit()
        text = box.gather().strip()

        inputwin.clear()
        inputwin.addstr((text), curses.color_pair(2))
        inputwin.refresh()
          
        k = k + 1
    


wrapper(main)