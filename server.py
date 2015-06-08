import socket
import sys
from thread import *
 
#User class
class twitterUser:
    def __init__(self, user=None):
        if user is None:
            self.username = {}
        else:
            self.username = user
        self.count = 0
        self.msgs = []
        self.tweets = []
        self.followers = []
        self.hashtags = []
    
    def is_follower(self, name, user):
        return (name in  userList[users.index(str(user))].followers)
        
    def get_followers(self, user):
        count = 1
        followersList = ''
        for i in userList[users.index(str(user))].followers:
            followersList += '\t' + str(i) + '\n'
            count = count +1
        return followersList[:-1]
        
    def get_actual_followers(self, user):
        count = 0
        followers = ''
        for i in userList:
            for j in i.followers:
                if str(j) == str(user):
                    followers += i.username + ' '
                    count = count +1
        if count == 0:
            return 'Nobody is subscribed you'
        else:
            return followers
  
    def get_msg_sender_name(self, user):
        if len(userList[users.index(str(user))].msgs) == 0:
            return '\tYou do not have any offline messages' 
        myListUsers = ''
        for i in userList[users.index(str(user))].msgs:
            msgSplit = i.strip(' ', 1)
            if str(msgSplit[0]) not in myListUsers:
                myListUsers += '\t' + msgSplit[0] + '\n'
        return myListUsers[:-1]
            
    def get_msgs(self, name, user):
        if len(userList[users.index(str(user))].msgs) == 0:
            return '\tYou do not have any offline messages'
        if str(name) == str(user):
            isAllMsgs = True
        combineMsgs = ''
        for i in userList[users.index(str(user))].msgs:
            if isAllMsgs:
                combineMsgs +='\t'+ str(i) +'\n'
            else:
                fromUser = i.strip(' ', 1)
                if str(fromUser[:-1]) == str(name):
                    combineMsgs += '\t' + str(i) + '\n'
        isAllMsgs = False
        userList[users.index(str(user))].msgs[:] = []
        return combineMsgs[:-1]
    
    def get_tweets(self, user):
        print len(userList[users.index(str(user))].tweets)
        if len(userList[users.index(str(user))].tweets) == 0:
            return '\tYou do not have any tweets'
        tweetMsgs = ''
        for i in userList[users.index(str(user))].tweets:
                tweetMsgs +=  '\t' + str(i) + '\n'
        return tweetMsgs[:-1]
    
    def add_follower(self, name, user):
        userList[users.index(str(user))].followers.append(str(name))
    
    def remove_follower(self, name, user):
        userList[users.index(str(user))].followers.remove(str(name))
    
    def add_msg(self, msg, user):
        userList[users.index(str(user))].msgs.append(str(msg))
    
    def remove_msg(self, msg, user):
        userList[users.index(str(user))].msgs.remove(str(msg))
    
    def tweets_count(self):
        return str(self.count)
    
    def hash_search(self, hashtag):
        found = ''
        for i in userList:
            for j in i.tweets:  
                if hashtag in j:
                    found = '\t' + str(j) + '\t'
        if str(found) == '':
            found = '\tHashtag was not found.'  
        return found
                    
        

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
            option = data.split()
            if str(option[0]) == str('Msgs'):
                conn.sendall(userList[user.index(str(option[2]))].get_msgs(option[1], option[2]))
            elif str(option[0]) == str('ListUsers'):
                conn.sendall(userList[user.index(str(option[1]))].get_msg_sender_name(option[1]))
            elif str(option[0]) == str('Follow'):
                if str(option[1]) == str(user):
                    conn.sendall('Can not subscribe to yourself')
                if (option[1] not in users):
                    conn.sendall('Invalid username')
                else:
                    userValue = users.index(str(option[2]))
                    exists = False
                    for i in users:
                        if (userList[userValue].is_follower(option[1], option[2])):
                            conn.sendall('Already subscribed that user.')
                            exists = True
                            break
                        if (str(i) == str(option[1])) and not(userList[userValue].is_follower(option[1], option[2])):
                            userList[userValue].add_follower(option[1], option[2])
                            conn.sendall ('You are now subscribed to ' + option[1])
                            exists = True
                            break
                    if exists == False:
                        conn.sendall('User does not exist.')
            elif str(option[0]) == str('Followers'):
                userValue = users.index(str(option[1]))
                conn.sendall(str(userList[userValue].get_actual_followers(option[1])))
            elif str(option[0]) == str('List'):
                userValue = users.index(str(option[1]))
                if not (userList[userValue].followers):
                    conn.sendall('\tYou do not have any subscriptions')
                    break
                conn.sendall(str(userList[userValue].get_followers(option[1])))
            elif str(option[0]) == str('Remove'):
                if str(option[1]) == str(user):
                    conn.sendall('Can not unsubscribe yourself')
                else:
                    userValue = users.index(str(option[2]))
                    exists = False
                    for i in users:
                        if (userList[userValue].is_follower(option[1], option[2])):
                            userList[userValue].remove_follower(option[1], option[2])
                            conn.sendall('Successfully unsubscribed to that user.')
                            exists = True
                            break
                    if exists == False:
                        conn.sendall('Invalid username.')
            elif str(option[0]) == str('Tweet'):
                option = data.split(' ', 2)
                hashtags = conn.recv(1024)
                userValue = users.index(str(option[1]))
                userList[userValue].count = userList[userValue].count + 1 
                if len(userList[userValue].followers) == 0:
                    break;
                for i in userList[userValue].followers:
                    followerIndex = users.index(str(i))
                    tweet = str(option[1]) + ': ' + str(option[2]) + ' ' + hashtags
                    if online[followerIndex]:
                        userList[followerIndex].tweets.append(tweet)
                        userList[userValue].tweets.append(tweet)
                        singleHash = hashtags.split()
                        for d in singleHash:
                            userList[userValue].hashtags.append(str(d))
                            
                    else:
                        userList[followerIndex].msgs.append(tweet)
                        userList[followerIndex].tweets.append(tweet)
                        userList[userValue].tweets.append(tweet)
                        singleHash = hashtags.split()
                        for d in singleHash:
                            userList[userValue].hashtags.append(str(d))         
            elif str(option[0]) == str('SeeTweets'):
                userValue = user.index(option[1])
                conn.sendall(userList[userValue].get_tweets(option[1]))
            elif str(option[0]) == str('Hashtag'):
                userValue = user.index(option[2])
                conn.sendall(userList[userValue].hash_search(option[1]))
            elif str(option[0]) == str('MsgsCount'):
                userValue = user.index(option[1])
                conn.sendall(userList[userValue].tweets_count())
            elif str(option[0]) == str('UserCount'):
                count = 0
                for i in online:
					if i == True:
						count = count + 1
                conn.sendall(str(count))
            elif str(option[0]) == str('StoredCount'):
				count = 0
				for i in userList:
					count = count + len(i.msgs)
				conn.sendall(str(count))
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
