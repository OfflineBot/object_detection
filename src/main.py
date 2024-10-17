
from dataset.dataclass import DataClass

full_path_to_json = "/home/offlinebot/Coding/py/object_detection/dataset/data.json"

x = DataClass(full_path_to_json)
x.init()
x.print_objs()
