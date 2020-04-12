import os

import pykafka

from kafka import utils


def get_messages() -> pykafka.SimpleConsumer:
    client = utils.get_client()
    return client.topics[os.environ["TOPIC_NAME"]].get_simple_consumer()
