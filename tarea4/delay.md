## Navegación

- [Método Activo 1 (Delay)](https://github.com/hugojerez/telnet-client-server/blob/master/tarea4/delay.md)
- [Método Activo 2 (Reorder)](https://github.com/hugojerez/telnet-client-server/blob/master/tarea4/reorder.md)
- [Método Activo 3 (Packet Loss)](https://github.com/hugojerez/telnet-client-server/blob/master/tarea4/packetloss.md)
- [Método Activo 4 (Packet Corruption)](https://github.com/hugojerez/telnet-client-server/blob/master/tarea4/corruption.md)
- [Youtube](https://github.com/hugojerez/telnet-client-server/blob/master/tarea4/youtube.md)
- [PCAP](https://github.com/hugojerez/telnet-client-server/blob/master/tarea4/pcap/)
- [Función Pasivo en tiempo real](https://github.com/hugojerez/telnet-client-server/blob/master/tarea4/pcap/function.md)



## Método Activo Offline
# Packet Delay

|Atributo|Descripción|
|--|--|
|Método|Delay|
|Función|Hace que el retardo adicional sea de 60000 ms ± 6000 ms con el siguiente elemento aleatorio dependiendo del 25% en el último.|
|Protocolo|Telnet|
|Pcap|00001.pcap (véase en el repositorio)|


### Tc-Netem

    sudo tc qdisc add dev lo root netem delay 60000ms 6000ms 25%

### Tshark 

    tshark -r r00001.pcap -T fields -e ip.len > r00001len.dat
    tshark -r r00001.pcap -T fields -e frame.time_epoch  > r00001time.dat

### Matlab


    data = load('r00001len.dat') 
    timeT = load('r00001time.dat')
    timeTB = timeT - timeT(1)
    plot(timeTB,data)
    cdfplot(data)

### Matlab output

![Gráfica](https://i.imgur.com/ntwCoSc.jpg)


_El Eje horizontal corresponde al tiempo en milisegundos (ms), el eje vertical corresponde a la cantidad de datos (%) transmitidos_

### ¿Qué se esperaba? (Expectativa previa)

Se esperaba recibir un error de TimeOut cortando el túnel de Telnet

### ¿Qué se obtuvo?  (Resultados)

A pesar de haber peticiones con un delay gigantezco de aproximadamente 1 minuto, el protocolo Telnet lograba controlar la situación acumulando mucha data en cada paquete, y generando patrones de re-transmisión 