import zmq
import sys

port = "20000"
if len(sys.argv) > 1:
    # lee el host
    port = sys.argv[1]

context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:%s" % port)


def procesarMensHumo():
    print("ALERTA! ASPERSOR ENCENDIDO")


# Process 5 updates
while True:
    print("Escuchando ...")
    msg = socket.recv_string()
    print("Recibido un mensaje")
    if msg == "Alerta":
        procesarMensHumo()
    socket.send_string("Response")
