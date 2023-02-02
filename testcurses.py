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
------------------------------------------------------------------------"""
global i 

arduino = serial.Serial(port='COM3',baudrate=115200,timeout=1)
path = 'C:/'
host_name = socket.gethostname()
host_ip = socket.gethostbyname(host_name)


def write_read(x):
  arduino.write(bytes(x, 'utf-8'))
  time.sleep(0.05)
  data = arduino.readline()
  return data


def main(stdscr):
    


    ##################HEADER####################
    date = datetime.now().ctime()
    stdscr.refresh()
    curses.init_pair(1, curses.COLOR_MAGENTA, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_CYAN, curses.COLOR_BLACK)
    header = curses.newwin(10, 100, 0, 0)
    header.clear()
    
    header.addstr(title, curses.color_pair(1)) 
    header.addstr(5,0, cursur, curses.color_pair(2))
    header.addstr(6,23, date, curses.color_pair(1))
    header.refresh()
    stdscr.addstr(10,1,">>>")
    stdscr.refresh()
   ####################INPUT####################
    text =""
    program = 1 
    k = 1
    while True:
      
      inputwin = curses.newwin(1,15,9+k,5)
      stdscr.addstr(9+k,1,">>>", curses.color_pair(1))
      box = Textbox(inputwin)
      stdscr.refresh()
      box.edit()
      text = box.gather()
      
      if text == 'quit':
        curses.endwin()
      
      data = write_read(text).decode("utf-8")
      inputwin.clear()
      inputwin.addstr(data, curses.color_pair(2))
      inputwin.refresh()
        
      k = k + 1
    

wrapper(main)