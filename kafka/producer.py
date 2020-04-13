import settings

from kafka import utils


class Producer:
    TOPIC_NAME = settings.TOPIC_NAME

    def __init__(self):
        client = utils.get_client()
        topic = client.topics[self.TOPIC_NAME]
        self._producer = topic.get_sync_producer()

    def produce(self, *args, **kwargs) -> None:
        self._producer.produce(*args, **kwargs)
