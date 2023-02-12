import serial
import socket
import time
from serial.tools import list_ports



#path = 'C:/'
#host_name = socket.gethostname()
#host_ip = socket.gethostbyname(host_name)
        


def receive_serial(arduino):
        
        received = arduino.readline().decode("utf-8")
        print(received)
        return(received)


        
        
     

    
    
    
    
