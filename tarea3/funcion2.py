# Función

def function(packet):
  # Se obtiene el argumento packet
  if packet["IP"]["src"] == "127.0.0.1":
    packet["IP"]["src"]  = "32.123.123.222"
  else:
    print("Paquete ignorado")
  # If the condition is meet
  return packet
