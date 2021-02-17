FROM ubuntu:20.04
RUN apt-get update
RUN apt-get install python3 python3-pip -y
COPY . /equin-dj-docker
WORKDIR /equin-dj-docker
RUN pip3 install -r requirements.txt