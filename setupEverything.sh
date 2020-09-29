# INSTALAR DOCKER CLIENTE
cd client
docker build -t clientetelnet .

cd ../

# INSTALAR DOCKER SERVIDOR

cd server
docker build -t servertelnet .
cd ../

# CORRER DOCKER

docker run -p 23:23 -d --network host servertelnet 
docker run  -d --network host clientetelnet 


docker run -dit ubuntu