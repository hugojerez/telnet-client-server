#
# Función 5
# 
# AUTORES
# Hugo Jerez <hugo.jerez@mail.udp.cl>
# Alejandro Álvarez <alejandro.alvarez@mail.udp.cl>
#
# DESCRIPCIÓN
# Deja el intervalo del paquete inválido (anulado)
# Esta invalidación se logra anulando el paquete
# dandole un ancho igual a cero
#

def function(packet):
  if packet["IP"]["proto"] == 6:
    packet["TCP"]["len"]  = "0x0"
  else:
    return packet 

