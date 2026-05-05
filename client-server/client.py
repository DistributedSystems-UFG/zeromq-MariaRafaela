import zmq
from consts import HOST, PORT

context = zmq.Context()
socket  = context.socket(zmq.REQ)       # create request socket

socket.connect("tcp://"+HOST+":"+PORT)  # block until connected
socket.send(b"Hello world")             # send message
message = socket.recv()                 # block until response
socket.send(b"STOP")                    # tell server to stop
print(message.decode())                 # print result