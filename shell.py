import subprocess
import platform
import socket
import time
import os
import Launcher
import pandas
import serial
import time


def write_read(x):
  arduino.write(bytes(x, 'utf-8'))
  time.sleep(0.05)
  data = arduino.readline()
  return data
def header():
    print('''
  _____                _     _           _ _                        _               
 |_   _|__ _ __  _ __ (_)___| |__   __ _| | | __ _ _   _ _ __   ___| |__   ___ _ __ 
   | |/ _ \ '_ \| '_ \| / __| '_ \ / _` | | |/ _` | | | | '_ \ / __| '_ \ / _ \ '__|
   | |  __/ | | | | | | \__ \ |_) | (_| | | | (_| | |_| | | | | (__| | | |  __/ |   
   |_|\___|_| |_|_| |_|_|___/_.__/ \__,_|_|_|\__,_|\__,_|_| |_|\___|_| |_|\___|_|   
                                                                                      ''')


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
    
    
