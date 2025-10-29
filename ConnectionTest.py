import socket
import os

PORTS = [20, 21, 22, 23, 25, 53, 67, 68, 69, 80, 110, 123, 135, 137, 138, 139, 143, 161, 162, 179, 389, 443, 445, 465, 500, 514, 587, 636, 873, 989, 990, 1433, 1521, 2049, 2181, 3128, 3306, 3389, 4500, 5000, 5432, 5900, 6379, 7001, 8080, 8081, 8443, 9200, 9300, 27017]

def TryConnection(address):
  command = f"ping -n 1 {address} > NUL 2>&1"
  response = os.system(command)
  return response

def StartSocket():
  sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  return sock

def LoopOpenDoors(sock,address):
  for i in range(len(PORTS)):
        result = sock.connect_ex((address,PORTS[i]))
        if result == 0:
          print(f"port {PORTS[i]} is open\n")
        else:
          print(f"port {PORTS[i]} is closed\n")
        i+1


def ConnectionError(address):
  print(f"No connection was found for the following address: {address}")

def ConnectionSucess(address):
  print(f"Connection to {address} successful.")






def Connection(address):
  
  
  if TryConnection(address) == 0:
    ConnectionSucess(address)
    
    LoopOpenDoors(StartSocket,address)
    StartSocket.close()
    
  else:
    ConnectionError(address)