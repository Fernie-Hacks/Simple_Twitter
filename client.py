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
    msg = str(username + ' ' + passW)
    s.send(msg)
    reply = s.recv(4096)
    if str(reply) == 'T':
		loggedIn = True
	if loggedIn:
		print 'Twitter Menu'
		print '1) See Offline Messages'
		print '2) Edit Subscriptions'
		print '3) Post a Message'
		print '4) Logout'
		option = raw_input('Enter number corresponding to menu option: ') 
		
    
#~ while 1:
    #~ socket_list = [sys.stdin, s]
     #~ 
    #~ # Get the list sockets which are readable
    #~ read_sockets, write_sockets, error_sockets = select.select(socket_list , [], [])
     #~ 
    #~ for sock in read_sockets:
        #~ #incoming message from remote server
        #~ if sock == s:
            #~ data = sock.recv(4096)
            #~ if not data :
                #~ print 'Connection closed'
                #~ sys.exit()
            #~ else :
                #~ #print data
                #~ sys.stdout.write(data)
         #~ 
        #~ #user entered a message
        #~ else :
            #~ #while(loggedIn):
                #~ #print 'Twitter Menu'
                #~ #print '1) See Offline Messages'
                #~ #print '2) Edit Subscriptions'
                #~ #print '3) Post a Message'
                #~ #print '4) Logout'
                #~ #option = raw_input('Enter number corresponding to menu option: ') 
    #~ 
            #~ msg = str(username + ' ' + passW)
            #~ s.send(msg)
