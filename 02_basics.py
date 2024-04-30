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