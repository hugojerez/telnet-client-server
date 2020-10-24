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
  if packet["IP"]["proto"] == 6:
    print("cumple el protocolo")
    # Se obtiene el argumento packet
    if packet["TCP"]["srcport"] != 23:
      # If the condition is meet
      packet["TCP"]["srcport"]  = 25
  return packet
