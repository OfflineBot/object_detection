
from dataclasses import dataclass
from typing import List
import json


@dataclass
class Object:
    label: str
    image_path: str
    positions: List[List[float]]


class DataClass:

    def __init__(self, absolute_json_path):
        self.path_to_json = absolute_json_path
        self.objects: List[Object] = []

    # initialize objects from json file
    def init(self) -> None:
        with open(self.path_to_json, 'r') as file:
            json_data = json.load(file)
            dataset_list = json_data['dataset']
            for obj in dataset_list:
                new_obj = Object(obj['label'], obj['image_path'], obj['positions'])
                self.objects.append(new_obj)

    def print_objs(self) -> None:
        for obj in self.objects:
            print(f"Label: [{obj.label}] | Image: [{obj.image_path}]")

    def validate(self) -> None:
        print("TODO! (open image and check if correct)")


