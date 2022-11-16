# InterviewTrainer


# steps:

## first build all the image and push them to docker (you can have your own docker repo)

sudo docker build -f Dockerfile -t mathildast/rasa-test:debugged  .
sudo docker push mathildast/rasa-test:debugged
sudo docker build -f Dockerfile-action.yml.dockerfile -t mathildast/rasa-action:debugged  .
sudo docker push mathildast/rasa-action:debugged

## in a seperate shell (or screen using command `screen`)
```
sudo docker image ls
sudo docker run <image name>

```
## back in the main shell, move the trained model out
```
sudo docker ps
sudo docker cp <containerID>:/app/models/<model name> models/
```

## check if the new models is in the folder
```
ls models/
```

## sprung up the server
sudo docker-compose up -d
