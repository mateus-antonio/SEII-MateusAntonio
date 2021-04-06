import socket                   
import sys

if len(sys.argv) != 4:
	print ("Correct usage: file_client IP Porta nome_do_arquivo_destino")
	exit()

s = socket.socket()                 
host = str(sys.argv[1])           
port = int(sys.argv[2])                         

s.connect((host, port))
f = open(str(sys.argv[3]),'wb')

l = s.recv(1024)
while (l):
    print ("Receiving...")
    f.write(l)
    l = s.recv(1024)

f.close()
print('Successfully get the file')
s.close()
print('Connection closed')