# docker -v

# Run first container
# docker run --name my_first_container busybox:latest

# docker run --detach --interactive --tty --name alpine alpine:latest
# shortened: docker run -dit --name alpine alpine:latest
# --detach | -d - run in background mode
# --interactive | -i - provide input/output
# --tty | -t - provide terminal for interactive mode

# Run container once and print ping output in terminal
# docker run -it --name my_container1 busybox:latest ping -c 6 localhost


# Container states
# docker ps --all | -a
# docker container ls -a

# docker run -dit --name my_container busybox:latest

# Pause a container
# docker container pause my_container

# Unpause a container
# docker container unpause my_container

# Stop a container
# docker container stop my_container

# Create but don't run a container
# docker container create --name my_container2 alpine:latest


# SH into a running container
# docker run -dit --name test_cont busybox:latest
# docker exec -i -t test_cont sh


# Inspect containers
# docker container inspect test_cont

# Logs
# Check logging driver
# docker info --format '{{.LoggingDriver}}'

# Change logging driver: run container with --log-driver or --log-opt

# Check logs in docker folder
# docker run --name test -dit alpine:latest sh -c "while true; do $(echo time) sleep 10; done"
# cd /var/lib/docker/containers
# if Permission Denied switch to root user: sudo -i
# use 'exit' to switch back
# ls
# cd <container_id> ls -ltr
# cat <container_id>-json.log


# Check logs via command
# docker run --name test_logs -dit alpine:latest sh -c "while true; do $(echo time) sleep 10; done"
# docker ps

# docker logs <container_id> or /test_logs
# docker logs <container_id> --follow | -f
# docker logs <id> --details
# show last 8 entries: docker logs /test_logs --tail 8
# show timestamps: docker logs /test_logs -t
# combine flags: docker logs /test_logs -t --tail 10

# grep: docker logs /test_logs | grep pattern
# docker logs /test_logs | grep error


# Images
# pull an image: docker image pull ubuntu:latest
# docker image ls | --all
# show digests (control checksum): docker image ls --digests
# docker image history d8e1f9a8436c

# docker info
# look for Storage Driver: overlay2
# Check images:
# sudo -i
# cd /var/lib/docker/overlay2
# ls -ltr

# Inspect image
# docker image inspect <id>

# Save image as tar-file
# docker image pull nginx:latest
# docker image ls
# docker image save <id> > mynginx.tar
# ls -ltr
# ls -sh mynginx.tar

# Save reserve copy:
# docker save --output nginx.tar nginx


# Create and Save image via commit without the dockerfile (install ping into ubuntu image and save changed image)
# docker run -dit --name ubuntu ubuntu:latest
# docker exec -it ubuntu sh
# ping google.com
# >>> sh: 1: ping: not found
# apt update && apt install iputils-ping -y
# now it will work: ping google.com
# Save the installed 'ping' to our myubuntu image
# exit
# docker commit <container_name> <new_image_name>
# docker commit ubuntu myubuntu
# Check available images:
# docker images
# Run the new container from created image: docker run -it --name myubuntu myubuntu sh


# Dockerfile
# Dockerfile has commands for building a container
# Every line is a new layer
# FROM: define OS for container
# LABEL: Meta data for image
# ENV: env variables
# RUN:
# CMD: default command that runs after the container is built
# ENTRYPOINT: entry point for the container
# ADD: copy files from host to container
# EXPOSE: what ports are 'published' on container creation
# WORKDIR: working directory for all previous commands (FROM, LABEL, etc.)
# USER: UID (user ID) or GID (group ID) for running commands
# VOLUME: create mount point

# Cache
# Check if an image is in cache and retrieve it


# Image creation optimizations
# Multilayer dockerfile
# vi Dockerfile
# FROM ubuntu:latest
# ENV HOME /root
# LABEL ubuntu=myubuntu
# ENTRYPOINT ["sleep"]
# CMD ["50"]
# RUN useradd -m -G root testuser
# USER root
# RUN apt-get update && apt-get install net-tools -y
# RUN apt-get install iputils-ping -y

# Run our Dockerfile
# docker build --tag myubuntu_image .

# docker images ls --digests

# We've created unoptimized image containing multiple RUN commands. Let's fix that.
# FROM ubuntu:latest
# ENV HOME /root
# LABEL ubuntu=myubuntu
# ENTRYPOINT ["sleep"]
# CMD ["50"]
# USER root
# RUN apt-get update && apt-get install net-tools -y && apt-get install iputils-ping -y && useradd -m -G root testuser

# docker build --tag myubuntu_image1 .

