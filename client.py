import socket   #for sockets
import sys  #for exit

userList = []
userList.append([])
userList.append([])
userList.append([])

# Populate users, adding three users
userList[0].append('TweetGod')
userList[0].append('easypass')
userList[1].append('Anthony')
userList[1].append('ITA')
userList[2].append('Fernando')
userList[2].append('cs164')

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

print 'Please provide your log in credentials'
username = raw_input('Username: ')
password = raw_input('Password: ') 

for i in xrange(len(grid[i]))
	if 
 
# create dgram udp socket
try:
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
except socket.error:
    print 'Failed to create socket'
    sys.exit()
 
host = 'localhost';
port = 8888;
 
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
