# docker -v

# Run first container
# docker run --name my_first_container busybox:latest

# docker run --detach --interactive --tty --name alpine alpine:latest
# --detach | -d - run in background mode
# ??? --interactive | -i - provide input/output
# ??? --tty | -t - provide terminal for interactive mode
# shortened: docker run -dit --name alpine alpine:latest

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