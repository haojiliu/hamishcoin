# Author: Haoji Liu
# LABEL maintainer="divid86391@hotmail.com"
FROM ubuntu:16.04

# Update OS
RUN sed -i 's/# \(.*multiverse$\)/\1/g' /etc/apt/sources.list

RUN apt-get update
RUN apt-get -y install python3-pip man build-essential python-dev curl vim net-tools ssh openssh-server sudo wget iputils-ping tree

ADD ./config /srv/config
RUN pip3 install --upgrade pip
RUN pip3 install -r /srv/config/requirements.txt

EXPOSE 5000

CMD ["python", "/srv/src/main.py", "--port", "5000"]
