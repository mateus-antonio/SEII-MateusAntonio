import socket
import sys                   

if len(sys.argv) != 3:
	print ("Correct usage: file_server Porta nome_do_arquivo_original")
	exit()

port = int(sys.argv[1])          
s = socket.socket()              
host = socket.gethostname()      
print(host)
s.bind((host, port))             
s.listen(5)                      

print('Server listening....') 

while True:
    conn, addr = s.accept()     
    print('Got connection from', addr)

    filename = str(sys.argv[2]) 
    f = open(filename,"rb")
    l = f.read(1024)
    while (l):
       conn.send(l)
       print('Sending ')
       l = f.read(1024)
    f.close()

    print('Done sending')
    conn.close()
    break