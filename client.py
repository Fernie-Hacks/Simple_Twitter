import socket   #for sockets
import sys  #for exit
import getpass

# A dictionary structure with usernames and passwords
users = ['TweetGod', 'Anthony', 'Fernando']
passWs = ['easypass', 'ITA', 'cs164']
validation = False
loggedIn = False

#~ print 'M.......MMMMMMMMMMMMMMMMMMMMMMMMMMMMMM8............,MMMMM.......MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM'
#~ print '..~+++...MMMMMMMMMMMMMMMMMMMMMMMMMMMMM..++++..++++..:MMM...+++:..MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM'
#~ print '..+++++.......:MMMMMMMMMMMMMMMMMMMMMM8..++++:.++++=..MMM..+++++..MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM'
#~ print '..+++++...............MMM.....?MM=.......++,..++++=..ZZZ..+++++..OZZMMMMO........,NMMMMD.. ......~MM'
#~ print '..++++++++++++++..++...7..=++......++=:.....:.++++=.......+++++.......,...,++++=....8$...,++++++...M'
#~ print '..++++++++++++++.++++....=++++....++++:.++++..+++++++++++.+++++++++++...+++++++++++....++++++++++..N'
#~ print '..+++++.......,..++++....=++++....++++:.++++:.+++++++++++.+++++++++++=.+++++...+++++..++++++++++~..M'
#~ print '..+++++..........++++....=++++....++++:.++++~.++++++++++..=+++++++++~.~+++++++++++++:+++++........MM'
#~ print '..+++++.... .....++++....+++++....++++,.++++~.+++++.......,++++.......=+++++++++++++.++++=..MMMMMMMM'
#~ print '..~++++++++++++..++++++:+++++++==+++++..++++~..+++++++++...+++++++++:..++++=....,=+,.++++=..MMMMMMMM'
#~ print 'M..:++++++++++++..+++++++++++++++++++...++++~..:+++++++++...?++++++++=..+++++++++++=.++++=..MMMMMMMM'
#~ print 'MM...++++++++++~....+++++++.~++++++:....++++.....++++++++....~+++++++....:++++++++...,+++...MMMMMMMM'
#~ print 'MMMN.............M,..................M8......~M$..........$M...........M...........:.......MMMMMMMMM'
#~ print 'MMMMMMM8?+++++ZMMMMMMN7+ZMMMMMD+?DMMMMMMM7?MMMMMMMMO+++IMMMMMMMN7+++NMMMMMMN7+IDMMMMMM8+8MMMMMMMMMMM'

while(1):
    print 'Please provide your log in credentials'
    username = raw_input('Username: ')
    passW = getpass.getpass('Password: ') 
    count = 0;
    for i in users:
        if (str(i) == str(username)) and (str(passWs[count]) == str(passW)):
            validation = True
            break
        count = count + 1
    if validation is True:
		loggedIn = True
        break
    else:
        print 'Invalid credentials, try again...'
          
# create dgram udp socket
try:
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
except socket.error:
    print 'Failed to create socket'
    sys.exit()
 
host = 'localhost';
port = 8888;
 
while(loggedIn):
	print 'Twitter Menu'
	print '1) See Offline Messages'
	print '2) Edit Subscriptions'
	print '3) Post a Message'
	print '4) Logout'
	option = raw_input('Enter number corresponding to menu option: ')
	 
 
while(1) :
    msg = raw_input('Enter message to send : ')
     
    try :
        #Set the whole string
        s.sendto(msg, (host, port))
         
        # receive data from client (data, addr)
        d = s.recvfrom(1024)
        reply = d[0]
        addr = d[1]
         
        print 'Server reply : ' + reply
     
    except socket.error, msg:
        print 'Error Code : ' + str(msg[0]) + ' Message ' + msg[1]
        sys.exit()
