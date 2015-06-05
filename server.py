import socket
import sys
from thread import *
 
#User class
class twitterUser:
    def __init__(self, user=None):
        self.name = user
        self.msgs = []
        self.tweets = []
        self.followers = []
        self.hashtags = []
    
    def is_follower(self, user):
        return (user in self.followers)
        
    def get_followers(self):
        count = 1
        followersList = ''
        for i in self.followers:
            followersList += '\t' + str(i) + '\n'
            count = count +1
        return followersList[:-1]
  
    def get_msgs_users(self):
        if len(self.msgs) == 0:
            return '\tYou do not have any offline messages' 
        myListUsers = ''
        for i in self.msgs:
            msgSplit = i.strip(' ', 1)
            if str(msgSplit[0]) not in myListUsers:
                myListUsers += '\t' + msgSplit[0] + '\n'
        return myListUsers[:-1]
            
    def get_msgs(self, username):
        if len(self.msgs) == 0:
            return '\tYou do not have any offline messages'
        if str(username) == str(self.name):
            isAllMsgs = True
        combineMsgs = ''
        for i in self.msgs:
            if isAllMsgs:
                combineMsgs +='\t'+ str(i) +'\n'
            else:
                if str(fromUser) == str(username):
                    combineMsgs += '\t' + str(i) + '\n'
        isAllMsgs = False
        self.msgs[:] = []
        return combineMsgs[:-1]
    
    def get_tweets(self):
        tweets = ''
        for i in self.tweets:
                tweets +=  '\t' + str(i[:-1]) + '\n'
        return tweets[:-1]
    
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
online = [False, False, False]
 
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
    isInMenu = False
    global online
    #infinite loop so that function do not terminate and thread do not end.
    while True:
        #if validation:
         #   conn.sendall(str(len(userList[users.index(str(user))].msgs)))
        data = conn.recv(1024)
        if not data: 
            break
        if validation is False:
            credentials = data.split()
            user = credentials[0]
            passW = credentials[1]
            count = 0 
            for i in myUsers:
                if (str(i) == str(user)) and (str(passW) == str(myPassWs[count])):
                    validation = True
                    break
                count = count + 1
            if validation is True:
                conn.sendall('T')
                conn.recv(1024)
                offlineMsgCount = len(userList[users.index(str(user))].msgs)
                conn.sendall(str(offlineMsgCount))
                online[count] = True
            else:
                conn.sendall('F')
        else:
            option = data.split(' ', 2)
            if str(option[0]) == str('Msgs'):
                conn.sendall(userList[user.index(str(option[2]))].get_msgs(option[1]))
            elif str(option[0]) == str('ListUsers'):
                conn.sendall(userList[user.index(str(option[1]))].get_msgs_users())
            elif str(option[0]) == str('Follow'):
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
                            exists = True
                            break
                        if (str(i) == str(option[1])) and not(userList[userValue].is_follower(str(option[1]))):
                            userList[userValue].add_follower(option[1])
                            conn.sendall ('You are now subscribe to ' + option[1])
                            exists = True
                            break
                    if exists == False:
                        conn.sendall('User does not exist.')
            elif str(option[0]) == str('List'):
                userValue = users.index(str(option[1]))
                if not (userList[userValue].followers):
                    conn.sendall('\tYou do not have any subscription')
                    break
                conn.sendall(str(userList[userValue].get_followers()))
            elif str(option[0]) == str('Remove'):
                if str(option[1]) == str(user):
                    conn.sendall('Can not unsubscribe yourself')
                else:
                    userValue = users.index(str(option[2]))
                    exists = False
                    for i in users:
                        if (userList[userValue].is_follower(str(option[1]))):
                            userList[userValue].remove_follower(option[1])
                            conn.sendall('Successfully unsubscribed to that user.')
                            exists = True
                            break
                    if exists == False:
                        conn.sendall('Invalid username.')
            elif str(option[0]) == str('Tweet'):
                hashtags = conn.recv(1024)
                userValue = users.index(str(option[1]))
                #print userValue
                if len(userList[userValue].followers) == 0:
                    break;
                for i in userList[userValue].followers:
                    followerIndex = users.index(str(i))
                    tweet = str(option[1]) + ': ' + str(option[2]) + ' ' + hashtags
                    if online[followerIndex]:
                        userList[followerIndex].tweets.append(tweet)
                        userList[userValue].msgs.append(tweet)
                        singleHash = hashtags.split()
                        for d in singleHash:
                            userList[userValue].hashtags.append(str(d))
                            
                    else:
                        userList[followerIndex].msgs.append(tweet)
                        userList[followerIndex].tweets.append(tweet)
                        userList[userValue].msgs.append(tweet)
                        singleHash = hashtags.split()
                        for d in singleHash:
                            userList[userValue].hashtags.append(str(d))         
            elif str(option[0]) == str('SeeTweets'):
                userValue = user.index(option[1])
                conn.sendall(userList[userValue].get_tweets())
            elif str(option[0]) == str('Hashtag'):
				userValue = user.index(option[1])
            elif str(option[0]) == str('LogOut'):
                userValue = users.index(str(option[1]))
                online[userValue] = False  
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
