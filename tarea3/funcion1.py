#
# Función 1
# 
# AUTORES
# Hugo Jerez <hugo.jerez@mail.udp.cl>
# Alejandro Álvarez <alejandro.alvarez@mail.udp.cl>
#
# DESCRIPCIÓN
# Cambia el contenido del paquete si la palabra es “data” la
# convierte por “POLY”
#
def function(packet):
  # Se obtiene el argumento packet
  if packet["TELNET"]["data"] == "data\n":
    packet["TCP"]["payload"] = str("POLY").encode("UTF-8")
  # If the condition is meet
  return packet

