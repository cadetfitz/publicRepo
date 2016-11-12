__author__ = 'fitzgd2'

import time
from socket import *
import sys
import base64
import random


ipAddress = str(sys.argv[1])
port = int(str(sys.argv[2]))
print "IP Address: %s"%(ipAddress)
print "Port: %d" %(port)
print " "

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


def morseEncoder(msg):
	result = []
	i = 0
	for char in msg:
		result.append(CODE[char.upper()])
		i += 1
	return result

def encodeSend(msg, clientSocket, addr):
	for char in msg:
		for i in char:
			if i == '.':
				sendShort(clientSocket, addr)
				print "short"
			elif i == '-':
				sendLong(clientSocket, addr)
				print "long"
			else:
				print "error"
			time.sleep(0.5)
		time.sleep(1)
		print "\n"

def sendShort(clientSocket, addr):
	message = base64.b64encode(bytes(sendMe()))
	x = 0
	while x < 3:
		clientSocket.sendto(message, addr)
		x += 1

def sendLong(clientSocket, addr):
	message = base64.b64encode(bytes(sendMe()))
	x = 0
	while x < 6:
		clientSocket.sendto(message, addr)
		x += 1

def sendMe():
	rand = random.randint(0,3)
	if rand == 0:
		return "nottheflag"
	elif rand == 1:
		return "nottheflag"
	elif rand == 2:
		return "nottheflag"
	else:
		return "nottheflag"

def main():  # Main
	# Connect to socket
	clientSocket = socket(AF_INET, SOCK_DGRAM)
	clientSocket.settimeout(1) #wait up to one second to receive reply
	message = 'FLAG(H4CK7H3PL4N37)'    #message sent
	eof = 'EOF'
	addr = (ipAddress, port) #loopback address on port 12000

	encoded = morseEncoder(message)
	print encoded
	
	start = time.clock() # get start time, use time.clock for precision
	encodeSend(encoded, clientSocket, addr)

	#print 'Packet number: %d' % (pings)
	
	#print "Start time: %f" % (start)
	clientSocket.sendto(eof, addr)  #send ping
	time.sleep(4)
	clientSocket.sendto(eof, addr)  #send ping
	try:
		data, server = clientSocket.recvfrom(1024)  #get reply
		end = time.clock()   #get end time
		#print "End time: %f" % (end)
		elapsed = (end - start) *1000    #get time elapsed in milliseconds
		#print 'Data sent: %s' % (data)
		#print 'Packet number: %d' % (pings)
		#print 'Time elapsed: %f' % (elapsed) # as float for precision
		print 'PING to <%s> : <%f>' % (ipAddress, elapsed) #Prints Ping <ipAddress> <sequence number> <elapsed time>
	except timeout: #get timeout and print
		print 'PING to <%s> LOST' % (ipAddress)
	#time.sleep(1) #sleep for one second, waits one second in between pings

	sys.exit()

if __name__ == "__main__":
	main()
