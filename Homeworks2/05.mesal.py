#barname ie benvisid ke ip ra az karbar gerefte va valid boodanash ra etela dahad 

import socket


addr = '127.0.0.253'

try:
    socket.inet_aton(addr)
    print('Valid ip')
    
except socket.error:
    print('invalid ip')    
    