# Run producer consumer python script
1. producer: `docker-compose exec client bash -c 'kinit -k -t /var/lib/secret/kafka-client.keytab kafka_producer && python3 /etc/kafka/producer.py'`
2. consumer: `docker-compose exec client bash -c 'kinit -k -t /var/lib/secret/kafka-client.keytab kafka_consumer && python3 /etc/kafka/consumer.py'`