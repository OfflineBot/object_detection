
from dataset.dataclass import DataClass
from ai.training import train

full_path_to_json = "/home/offlinebot/Coding/py/object_detection/dataset/data.json"
dataset_path = "/home/offlinebot/Coding/py/object_detection/dataset/"

x = DataClass(dataset_path, full_path_to_json)
x.init()
x.print_objs()

train(2, 2, 100, 0.01, x)
