# Función

def filter_icmp_packets(packet):
    # Se obtiene el argumento packet
    
    if packet["IP"]["addr"] == "127.0.0.1"
        packet["IP"]["addr"]  = "53.123.123.222"
    else
        print("Paquete ignorado")
    # If the condition is meet
    return packet

