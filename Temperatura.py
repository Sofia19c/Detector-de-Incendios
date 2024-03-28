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
    time.sleep(6)
    # Using random.choice()
    print("Enviando reporte de temperatura ...")
    random_temp = (random.random() * (29.4 - 11 )) + 11
    socket.send_string("Temperatura " + str(random_temp))
    print("Se enviò el mensaje al proxy ", "Temperatura: ", random_temp)
