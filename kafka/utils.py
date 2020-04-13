import pykafka

import settings


def get_client() -> pykafka.KafkaClient:
    return pykafka.KafkaClient(
        hosts=f'{settings.KAFKA_HOST}:{settings.KAFKA_PORT}'
    )
