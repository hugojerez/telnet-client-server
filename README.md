# Video in action

[![Polymorph](https://img.youtube.com/vi/AMVPcL8OY0E/1.jpg)](https://youtu.be/AMVPcL8OY0E)


# Video (In spanish)
    
    https://www.youtube.com/embed/AXkPJoVW7UM

# STEP 1

Install telnet client 

    cd client
    docker build -t clientetelnet .
    cd ../

# STEP 2

Install telnet server

    cd server
    docker build -t servertelnet .
    cd ../

# STEP 3

Run docker

    docker run --network host  -p 23:23 -d servertelnet 
    docker run  -d --network host clientetelnet 

# STEP 4 : Intall Wireshark 

    docker run \
    --name=wireshark \
    --network=host \
    --cap-add=NET_ADMIN \
    -e PUID=1000 \
    -e PGID=1000 \
    -e TZ=Europe/London \
    -p 3000:3000 \
    linuxserver/wireshark

# STEP 5 (Optional)

Create a dummy docker just for fun  

    docker run --network host -dit ubuntu