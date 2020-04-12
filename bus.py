import json
import time
import itertools

import utils
from kafka import producer


class Bus:
    def __init__(self, number: int, coordinates: itertools.cycle):
        self._producer = producer.Producer()
        self.number = number
        self.coordinates = coordinates

    def run(self) -> None:
        for coordinate in self.coordinates:
            self._producer.produce(json.dumps({
                "bus_number": self.number,
                "key": f"{self.number}_{utils.generate_uuid()}",
                "latitude": coordinate[1],
                "longitude": coordinate[0],
            }).encode('ascii'))
            time.sleep(1)


if __name__ == '__main__':
    input_file = open('data/bus25.json')
    json_array = json.load(input_file)
    coordinates = itertools.cycle(
        json_array['features'][0]['geometry']['coordinates']
    )
    bus = Bus(25, coordinates)
    bus.run()
