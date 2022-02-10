import socket 

s = socket.socket()
print("socket successfully created")

port = 12345 
s.bind(('', port))
print('socket binded to %s' %(port))

s.listen(5)
print ("socket is listening")

while True:

  c, addr = s.accept()
  print('Got connection from ', addr)

  c.send('Thank your for connecting'.encode())

  c.close()
  break


# ref link 
  # https://yasoob.me/2013/08/06/python-socket-network-programming/

# https://www.geeksforgeeks.org/socket-programming-python/
