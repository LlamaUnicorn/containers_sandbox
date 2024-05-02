FROM ubuntu:latest
ENV HOME /root
LABEL ubuntu=myubuntu
ENTRYPOINT ["sleep"]
CMD ["50"]
USER root
RUN apt-get update && apt-get install net-tools -y && apt-get install iputils-ping -y && useradd -m -G root testuser
