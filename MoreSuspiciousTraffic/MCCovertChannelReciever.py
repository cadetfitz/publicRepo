import random
from socket import *
import time
import base64



CODE = {'A': '.-',     'B': '-...',   'C': '-.-.',
        'D': '-..',    'E': '.',      'F': '..-.',
        'G': '--.',    'H': '....',   'I': '..',
        'J': '.---',   'K': '-.-',    'L': '.-..',
        'M': '--',     'N': '-.',     'O': '---',
        'P': '.--.',   'Q': '--.-',   'R': '.-.',
     	'S': '...',    'T': '-',      'U': '..-',
        'V': '...-',   'W': '.--',    'X': '-..-',
        'Y': '-.--',   'Z': '--..',   ':': '---...',
		'(': '-.--.',  ')': '-.--.-', '0': '-----',
		'1': '.----',  '2': '..---',  '3': '...--',
		'4': '....-',  '5': '.....',  '6': '-....',
		'7': '--...',  '8': '---..',  '9': '----.'
        }

inverseCODE = dict((v,k) for (k,v) in CODE.items())

serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(('', 23284))
start = time.time()
tp = 0
x = 1
y = 1
a = 0
b = 0
decode = ""
char = ''
while True:
    #rand = random.randint(0, 10)
    #message, address = serverSocket.recvfrom(1024)
    t = time.time() - start    
    #message = message.upper()
    #print message
    #print t
    
    if (t-tp)<0.1:
	x += 1
	tp = t
    elif (t - tp)<0.6:
	if x == 6:
	    char += '-'
	    #print "long"
	elif x == 3:
	    char += '.'
	    #print "short"
	x = 1
	tp = t
	#print "\n"
    elif (t-tp)<3.5:
	print "Recieving Message..."
	if x == 6:
	    char += '-'
            #print "long"
        elif x == 3:
	    char += '.'
            #print "short"
        x = 1
        tp = t
	#print char
	if char != '':
	    #print inverseCODE[char]
	    decode = decode + inverseCODE[char]
	    #print "Decoded message: " + decode + '\n'
	char = ''
	#print "BREAK\n"
    else:
	print "Decoded message: " + decode + '\n'
	x = 1
	tp = t
	print "----------"
	char = ''
	decode = ""
	
    message, address = serverSocket.recvfrom(1024)
    

    ack = base64.b64encode(bytes("ACK"))
    serverSocket.sendto(ack, address)


#    if rand >= 4:
#        serverSocket.sendto(message, address)

