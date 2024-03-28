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
  """
  docstring
  """
  print("Reporte de humo: ", msg)

def procesarMensTemp(msg):
    """
    docstring
    """
    print("Reporte de la temperatura", msg)

def procesarMensHume(msg):
    """
    docstring
    """
    print("Reporte de humedad", msg)

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
