#
# Método Pasivo en tiempo real
# 
# AUTORES
# Hugo Jerez <hugo.jerez@mail.udp.cl>
# Alejandro Álvarez <alejandro.alvarez@mail.udp.cl>
#
# DESCRIPCIÓN
# Realiza un packet loss
#

def function(packet):
  import random
  if random.uniform(0, 1) > 0.5 :
      print("Paquete perdido")
      if packet["IP"]["proto"] == 6:
        packet["TCP"]["len"]  = "0x0"
  else:
    print("paquete mantenido")
    return packet
