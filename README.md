# InterviewTrainer


# steps:

## first build all the image and push them to docker

```
sudo docker build -f Dockerfile -t <accountname>/<rasa repo name>:<tag>  .
sudo docker push <accountname>/<rasa repo name>:<tag>
sudo docker build -f Dockerfile-action.yml.dockerfile -t <accountname>/<rasa action repo name>:<tag>  .
sudo docker push <accountname>/<rasa action repo name>:<tag>
```

## in a seperate shell (or screen using command `screen`)
```
sudo docker image ls
sudo docker run <image id>

```
## back in the main shell, move the trained model out
```
sudo docker ps
sudo docker cp <containerID>:/app/models/<model name> models/
```

## then go back to the previous shell 
do `crtl-c` to stop the container

## check if the new models is in the folder
```
ls models/
```

## sprung up the server
sudo docker-compose up -d


# debugging
if you need to debug the rasa server, please add -vv to the docker-compose.yml as the last line under command. 
