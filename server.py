import zmq
import sys

host = "localhost:10100"
if len(sys.argv) > 1:
    host = sys.argv[1]

context = zmq.Context()
socket = context.socket(zmq.SUB)
socket.connect("tcp://%s" % host)

# Subscribe
socket.subscribe("")

def procesarMensHumo(msg):
  if msg == "True":
    print("Reporte de humo: ", msg)
  elif msg == "False":
    print("Reporte de humo: ", msg)
  else:
    print("Mensaje no valido") 


def procesarMensTemp(msg):
    temp= float(msg)
    if temp > 11 and temp < 29.4:
      print("Reporte de la temperatura", msg)
    else:
       print("Mensaje no valido")
   
def procesarMensHume(msg):
    hume = float(msg)
    if hume > 0.7 and hume < 1:
      print("Reporte de humedad", msg)
    else:
       print("Mensaje no valido")

def procesarMensAsper(msg):
    """
    docstring
    """
    print("Reporte de Aspersor", msg)


# Process 5 updates
while True:
  print("Escuchando ...")
  total_value = 0
  topic, msg = socket.recv_string().split(" ")
  print("Recibido un mensaje")
  if topic == "Humo":
    procesarMensHumo(msg)
  elif topic == "Temperatura":
    procesarMensTemp(msg)
  elif topic == "Humedad":
    procesarMensHume(msg)
  elif topic == "Aspersor":
    procesarMensAsper(msg)
