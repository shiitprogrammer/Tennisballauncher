import sys

import subprocess
import platform
import socket
import time
import os
import Launcher
import pandas
import serial
import time
from datetime import datetime
from rich.console import Console
from rich.layout import Layout
from rich import print 
import pyfiglet



os.system('cls')
console = Console()
def layout():
  layout = Layout()
  layout.split_column(
      Layout(name="header"),
      Layout(name="body")
  )
  layout["body"].split_row(
      Layout(name="input"),
      Layout(name="rpm"),
  )
  layout["header"].update(header())
  layout["input"].size = 10
  print(layout)

def write_read(x):
  arduino.write(bytes(x, 'utf-8'))
  time.sleep(0.05)
  data = arduino.readline()
  return data
def header():

    title = pyfiglet.figlet_format("Tennisballauncher", font = "small")                                                                                                                                 
    console.print(title,style="red")
    console.rule(f"[bold red] {datetime.now().ctime()}")

header()
arduino = serial.Serial(port='COM3',baudrate=115200,timeout=1)
path = 'C:/'
host_name = socket.gethostname()
host_ip = socket.gethostbyname(host_name)
program = 1

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
      print(rpmdata.decode("utf-8"))
    
    
