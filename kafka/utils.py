import os

import pykafka


def get_client() -> pykafka.KafkaClient:
    return pykafka.KafkaClient(
        hosts=f'{os.environ["KAFKA_HOST"]}:{os.environ["KAFKA_PORT"]}'
    )
