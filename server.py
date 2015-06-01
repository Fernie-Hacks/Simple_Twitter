import socket
import sys
from thread import *
 
#User class
class twitterUser:
    def __init__(self, user=None):
        self.name = user
        self.msgs = []
        self.followers = []
    
    def is_follower(self, user):
        return (user in self.followers)
        
    def get_followers(self):
        count = 1
        for i in self.followers:
            followerList = str(i + '\n')
            count = count +1
        return followerList
    
    def add_follower(self, user):
        self.followers.append(str(user))
    
    def remove_follower(self, user):
        self.followers.remove(str(user))
    
    def add_msg(self, msg):
        self.msgs.append(str(msg))
    
    def remove_msg(self, msg):
        self.msgs.remove(str(msg)) 

users = ['TweetGod', 'Anthony', 'Fernando']
passWs = ['easypass', 'ITA', 'cs164']    
TweetGod = twitterUser('TweetGod')
Anthony = twitterUser('Anthony')
Fernando = twitterUser('Fernando')
userList = []
userList.append(TweetGod)
userList.append(Anthony)
userList.append(Fernando)
 
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
def clientthread(conn, myUsers, myPassWs):
    validation = False
    #infinite loop so that function do not terminate and thread do not end.
    while True:
        data = conn.recv(1024)
        if not data: 
            break
        if validation is False:
            credentials = data.split()
            user = credentials[0]
            passW = credentials[1]
            count = 0 
            for i in myUsers:
                if (str(i) == str(user)) and (passW == myPassWs[count]):
                    validation = True
                count = count + 1
            if validation is True:
                conn.sendall('T')
            else:
                conn.sendall('F')
        else:
            option = data.split()
            if str(option[0]) == str('Follow'):
                if str(option[1]) == str(user):
                    conn.sendall('Can not subscribe to yourself')
                if (option[1] not in users):
                    conn.sendall('Invalid username')
                else:
                    userValue = users.index(str(option[2]))
                    exists = False
                    for i in users:
                        if (userList[userValue].is_follower(str(option[1]))):
                            conn.sendall('Already following that user.')
                            break
                        if (str(i) == option[1]) and not(userList[userValue].is_follower(str(option[1]))):
                            userList[userValue].add_follower(option[1])
                            conn.sendall ('You are now subscribe to ' + option[1])
                            exists = True
                            break
                    if exists == False:
                        conn.sendall('User does not exist.')
            if str(option[0]) == 'List':
                userValue = users.index(str(option[1]))
                if not (userList[userValue].followers):
                    conn.sendall('You do not have any subscription')
                    break
                conn.sendall(str(userList[userValue].get_followers()))
            if str(option[0]) == str('Remove'):
                if str(option[1]) == str(user):
                    conn.sendall('Can not unsubscribe yourself')
                else:
                    userValue = users.index(str(option[2]))
                    exists = False
                    for i in users:
                        if (userList[userValue].is_follower(str(option[1]))):
                            userList[userValue].remove_follower(option[1])
                            conn.sendall('Successfully unsubscribed to that user.')
                            break
                    conn.sendall('Invalid username.')
                                
    #came out of loop
    conn.close()
 
#Code to talk to the client
while 1:
    #wait to accept a connection - blocking call
    conn, addr = s.accept()
    print 'Connected with ' + addr[0] + ':' + str(addr[1])
     
    #start new thread takes 1st argument as a function name to be run, second is the tuple of arguments to the function.
    start_new_thread(clientthread ,(conn, users, passWs))
 
s.close()
