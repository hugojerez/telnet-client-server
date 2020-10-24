#
# Función 3
# 
# AUTORES
# Hugo Jerez <hugo.jerez@mail.udp.cl>
# Alejandro Álvarez <alejandro.alvarez@mail.udp.cl>
#
# DESCRIPCIÓN
# Cambia los puertos de origen
# por el puerto 25
#


def function(packet):
  # Se obtiene el argumento packet
  #if packet["IP"]["srcport"] == "23":
  packet["TCP"]["srcport"]  = 25
  # If the condition is meet
  return packet
