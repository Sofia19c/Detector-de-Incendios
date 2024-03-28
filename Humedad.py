import random
import sys
import zmq
import time

# REcivir parametros

host = "localhost:10000"
if len(sys.argv) > 1:
    # lee el host
    host = sys.argv[1]

# Socket to talk to server
context = zmq.Context()
socket = context.socket(zmq.PUB)

socket.connect("tcp://%s" % host)

while True:
    print("En reposo")
    time.sleep(5)
    # Using random.choice()
    print("Enviando reporte de temperatura ...")
    random_Hume = (random.random() * (1 - 0.7)) + 0.7
    socket.send_string("Humedad " + str(random_Hume))
    print("Se enviò el mensaje al proxy ", "Humedad: ", random_Hume)
