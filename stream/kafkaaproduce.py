from kafka import KafkaProducer
producer = KafkaProducer(bootstrap_servers='localhost:9092')
producer.send('NSE', b'Hello, World!')
producer.send('NSE', key=b'message-two', value=b'This is Kafka-Python')