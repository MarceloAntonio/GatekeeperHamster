import argparse
import socket
import os


def Conection(URL):
  command = f"ping -n 1 {URL} > NUL 2>&1"
  response = os.system(command)
  
  if response == 0:
    print("Conectado com sucesso")
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    PORTS = [20, 21, 22, 23, 25, 53, 67, 68, 69, 80, 110, 123, 135, 137, 138, 139, 143, 161, 162, 179, 389, 443, 445, 465, 500, 514, 587, 636, 873, 989, 990, 1433, 1521, 2049, 2181, 3128, 3306, 3389, 4500, 5000, 5432, 5900, 6379, 7001, 8080, 8081, 8443, 9200, 9300, 27017]
    for i in range(len(PORTS)):
        result = sock.connect_ex((URL,PORTS[i]))
        if result == 0:
          print(f"port {PORTS[i]} is open\n")
        else:
          print(f"port {PORTS[i]} is closed\n")
        i+1
    sock.close()
  else:
    print("Erro de conexão")


def Run():
  parser = argparse.ArgumentParser(
    prog='1.1.1.1',
    description= 'A test Program with argparse',
    epilog='Text -h to get help'
  )
  
  parser.add_argument('URL', help='URL ')
  parser.add_argument('--ALL','-a',action='store_true', help='Your name')
 

  arg = parser.parse_args()
  
  if(arg.ALL):
   Conection(arg.URL)
    
  
Run()

