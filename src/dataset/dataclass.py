
from dataclasses import dataclass
from typing import List


@dataclass
class Object:
    label: str
    image_path: str
    positions: List[List[float]]


class DataClass:

    def __init__(self, absolute_json_path):
        self.path_to_json = absolute_json_path
        self.objects: List[Object]

    # initialize objects from json file
    def init(self) -> None:
        print("TODO! (Load json from path_to_json to objects)")

    def validate(self) -> None:
        print("TODO! (open image and check if correct)")

