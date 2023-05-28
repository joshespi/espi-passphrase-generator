# simple python password generator
 
build with  ```docker build -t passphrase-generator .```

run with ```docker run -d -p 5000:5000 passphrase-generator```

You should be able to navigate to the servers IP:5000

## optional setting
Tell the docker container to auto start, unless you stop it. ```docker update --restart unless-stopped container_id```