# Start Zookeeper:
```
zookeeper-server-start /usr/local/etc/kafka/zookeeper.properties
```
# Start Kafka server:
```
kafka-server-start /usr/local/etc/kafka/server.properties
```
# Create Kafka Topic:
```
kafka-topics --create --zookeeper localhost:2181 --replication-factor 1 --partitions 1 --topic bus
```
