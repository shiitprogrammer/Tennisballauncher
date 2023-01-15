import subprocess
import platform
import socket
import time
import os
import Launcher
import pandas
def header():
    print('''
  _____                _     _           _ _                        _               
 |_   _|__ _ __  _ __ (_)___| |__   __ _| | | __ _ _   _ _ __   ___| |__   ___ _ __ 
   | |/ _ \ '_ \| '_ \| / __| '_ \ / _` | | |/ _` | | | | '_ \ / __| '_ \ / _ \ '__|
   | |  __/ | | | | | | \__ \ |_) | (_| | | | (_| | |_| | | | | (__| | | |  __/ |   
   |_|\___|_| |_|_| |_|_|___/_.__/ \__,_|_|_|\__,_|\__,_|_| |_|\___|_| |_|\___|_|   
                                                                                      ''')
def rpmcounter():
  print("rpm")
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
    if code == 'distance':
      distance = input("Distance:")
    if code == 'angle':
      angle = input("Angle:")
    if code == 'quit':
      program = 0
    
