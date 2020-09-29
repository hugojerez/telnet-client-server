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

# Step 3

Run docker

    docker run -p 23:23 -d --network host servertelnet 
    docker run  -d --network host clientetelnet 

# Step 4 (Optional)

Create a dummy docker just for fun  

    docker run -dit ubuntu