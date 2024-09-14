from kafka import KafkaConsumer
from kafka.errors import KafkaError
import sys

# Load configuration
consumer_config_path = '/etc/kafka/consumer.properties'
config = {}
with open(consumer_config_path, 'r') as file:
    for line in file:
        if line.strip() and not line.startswith('#'):
            key, value = line.strip().split('=', 1)
            config[key.strip()] = value.strip()

# Extract Kafka broker list and other configuration
bootstrap_servers = config.get('bootstrap.servers', 'localhost:9093')
group_id = config.get('group.id', 'my-consumer-group')
auto_offset_reset = config.get('auto.offset.reset', 'earliest')

# Create Kafka consumer instance
consumer = KafkaConsumer(
    'test',  # Topic to subscribe to
    bootstrap_servers=bootstrap_servers,
    group_id=group_id,
    auto_offset_reset=auto_offset_reset,
    security_protocol=config.get('security.protocol', 'PLAINTEXT'),
    sasl_mechanism='GSSAPI',  # For Kerberos
    sasl_kerberos_service_name=config.get('sasl.kerberos.service.name', 'kafka'),
    value_deserializer=lambda x: x.decode('utf-8'),
    auto_offset_reset='earliest'
)

# Consume messages
print('Starting to consume messages...')
try:
    for message in consumer:
        print(f"Received message: {message.value} from topic {message.topic}")
except KafkaError as e:
    print(f'Error while consuming messages: {e}')
finally:
    consumer.close()