
from dataset.dataclass import DataClass

full_path_to_json = "/home/offlinebot/Coding/py/object_detection/dataset/data.json"
dataset_path = "/home/offlinebot/Coding/py/object_detection/dataset/"

x = DataClass(full_path_to_json)
x.init()
x.print_objs()
x.validate(dataset_path)

