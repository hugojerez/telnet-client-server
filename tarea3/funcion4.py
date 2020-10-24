#
# Función 4
# 
# AUTORES
# Hugo Jerez <hugo.jerez@mail.udp.cl>
# Alejandro Álvarez <alejandro.alvarez@mail.udp.cl>
#
# DESCRIPCIÓN
# Cambia los flags por URG
# Le da prioridad Urgente al paquete
#


def function(packet):
  if packet["IP"]["proto"] == 6:
    # Cuando los flags se emitan de forma
    # común y corriente (0x018) se le añadirá 
    # el flag de urgent

    if packet["TCP"]["flags"] == 0x018:
      packet["TCP"]["flags"]   = 0x020
    return packet
  else:
    return packet


