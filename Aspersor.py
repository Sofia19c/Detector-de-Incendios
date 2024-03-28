import zmq
import sys

host = "localhost:10100"
if len(sys.argv) > 1:
    # lee el host
    host = sys.argv[1]

context = zmq.Context()
socket = context.socket(zmq.SUB)
socket.connect("tcp://%s" % host)

# Subscribe
socket.subscribe("")


def procesarMensHumo(msg):
    if msg == "True":
      print("ALERTA! ASPERSOR ENCENDIDO")


# Process 5 updates
while True:
    print("Escuchando ...")
    total_value = 0
    topic, msg = socket.recv_string().split(" ")
    print("Recibido un mensaje")
    if topic == "Humo":
        procesarMensHumo(msg)
