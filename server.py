import socket
import sys
from thread import *
 
HOST = ''   # Symbolic name meaning all available interfaces
PORT = 8888 # Arbitrary non-privileged port
 
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#Bind socket to local host and port
try:
    s.bind((HOST, PORT))
except socket.error , msg:
    print 'Bind failed. Error Code : ' + str(msg[0]) + ' Message ' + msg[1]
    sys.exit()
     
#Start listening on socket
s.listen(10)

#Function for handling connections, to create threads
def clientthread(conn):
    users = ['TweetGod', 'Anthony', 'Fernando']
    passWs = ['easypass', 'ITA', 'cs164']
    validation = False
    #infinite loop so that function do not terminate and thread do not end.
    while True:
        if validation is False:
            data = conn.recv(1024)
            if not data: 
                break
            credentials = data.split()
            user = credentials[0]
            passW = credentials[1]
            count = 0 
            for i in users:
                if (str(i) == str(user)) and (passW == passWs[count]):
                    validation = True
                count = count + 1
            if validation is True:
                conn.sendall('T')
            else:
                conn.sendall('F')
        else:
			
			conn.sendall(reply)
    #came out of loop
    conn.close()
 
#Code to talk to the client
while 1:
    #wait to accept a connection - blocking call
    conn, addr = s.accept()
    print 'Connected with ' + addr[0] + ':' + str(addr[1])
     
    #start new thread takes 1st argument as a function name to be run, second is the tuple of arguments to the function.
    start_new_thread(clientthread ,(conn,))
 
s.close()
