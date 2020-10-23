# Función

def function(packet):
  # Se obtiene el argumento packet
  if packet["IP"]["srcport"] == "23"
    packet["IP"]["srcport"]  = "25"
  else
    print("Paquete ignorado")
  # If the condition is meet
  return packet

