FROM ubuntu:22.04

ENV DEBIAN_FRONTEND noninteractive

RUN apt update \
    && apt install -y git-all \
        python3-dev python3-pip python3-setuptools \
        cmake build-essential libssl-dev

COPY bin/ /app

WORKDIR /app

RUN pip3 install --upgrade pip

RUN pip3 install -r requirements.txt

ENV WAIT_VERSION 2.7.2

ADD https://github.com/ufoscout/docker-compose-wait/releases/download/$WAIT_VERSION/wait /wait

RUN chmod +x /wait

CMD ["python3", "app.py"]
