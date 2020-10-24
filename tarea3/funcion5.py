#
# Función 5
# 
# AUTORES
# Hugo Jerez <hugo.jerez@mail.udp.cl>
# Alejandro Álvarez <alejandro.alvarez@mail.udp.cl>
#
# DESCRIPCIÓN
# Deja el intervalo del paquete inválido (anulado)
#

def function(packet):
  if packet["IP"]["proto"] == 6:
    return None
  else:
    return packet 

