from pykafka import KafkaClient


class Producer:
    TOPIC_NAME = "bus"

    def __init__(self):
        client = KafkaClient(hosts="localhost:9092")
        topic = client.topics[self.TOPIC_NAME]
        self._producer = topic.get_sync_producer()

    def produce(self, *args, **kwargs) -> None:
        self._producer.produce(*args, **kwargs)
