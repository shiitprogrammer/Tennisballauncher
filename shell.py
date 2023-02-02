import sys

import subprocess
import platform
import socket
import time
import os
import Launcher
import serial
import time
from datetime import datetime
from rich.console import Console, Group
from rich import print 


os.system('cls')
console = Console()

def write_read(x):
  arduino.write(bytes(x, 'utf-8'))
  time.sleep(0.05)
  data = arduino.readline()
  return data




def header():

    title = """
  _____              _    _          _ _                   _            
 |_   _|__ _ _  _ _ (_)__| |__  __ _| | |__ _ _  _ _ _  __| |_  ___ _ _ 
   | |/ -_) ' \| ' \| (_-< '_ \/ _` | | / _` | || | ' \/ _| ' \/ -_) '_|
   |_|\___|_||_|_||_|_/__/_.__/\__,_|_|_\__,_|\_,_|_||_\__|_||_\___|_|  
                                                                        """
                                                                                                                              
    console.print(title,style="magenta")
    console.rule(f"[bold magenta] {datetime.now().ctime()}")


arduino = serial.Serial(port='COM3',baudrate=115200,timeout=1)
path = 'C:/'
host_name = socket.gethostname()
host_ip = socket.gethostbyname(host_name)

header()
program = 1
while program == 1:
  txt = input(">>>")
  x = txt.split()

  if x[0] == 'start':
      v = Launcher.start_program(distance,angle)
      print(v)
  if x[0] == 'quit':
        
        program = 0 
  if x[0] == 'distance' or x == 'd':
        distance = x[1]
  if x[0] == 'angle' or x == 'a':
        angle = x[1]
  if x[0] == 'rpm':
        
        rpmdata = (write_read(x[1]))
          
        received = rpmdata.decode("utf-8")
        
        print(received)
    
      
      
          

      
      
          
    
