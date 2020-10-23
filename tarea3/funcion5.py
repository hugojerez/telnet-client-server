# Función

def function(packet):
  # Se obtiene el argumento packet
  if packet["TCP"]["len"] == "0x80":
    packet["TCP"]["len"]  = "0x0"
  # If the condition is meet
  return packet

