import socket   #for sockets
import sys  #for exit
import getpass
import select
import string
        
host = 'localhost';
port = 8888;

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.settimeout(2)
 
# connect to remote host
try :
    s.connect((host, port))
except :
    print 'Unable to connect'
    sys.exit()

loggedIn = False

print 'M.......MMMMMMMMMMMMMMMMMMMMMMMMMMMMMM8............,MMMMM.......MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM'
print '..~+++...MMMMMMMMMMMMMMMMMMMMMMMMMMMMM..++++..++++..:MMM...+++:..MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM'
print '..+++++.......:MMMMMMMMMMMMMMMMMMMMMM8..++++:.++++=..MMM..+++++..MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM'
print '..+++++...............MMM.....?MM=.......++,..++++=..ZZZ..+++++..OZZMMMMO........,NMMMMD.. ......~MM'
print '..++++++++++++++..++...7..=++......++=:.....:.++++=.......+++++.......,...,++++=....8$...,++++++...M'
print '..++++++++++++++.++++....=++++....++++:.++++..+++++++++++.+++++++++++...+++++++++++....++++++++++..N'
print '..+++++.......,..++++....=++++....++++:.++++:.+++++++++++.+++++++++++=.+++++...+++++..++++++++++~..M'
print '..+++++..........++++....=++++....++++:.++++~.++++++++++..=+++++++++~.~+++++++++++++:+++++........MM'
print '..+++++.... .....++++....+++++....++++,.++++~.+++++.......,++++.......=+++++++++++++.++++=..MMMMMMMM'
print '..~++++++++++++..++++++:+++++++==+++++..++++~..+++++++++...+++++++++:..++++=....,=+,.++++=..MMMMMMMM'
print 'M..:++++++++++++..+++++++++++++++++++...++++~..:+++++++++...?++++++++=..+++++++++++=.++++=..MMMMMMMM'
print 'MM...++++++++++~....+++++++.~++++++:....++++.....++++++++....~+++++++....:++++++++...,+++...MMMMMMMM'
print 'MMMN.............M,..................M8......~M$..........$M...........M...........:.......MMMMMMMMM'
print 'MMMMMMM8?+++++ZMMMMMMN7+ZMMMMMD+?DMMMMMMM7?MMMMMMMMO+++IMMMMMMMN7+++NMMMMMMN7+IDMMMMMM8+8MMMMMMMMMMM'

while(1): 
    if not loggedIn:
        print 'Please provide your log in credentials'
        username = raw_input('Username: ')
        passW = getpass.getpass('Password: ') 
        msg = str(username + ' ' + passW)
        s.send(msg)
        reply = s.recv(4096)
        if str(reply) == 'T':
            s.send('Trash')
            loggedIn = True
            print '\tWelcome ', username 
            msgCount = s.recv(4096)
            print '\tYou have ' + msgCount + ' new messages.'
        else:
            print '\tInvalid credentials, please try again...'
    
    if loggedIn:
        print 'Twitter Menu'
        print '1) See Offline Messages'
        print '2) Edit Subscriptions'
        print '3) Post a Message'
        print '4) See Tweets'
        print '5) Hashtag Search'
        print '6) Logout'
        option = raw_input('Enter number corresponding to option: ')
        if str(option) == '1':
            while(1):
                print '1) View all messages'
                print '2) View messages from a particular user'
                msgOption = raw_input('Select an option: ')
                if str(msgOption) == '1':
                    s.send('Msgs ' + str(username) + ' ' + str(username))
                    allOfflineMsgs = s.recv(4096)
                    print str(allOfflineMsgs)
                    break
                    #if str(allOfflineMsgs) == '\tYou do not have any offline messages':
                    #    break;
                elif str(msgOption) == '2':
                    s.send('ListUsers ' + str(username))
                    msgsList = s.recv(4096)
                    print str(msgsList)
                    if str(msgsList) == '\tYou do not have any offline messages':
                        break;
                    msgsFromUser = raw_input('Messages from what user? ')
                    msgsByUser = msgsList.strip()
                    if str(msgsByUser) in msgsList:
                        s.send('Msgs ') + str(msgsFromUser) + username
                        offlineMsgs = s.recv(4096)
                        print str(offlineMsgs)
                    else:
                         'Invalid username'
                else:
                    print 'Invalid option, please try again.' 
        elif str(option) == '2':
            while(1):    
                print '1) Subscribe to users'   
                print '2) Delete subscription'
                print '3) Show Followers'
                subOption = raw_input('Select an option: ')
                if str(subOption) == '1':
                    followUser = raw_input('Enter user to subscribe to: ')
                    s.send('Follow ' + str(followUser) + ' ' + str(username))
                    followers = s.recv(4096)
                    print '\t' + followers
                    break
                elif str(subOption) == '2': 
                    s.send('List ' + str(username))
                    users = s.recv(4096)
                    print users
                    if str(users) == '\tYou do not have any subscriptions':
                        break
                    unfollow = raw_input('Enter user to unsubscribe: ')
                    s.send('Remove ' + unfollow + ' ' + username)
                    unfollow = s.recv(4096)
                    print '\t' + unfollow
                    break
                elif str(subOption) == '3':
                    s.send('Followers ' + str(username))
                    followers = s.recv(4096)
                    print '\t' + followers
                    break
                else:
                    print '\tInvalid option, try again'
        elif str(option) == '3':
            hasCorrectLength = False
            while not(hasCorrectLength):
                print 'Message + Hashtags should be no more than 140 characters'
                tweet = []
                tweet.append(raw_input ('Enter a Message or 1 to cancel: '))
                if str(tweet[0]) == '1':
                    break;
                print 'Current Message Count: ', len(tweet[0])
                tweet.append(raw_input ('Enter Hashtags: '))
                if (len(tweet[0]) + len(tweet[1])) + 1 <= 140:
                    hasCorrectLength = True;
            if hasCorrectLength:
                s.send('Tweet ' + username + ' ' + str(tweet[0]))
                s.send(str(tweet[1]))
            print '\tTweet has been posted.'
        elif str(option) == '4':
            print 'Option 4'
            s.send('SeeTweets ' + username)
            tweets = s.recv(4096)
            print tweets
        elif str(option) == '5':
            search = raw_input('Enter the Hashtag you want to search: ')
            s.send('Hashtag ' + search + ' ' + username)
            findings = s.recv(4096)
            print findings
        elif str(option) == '6':
            loggedIn = False
            s.send('LogOut ' + username)
            break
        elif str(option) == 'messagecount' and str(username) == 'TweetGod':
            s.send('MsgsCount ' + username)
            count = s.recv(4096)
            print '\tThe number of tweets so far are ', count
        elif str(option) == 'usercount' and str(username) == 'TweetGod':
            s.send('UserCount ' + username)
            count = s.recv(4096)
        elif str(option) == 'storedcount' and str(username) == 'TweetGod':
            s.send('StoredCount ' + username)
            count = s.recv(4096)
            print '\tThe current number of unread messages are ', count
        else:
            print '\tInvalid option, try again...'
             
print 'Session has ended'     
