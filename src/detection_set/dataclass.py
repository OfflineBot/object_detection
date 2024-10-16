
from dataclasses import dataclass
from typing import List


@dataclass
class Object:
    label: str
    image_path: str
    positions: List[List[float]]


class DataClass:

    def __init__(self, path_to_json):
        self.path_to_json = path_to_json
        self.objects: List[Object]

    def init(self):
        print("TODO! (Load json from path_to_json to objects)")


