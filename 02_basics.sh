#reformat:
#Commands and flags
#Use cases/scenarios

#Basic info
docker -v
docker info

#Run first container
docker run --name my_first_container busybox:latest

docker run --detach --interactive --tty --name alpine alpine:latest
#shortened:
docker run -dit --name alpine alpine:latest
#--detach | -d - run in background mode
#--interactive | -i - provide input/output
#--tty | -t - provide terminal for interactive mode

#-p publish exposed port from the docker container to the host: -p <host_port>:<container_port>
docker run -p 8080:80 nginx

#run nginx and test if it runs
docker image pull nginx:latest
docker run -p 8080:80 nginx
curl http://localhost:8080

#inspect exposed ports
docker image inspect nginx | jq .[].Config]ExposedPorts

#Run container once and print ping output in terminal
docker run -it --name my_container1 busybox:latest ping -c 6 localhost


#Container states
# ps shows only active running containers. --all shows all containers
docker ps --all | -a
docker container ls -a

docker run -dit --name my_container busybox:latest

#Pause a container
docker container pause my_container

#Unpause a container
docker container unpause my_container

#Stop a container
docker container stop my_container

#Kill a container that's not stopping
docker container kill <container_id>

#Remove a container
docker rm <container_id>

#Create but don't run a container
docker container create --name my_container2 alpine:latest


#SH into a running container
docker run -dit --name test_cont busybox:latest
docker exec -i -t test_cont sh


#Inspect containers
docker container inspect test_cont

#Logs
#Check logging driver
docker info --format '{{.LoggingDriver}}'

#Change logging driver:
run container with --log-driver or --log-opt

#Check logs in docker folder
docker run --name test -dit alpine:latest sh -c "while true; do $(echo time) sleep 10; done"
cd /var/lib/docker/containers
#if Permission Denied switch to root user: sudo -i
#use 'exit' to switch back
ls
#cd <container_id> ls -ltr
#cat <container_id>-json.log


#Check logs via command
docker run --name test_logs -dit alpine:latest sh -c "while true; do $(echo time) sleep 10; done"
docker ps

docker logs <container_id> or /test_logs
docker logs <container_id> --follow | -f
docker logs <id> --details
#show last 8 entries: docker logs /test_logs --tail 8
#show timestamps: docker logs /test_logs -t
#combine flags: docker logs /test_logs -t --tail 10

grep: docker logs /test_logs | grep pattern
docker logs /test_logs | grep error


#Images
#pull an image:
docker image pull ubuntu:latest
#pull from different registry, not docker hub
docker pull private-docker-registry.example.com/nginx
#if auth required
docker login -u <username> -p <password> private-docker-registry.example.com/nginx

#side effect: your password is stored as plain text in the shell history
#you can deal with it by piping the password directly from the file 'docker_password' with your password
docker login -u <username> --password-stdin private-docker-registry.example.com < docker_password
#windows powershell:
Get-Content docker_password | docker login -u <username> --password-stdin private-docker-registry.example.com

#Show images
docker image ls
docker image ls | --all

#Tag image
docker tag <image_id> <tag_name>

#Remove image
docker rmi <image_id>
#You can't remove image that is being used by another container. Remove the container before removing the image.

#show digests (control checksum):
docker image ls --digests
docker image history d8e1f9a8436c

#docker info
#look for Storage Driver: overlay2
#Check images:
sudo -i
cd /var/lib/docker/overlay2
ls -ltr

#Inspect image
#Useful info: Env, Cmd, Layers
docker image ls
#docker image inspect <id>|<container_name>
#Inspect ENV: docker image inspect hello-world | jq .[].Config.Env
#Inspect CMD: docker image inspect hello-world | jq .[].Config.Cmd
#Inspect Layers: docker image inspect hello-world | jq .[].RootFS.Layers

#Save image as tar-file
docker image pull nginx:latest
docker image ls
docker image save <id> > mynginx.tar
ls -ltr
ls -sh mynginx.tar

#Save reserve copy:
docker save --output nginx.tar nginx


#Create and Save image via commit without the dockerfile (install ping into ubuntu image and save changed image)
docker run -dit --name ubuntu ubuntu:latest
docker exec -it ubuntu sh
ping google.com
#>>> sh: 1: ping: not found
apt update && apt install iputils-ping -y
#now it will work: ping google.com
#Save the installed 'ping' to our myubuntu image
exit
docker commit <container_name> <new_image_name>
docker commit ubuntu myubuntu

#Check available images:
docker images
#Run the new container from created image:
docker run -it --name myubuntu myubuntu sh


#Dockerfile
#Dockerfile has commands for building a container
#Every line is a new layer
FROM: define OS for container
LABEL author="Dave": Meta data for image
LABEL description="An example Dockerfile"
ENV: env variables
RUN: apt-get install python
CMD: default command that runs after the container is built
ENTRYPOINT: entry point for the container
ADD: copy files from host to container
EXPOSE: what ports are 'published' on container creation
WORKDIR: working directory for all previous commands (FROM, LABEL, etc.)
USER: UID (user ID) or GID (group ID) for running commands
VOLUME: create mount point

#Cache
#Check if an image is in cache and retrieve it

#Build context. Pass the contents of URL/folder to docker daemon
docker build https://github.com/sathyabhat/sample-repo.git#mybranch

#Build context on tag
docker build https://github.com/sathyabhat/sample-repo.git#mytag

#Build on pull request
docker build https://github.com/sathyabhat/sample-repo.git#pull/1337/head

#You can build context on .tar files
#Passing root / to context will pass the contents of a drive to docker daemon

#Dockerignore example
*/temp*
.DS_Store
.git

#BuildKit allows you to pass secrets into layers without the secret being in the final layer.
#Switch to legacy builder
DOCKER_BUILDKIT=0 docker build .

#Build test image
FROM ubuntu:latest
CMD echo Hello World!

docker build .


#Image creation optimizations
#Multilayer dockerfile
vi Dockerfile
FROM ubuntu:latest
ENV HOME /root
LABEL ubuntu=myubuntu
ENTRYPOINT ["sleep"]
CMD ["50"]
RUN useradd -m -G root testuser
USER root
RUN apt-get update && apt-get install net-tools -y
RUN apt-get install iputils-ping -y

#Run our Dockerfile
docker build --tag myubuntu_image .

docker images ls --digests

#We've created unoptimized image containing multiple RUN commands. Let's fix that.
FROM ubuntu:latest
ENV HOME /root
LABEL ubuntu=myubuntu
ENTRYPOINT ["sleep"]
CMD ["50"]
USER root
RUN apt-get update && apt-get install net-tools -y && apt-get install iputils-ping -y && useradd -m -G root testuser

docker build --tag myubuntu_image1 .

