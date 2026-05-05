import zmq, time, pickle, sys, socket as sock
from constPipe import *  #-

context = zmq.Context()
me = str(sys.argv[1]) if len(sys.argv) > 1 else sock.gethostname()
r  = context.socket(zmq.PULL)     # create a pull socket
p1 = "tcp://"+ SRC1 +":"+ PORT1   # address first task source
p2 = "tcp://"+ SRC2 +":"+ PORT2   # address second task source
r.connect(p1)                     # connect to task source 1
r.connect(p2)                     # connect to task source 2
#-
print (me + " started") #-

while True:
  work = pickle.loads(r.recv())   # receive work from a source
  print (me + " received " + str(work)) #-
  time.sleep(work*0.01)        # pretend to work
 