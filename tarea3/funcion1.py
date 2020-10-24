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
  try:
    # Se obtiene el argumento packet
      if packet["IP"]["proto"] == 6:
        if packet["TELNET"]["data"] == "data\n":
          # If the condition is meet
          packet["TCP"]["payload"] = str("POLY").encode("UTF-8")
        return packet
      else:
        return packet
  except:
    return packet

