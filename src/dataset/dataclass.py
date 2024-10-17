
from PIL.ImageFile import ImageFile
import numpy as np
from numpy.typing import NDArray
from dataclasses import dataclass
from typing import List
import json
import os
import matplotlib.pyplot as plt
from PIL import Image, ImageDraw
from torch import return_types

from ai.detection import NDArray


@dataclass
class Object:
    label: str
    image_path: str
    positions: List[List[float]]


class DataClass:

    def __init__(self, dataset_dir_path: str, absolute_json_path: str):
        self.path_to_json: str = absolute_json_path
        self.dataset_dir_path: str = dataset_dir_path
        self.objects: List[Object] = []
        self.length = 0

    # initialize objects from json file
    def init(self) -> None:
        with open(self.path_to_json, 'r') as file:
            json_data = json.load(file)
            dataset_list = json_data['dataset']
            for obj in dataset_list:
                new_obj = Object(obj['label'], obj['image'], obj['positions'])
                self.objects.append(new_obj)
                self.length += 1

    def print_objs(self) -> None:
        for obj in self.objects:
            print(f"Label: [{obj.label}] | Image: [{obj.image_path}]")

    def validate(self) -> None:
        for obj in self.objects:
            path = os.path.join(self.dataset_dir_path, obj.image_path)
            img = Image.open(path)
            draw = ImageDraw.Draw(img)
            for pos in obj.positions:
                x1, x2, y1, y2 = pos
                coords = (x1, x2, y1, y2)
                draw.rectangle(coords, outline='red', width=1)
            plt.imshow(img)
            plt.axis('off')
            plt.show(block=False)

            is_ok = input("Is ok? (y/n)> ")
            if is_ok == "y":
                plt.close()
                continue
            elif is_ok == "n":
                plt.close()
                print("something should be done now :)")
                continue
            else:
                print("unknown input. just skipping this image and closing it")
                plt.close()
                continue

    def get_image_value(self, image_path: str) -> NDArray[np.float32]:
        path: str = os.path.join(self.dataset_dir_path, image_path)
        img: ImageFile = Image.open(path)
        return np.array(img)

