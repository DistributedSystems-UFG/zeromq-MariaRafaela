import zmq
from consts import HOST, PORT

context = zmq.Context()
socket = context.socket(zmq.SUB)
socket.connect(f"tcp://{HOST}:{PORT}")
socket.setsockopt(zmq.SUBSCRIBE, b"TIME")

for i in range(5):
    time = socket.recv()
    print(time.decode())