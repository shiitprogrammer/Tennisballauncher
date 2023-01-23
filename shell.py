import subprocess
import platform
import socket
import time
import os
import Launcher
import pandas
import serial
import time
from rich.console import Console
from rich import print 
import pyfiglet
console = Console()

def write_read(x):
  arduino.write(bytes(x, 'utf-8'))
  time.sleep(0.05)
  data = arduino.readline()
  return data
def header():
    
    title = '''88888888888                         d8b          888               888 888                                     888                       
                  888                             Y8P          888               888 888                                     888                       
                  888                                          888               888 888                                     888                       
                  888   .d88b.  88888b.  88888b.  888 .d8888b  88888b.   8888b.  888 888  8888b.  888  888 88888b.   .d8888b 88888b.   .d88b.  888d888 
                  888  d8P  Y8b 888 "88b 888 "88b 888 88K      888 "88b     "88b 888 888     "88b 888  888 888 "88b d88P"    888 "88b d8P  Y8b 888P"   
                  888  88888888 888  888 888  888 888 "Y8888b. 888  888 .d888888 888 888 .d888888 888  888 888  888 888      888  888 88888888 888     
                  888  Y8b.     888  888 888  888 888      X88 888 d88P 888  888 888 888 888  888 Y88b 888 888  888 Y88b.    888  888 Y8b.     888     
                  888   "Y8888  888  888 888  888 888  88888P' 88888P"  "Y888888 888 888 "Y888888  "Y88888 888  888  "Y8888P 888  888  "Y8888  888     '''
    
                                                                                                                                         
    console.print(title,style="red")


arduino = serial.Serial(port='COM3',baudrate=115200,timeout=1)
path = 'C:/'
host_name = socket.gethostname()
host_ip = socket.gethostbyname(host_name)
header()
program = 1

#if __name__ == '__main__':
while program == 1:
    code = input(">>> ")
    if code == 'start':
      v = Launcher.start_program(distance,angle)
      print(v)
    if code == 'quit':
      program = 0
    if code == 'distance' or code == 'd':
      distance = input("Distance:")
    if code == 'angle' or code == 'a':
      angle = input("Angle:")
    if code == 'rpm':
      rpmdata = (write_read(input('Rpm:')))
      print(rpmdata)
    
    
