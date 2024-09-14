FROM ubuntu:20.04
MAINTAINER d.gasparina@gmail.com
ENV container docker

# Update and install necessary packages
RUN apt-get update && apt-get install -y \
    gnupg \
    wget \
    openjdk-11-jdk \
    krb5-user \
    krb5-config

# Install Kerberos packages and related dependencies
RUN apt-get update && apt-get install -y \
    libkrb5-dev \
    gcc \
    libsasl2-dev

RUN apt-get update && apt-get install -y python3 python3-pip
RUN pip3 install kafka-python
RUN pip3 install gssapi

# 1. Adding Confluent repository
RUN wget -qO - https://packages.confluent.io/deb/5.4/archive.key | apt-key add -
RUN echo "deb [arch=amd64] https://packages.confluent.io/deb/5.4 stable main" | tee /etc/apt/sources.list.d/confluent.list

# 2. Install confluent kafka tools:
RUN apt-get update && apt-get install -y confluent-kafka-2.12

# 3. Copy in required settings for client access to Kafka
COPY consumer.properties /etc/kafka/consumer.properties
COPY producer.properties /etc/kafka/producer.properties
COPY command.properties /etc/kafka/command.properties
COPY client.sasl.jaas.config /etc/kafka/client_jaas.conf
COPY producer.py /etc/kafka/producer.py
COPY consumer.py /etc/kafka/consumer.py

ENV KAFKA_OPTS=-Djava.security.auth.login.config=/etc/kafka/kafka_server_jaas.conf

CMD sleep infinity
