# Función

def function(packet):
  # Se obtiene el argumento packet
  if packet["TELNET"]["data"] == "data":
    packet["TCP"]["payload"] = str("POLY").encode("UTF-8")
  else:
    print("Paquete ignorado")
    # If the condition is meet
  return packet

