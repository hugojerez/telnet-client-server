# Función

def function(packet):
  # Se obtiene el argumento packet
  if packet["TELNET"]["data"] == "data\n":
    packet["TCP"]["payload"] = str("POLY").encode("UTF-8")
  # If the condition is meet
  return packet

