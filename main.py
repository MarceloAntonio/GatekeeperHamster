from Connection import Connection
import argparse
import List


if __name__ == "__main__":
  parser = argparse.ArgumentParser(
    prog='example.com',
    description= 'A program for quickly and easily checking for open doors.',
    epilog='Text -h to get help'
  )
  
  parser.add_argument('URL', help='Target IP or URL')
  parser.add_argument('--all','-a',action='store_true', help='Check all ports')
  parser.add_argument('--web','-w',action='store_true', help='Check just web ports')
  parser.add_argument('--network','-n',action='store_true', help='Check just network ports')
  parser.add_argument('--file','-f',action='store_true', help='Check just file ports')
  parser.add_argument('--db','-d',action='store_true', help='Check just database ports')
  parser.add_argument('--ftp','-p',action='store_true', help='Check just ftp ports')
  parser.add_argument('--remote','-r',action='store_true', help='Check just remote ports')
  

  arg = parser.parse_args()
   
  if arg.all:
      Connection(arg.URL, List.allPortsList)

  elif arg.web:
      Connection(arg.URL, List.webList)

  elif arg.network:
      Connection(arg.URL, List.networkList)

  elif arg.file:
      Connection(arg.URL, List.fileList)

  elif arg.db:
      Connection(arg.URL, List.dbList)

  elif arg.ftp:
      Connection(arg.URL, List.ftpList)

  elif arg.remote:
      Connection(arg.URL, List.remoteList)

  else:
      print("No options selected. Use -h to see the options.")
