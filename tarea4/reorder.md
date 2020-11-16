## Navegación

- [Método Activo 1 (Delay)](https://github.com/hugojerez/telnet-client-server/blob/master/tarea4/delay.md)
- [Método Activo 2 (Reorder)](https://github.com/hugojerez/telnet-client-server/blob/master/tarea4/reorder.md)
- [Método Activo 3 (Packet Loss)](https://github.com/hugojerez/telnet-client-server/blob/master/tarea4/packetloss.md)
- [Método Activo 4 (Packet Corruption)](https://github.com/hugojerez/telnet-client-server/blob/master/tarea4/corruption.md)
- [Youtube](https://github.com/hugojerez/telnet-client-server/blob/master/tarea4/youtube.md)
- [PCAP](https://github.com/hugojerez/telnet-client-server/blob/master/tarea4/pcap/)
- [Función Pasivo en tiempo real](https://github.com/hugojerez/telnet-client-server/blob/master/tarea4/pcap/function.md)


## Método Activo Offline
# Packet Reorder

|Atributo|Descripción|
|--|--|
|Método|Reorder|
|Autores|Hugo Jerez - Alejandro Álvarez |
|Función|Esto hace que cada 5 (o 10, 15, 20, ...) el paquete se envíe inmediatamente y cada dos el paquete se retrasa 10 ms. .|
|Protocolo|Telnet|
|Pcap|00002.pcap (véase en el repositorio)|


### Tc-Netem

    sudo tc qdisc add  dev lo root netem delay 10ms reorder 25% 50%

### Tshark (Archivo generado de métrica) 

    tshark -r r00002.pcap -T fields -e ip.len > r00002len.dat
    tshark -r r00002.pcap -T fields -e frame.time_epoch  > r00002time.dat

### Matlab


    data = load('r00002len.dat') 
    timeT = load('r00002time.dat')
    timeTB = timeT - timeT(1)
    plot(timeTB,data)

### Matlab output

![Gráfica](https://i.imgur.com/LYYPRaA.jpg)


_El Eje horizontal corresponde al tiempo en milisegundos (ms), el eje vertical corresponde a la cantidad de datos (%) transmitidos_

### ¿Qué se esperaba? (Expectativa previa)

Se esperaba que Telnet entre en algún tipo de bucle al perder la lógica y orden de sus paquetes

### ¿Qué se obtuvo?  (Resultados)

A pesar de alterar el orden de los paquetes, Telnet mostró una constante inestabilidad en la transmisión de paquetes, advirtiendo mediante un paquete con la información "spurious retransmission"


### Búsqueda de un valor crítico

Se ha determinado que todo reordenamiento sobre el 25% afecta la transmisión de datos