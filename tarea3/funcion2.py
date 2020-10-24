#
# Función 2
# 
# AUTORES
# Hugo Jerez <hugo.jerez@mail.udp.cl>
# Alejandro Álvarez <alejandro.alvarez@mail.udp.cl>
#
# DESCRIPCIÓN
# Cambia la dirección IP de origen
# por la IP 32.123.123.222 (Dirección inventada)
#

def function(packet):
  # Se obtiene el argumento packet
  if packet["IP"]["src"] == "127.0.0.1":
    packet["IP"]["src"]  = "32.123.123.222"
  else:
    print("Paquete ignorado")
  # If the condition is meet
  return packet

