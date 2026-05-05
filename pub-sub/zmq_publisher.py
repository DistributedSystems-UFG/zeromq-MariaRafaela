import zmq, time
from consts import PORT

context = zmq.Context()
socket = context.socket(zmq.PUB)
socket.bind(f"tcp://*:{PORT}")

for i in range(5): # para o programa não rodar eternamente
    time.sleep(5)
    t = "TIME " + time.asctime()
    socket.send(t.encode())