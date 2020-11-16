## Navegación

- [Método Activo 1 (Delay)](https://github.com/hugojerez/telnet-client-server/blob/master/tarea4/delay.md)
- [Método Activo 2 (Reorder)](https://github.com/hugojerez/telnet-client-server/blob/master/tarea4/reorder.md)
- [Método Activo 3 (Packet Loss)](https://github.com/hugojerez/telnet-client-server/blob/master/tarea4/packetloss.md)
- [Método Activo 4 (Packet Corruption)](https://github.com/hugojerez/telnet-client-server/blob/master/tarea4/corruption.md)
- [Youtube](https://github.com/hugojerez/telnet-client-server/blob/master/tarea4/youtube.md)
- [PCAP](https://github.com/hugojerez/telnet-client-server/blob/master/tarea4/pcap/)
- [Función Pasivo en tiempo real](https://github.com/hugojerez/telnet-client-server/blob/master/tarea4/pcap/function.md)

## Método Pasivo en tiempo real

   [Ver archivo Python](https://github.com/hugojerez/telnet-client-server/blob/master/tarea4/pcap/function.py)

### Tshark 

    tshark -r r00005.pcap -T fields -e ip.len > r00005len.dat
    tshark -r r00005.pcap -T fields -e frame.time_epoch  > r00005time.dat

### Matlab


    data = load('r00005len.dat') 
    timeT = load('r00005time.dat')
    timeTB = timeT - timeT(1)
    plot(timeTB,data)

### Matlab output

![Gráfica](https://i.imgur.com/VHBhK9r.jpg)


_El Eje horizontal corresponde al tiempo en milisegundos (ms), el eje vertical corresponde a la cantidad de datos (%) transmitidos_
