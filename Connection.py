import socket
import os
from colorama import init, Fore, Back, Style
from LogoAscii import Logo
import threading

init(autoreset=True)





def TryConnection(address):
  command = f"ping -n 1 {address} > NUL 2>&1 " if os.name == "nt" else f"ping -c 1 {address} > /dev/null 2>&1"
  response = os.system(command)
  return response


def LoopOpenDoors(address,port):
  
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.5)
        try:
          result = sock.connect_ex((address,port))
          if result == 0:
              print(Fore.GREEN + f"port {port} is open\n")
          else:
              print(Fore.RED + f"port {port} is closed\n")
        finally:
          sock.close()


def theand(address,list):
  threads = []
  for port in list:
      thread = threading.Thread(target=LoopOpenDoors, args=(address,port))
      thread.start()
      threads.append(thread)

  for thread in threads:
      thread.join()




def ConnectionError(address):
  print(Fore.RED + f"No connection was found for the following address: {address}")

def ConnectionSucess(address):
  print(Fore.GREEN + f"Connection to {address} successful.")




def Connection(address, list):
  Logo()
  
  if TryConnection(address) == 0:
    ConnectionSucess(address)
    
    theand(address, list)
    
  else:
    ConnectionError(address)
    