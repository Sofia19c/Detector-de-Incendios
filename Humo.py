import random
import sys
import zmq
import time

# REcivir parametros

host = "localhost:10000"
if len(sys.argv) > 1:
  # lee el host
  host = sys.argv[1]


hostAspersor = "localhost:20000"
if len(sys.argv) > 2:
  hostAspersor = sys.argv[2]
  
# Socket to talk to server
context = zmq.Context()
socket = context.socket(zmq.PUB)

socket.connect ("tcp://%s" % host)


socketAspersor = context.socket(zmq.REQ)
socketAspersor.connect("tcp://%s" % hostAspersor)

while True:
    print("En reposo")
    time.sleep(3)
    # Using random.choice()
    print("Enviando reporte de humo ...")
    random_bool = True if random.random() > 0.9 else False
    socket.send_string("Humo " + str(random_bool))
    print("Se enviò el mensaje al proxy ", "Alerta! se esta incendiando", random_bool)
    if random_bool == True:
      socketAspersor.send_string("Alerta")
      socketAspersor.recv_string()
    