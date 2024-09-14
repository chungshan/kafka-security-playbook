from kafka import KafkaProducer
from kafka.errors import KafkaError
import os

# Load configuration
producer_config_path = '/etc/kafka/producer.properties'
config = {}
with open(producer_config_path, 'r') as file:
    for line in file:
        if line.strip() and not line.startswith('#'):
            key, value = line.strip().split('=', 1)
            config[key.strip()] = value.strip()

# Extract Kafka broker list and other configuration
bootstrap_servers = config.get('bootstrap.servers', 'localhost:9093')
security_protocol = config.get('security.protocol', 'PLAINTEXT')
sasl_kerberos_service_name = config.get('sasl.kerberos.service.name', 'kafka')
sasl_jaas_config = config.get('sasl.jaas.config', '')

# Create Kafka producer instance
producer = KafkaProducer(
    bootstrap_servers=bootstrap_servers,
    security_protocol=security_protocol,
    sasl_mechanism='GSSAPI',  # SASL_KERBEROS corresponds to GSSAPI
    sasl_kerberos_service_name=sasl_kerberos_service_name,
    acks='all'
)

# Define topic and message
topic = 'test'
message = 'Hello Kafka!'

# Send message
try:
    producer.send(topic, value=message.encode('utf-8'))
    producer.flush()  # Ensure all messages are sent
    print(f'Message "{message}" sent to topic "{topic}".')
except KafkaError as e:
    print(f'Failed to send message: {e}')

# Close the producer
producer.close()
