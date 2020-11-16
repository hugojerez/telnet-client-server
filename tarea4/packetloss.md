## Navegación

- [Método Activo 1 (Delay)](https://github.com/hugojerez/telnet-client-server/blob/master/tarea4/delay.md)
- [Método Activo 2 (Reorder)](https://github.com/hugojerez/telnet-client-server/blob/master/tarea4/reorder.md)
- [Método Activo 3 (Packet Loss)](https://github.com/hugojerez/telnet-client-server/blob/master/tarea4/packetloss.md)
- [Método Activo 4 (Packet Corruption)](https://github.com/hugojerez/telnet-client-server/blob/master/tarea4/corruption.md)
- [Youtube](https://github.com/hugojerez/telnet-client-server/blob/master/tarea4/youtube.md)
- [PCAP](https://github.com/hugojerez/telnet-client-server/blob/master/tarea4/pcap/)
- [Función Pasivo en tiempo real](https://github.com/hugojerez/telnet-client-server/blob/master/tarea4/pcap/function.md)


## Método Activo Offline
# Packet Loss

|Atributo|Descripción|
|--|--|
|Método|Packet Loss|
|Autores|Hugo Jerez - Alejandro Álvarez |
|Función|Este comando hace que se pierda el 5% de los paquetes.|
|Protocolo|Telnet|
|Pcap|00003.pcap (véase en el repositorio)|


### Tc-Netem

    sudo tc qdisc add dev lo root netem loss 5%

### Tshark 

    tshark -r r00003.pcap -T fields -e ip.len > r00003len.dat
    tshark -r r00003.pcap -T fields -e frame.time_epoch  > r00003time.dat

### Matlab


    data = load('r00003len.dat') 
    timeT = load('r00003time.dat')
    timeTB = timeT - timeT(1)
    plot(timeTB,data)

### Matlab output

![Gráfica](https://i.imgur.com/Pr4wEh7.jpg)


_El Eje horizontal corresponde al tiempo en milisegundos (ms), el eje vertical corresponde a la cantidad de datos (%) transmitidos_

### ¿Qué se esperaba? (Expectativa previa)

Se esperaba que se vuelvan a retransmitir los paquetes perdidos

### ¿Qué se obtuvo?  (Resultados)

Se cumplió el resultado esperado, se re-acumulaba la información dentro del siguiente paquete