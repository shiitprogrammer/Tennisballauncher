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
from rich import box
from rich.align import Align
from rich.console import Console, Group
from rich.layout import Layout
from rich.panel import Panel
from rich.progress import BarColumn, Progress, SpinnerColumn, TextColumn
from rich.syntax import Syntax
from rich.table import Table
from rich.live import Live 
from rich import print 
import pyfiglet
from tkinter import *


os.system('cls')
console = Console()

def window():
  def Close():
      window.destroy()
      shell = 0
  window = Tk()
  window.title("Rpmcounter")

  window.geometry('350x200')
  shell = 1 
  while shell == 1:
    arduino.write(bytes("conversation", 'utf-8'))
    rpm = arduino.readline().decode("utf-8")
    time.sleep(0.1)
    lbl = Label(window, text=rpm)
    lbl.grid(column=0, row=0)
    btn = Button(window, text="Exit", command=Close)

    btn.grid(column=1, row=0)

    window.update()   
  return shell
def layout():
  title = pyfiglet.figlet_format("Tennisballauncher", font = "small")    
  layout = Layout()
  layout.split_column(
      Layout(name="header"),
      Layout(name="body")
  )
  layout["body"].split_row(
      Layout(name="input"),
      Layout(name="rpm"),
  )
  layout["header"].update(title)
  
  with Live(layout, refresh_per_second=10, screen=True):
    layout['input'].update(codes(input("<<<")))
    layout["input"].size = 20
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


arduino = serial.Serial(port='COM3',baudrate=115200,timeout=1)
path = 'C:/'
host_name = socket.gethostname()
host_ip = socket.gethostbyname(host_name)

header()
program = 1
while program == 1:
  x = input(">>>")
  if x == 'start':
      v = Launcher.start_program(distance,angle)
      print(v)
  if x == 'quit':
        program = 0
  if x == 'distance' or x == 'd':
        distance = input("Distance:")
  if x == 'angle' or x == 'a':
        angle = input("Angle:")
  if x == 'rpm':
        received1 = write_read("setrpm")
        print(received1.decode("utf-8"))
        rpmdata = (write_read(input("Rpm?")))
        received2 = rpmdata.decode("utf-8")
        print(received2)
  if x == 't':
      window()
      
          

      
      
          
    
