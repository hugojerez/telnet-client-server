# Función

def filter_icmp_packets(packet):
  # Se obtiene el argumento packet
  if packet["TCP"]["flags"] == "24":
    packet["TCP"]["flags"]  = "32"
  # If the condition is meet
  return packet

