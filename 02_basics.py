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

# docker run --name test -dit alpine:latest sh -c "while true; do $(echo time) sleep 10; done"
# cd /var/lib/docker/containers
# ls
# cd ls -ltr
# cat -json.log


# docker run --name test_logs -dit alpine:latest sh -c "while true; do $(echo time) sleep10; done"
# docker ps
# docker logs <container_id>
# docker logs <container_id> -follow
# docker logs <id> --detail