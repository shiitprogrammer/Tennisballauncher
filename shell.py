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
    
    title = pyfiglet.figlet_format('Tennisballauncher', font='weird')
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
    
    
