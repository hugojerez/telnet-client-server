## Navegación

- [Método Activo 1 (Delay)](https://github.com/hugojerez/telnet-client-server/blob/master/tarea4/delay.md)
- [Método Activo 2 (Reorder)](https://github.com/hugojerez/telnet-client-server/blob/master/tarea4/reorder.md)
- [Método Activo 3 (Packet Loss)](https://github.com/hugojerez/telnet-client-server/blob/master/tarea4/packetloss.md)
- [Método Activo 4 (Packet Corruption)](https://github.com/hugojerez/telnet-client-server/blob/master/tarea4/corruption.md)
- [Youtube](https://github.com/hugojerez/telnet-client-server/blob/master/tarea4/youtube.md)
- [PCAP](https://github.com/hugojerez/telnet-client-server/blob/master/tarea4/pcap/)
- [Función Pasivo en tiempo real](https://github.com/hugojerez/telnet-client-server/blob/master/tarea4/pcap/function.md)


## Método Activo Offline
# Packet Corruption

|Atributo|Descripción|
|--|--|
|Autores|Hugo Jerez - Alejandro Álvarez |
|Método|Packet Corruption|
|Función|El ruido aleatorio se puede emular con la opción correcta. Eso introduce un error de un solo bit en un desplazamiento aleatorio en el paquete|Telnet|
|Pcap|00004.pcap (véase en el repositorio)|


### Tc-Netem

    
    sudo tc qdisc add dev lo root netem corrupt 5%


### Tshark 

    tshark -r r00004.pcap -T fields -e ip.len > r00004len.dat
    tshark -r r00004.pcap -T fields -e frame.time_epoch  > r00004time.dat

### Matlab


    data = load('r00004len.dat') 
    timeT = load('r00004time.dat')
    timeTB = timeT - timeT(1)
    plot(timeTB,data)

### Matlab output

![Gráfica](https://i.imgur.com/ICZcyw4.jpg)


_El Eje horizontal corresponde al tiempo en milisegundos (ms), el eje vertical corresponde a la cantidad de datos (%) transmitidos_

### ¿Qué se esperaba? (Expectativa previa)

Se esperaba que los datos se dañaran y se volvieran a retransmitir 

### ¿Qué se obtuvo?  (Resultados)

Cada vez se fue volviendo más lenta la retransmisión hasta que apareció un error finalizando toda la transmisión indicando que habían paquetes duplicados