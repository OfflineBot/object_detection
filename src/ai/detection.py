
from typing import Tuple
from numpy.typing import NDArray
import torch.nn as nn
import torch.nn.functional as F

from numpy.typing import NDArray


class DetectionNN(nn.Module):

    def __init__(self, num_classes, num_objects):
        super().__init__()

        self.conv1 = nn.Conv2d(3, 16, kernel_size=3, stride=1, padding=1)
        self.conv2 = nn.Conv2d(16, 32, kernel_size=3, stride=1, padding=1)
        self.conv3 = nn.Conv2d(32, 64, kernel_size=3, stride=1, padding=1)
        self.conv4 = nn.Conv2d(64, 128, kernel_size=3, stride=1, padding=1)

        self.fc1 = nn.Linear(128 * 6 * 6, 1024)
        self.fc2 = nn.Linear(1024, 512)
        self.fc3_boxes = nn.Linear(512, num_objects * 4)
        self.fc3_classes = nn.Linear(512, num_classes * num_objects)

    def forward(self, x) -> Tuple[NDArray, NDArray]:
        x = F.relu(F.max_pool2d(self.conv1(x), 2))
        x = F.relu(F.max_pool2d(self.conv2(x), 2))
        x = F.relu(F.max_pool2d(self.conv3(x), 2))
        x = F.relu(F.max_pool2d(self.conv4(x), 2))

        x = x.view(x.size(0), -1)

        x = F.relu(self.fc1(x))
        x = F.relu(self.fc2(x))

        x_box = self.fc3_boxes(x)
        x_class = self.fc3_classes(x)

        return x_box, x_class


def object_detection_loss(box_fake, box_truth, class_fake, class_truth, box_weigth=1.0, class_weigth=1.0) -> float:
    box_loss = F.smooth_l1_loss(box_fake, box_truth)
    class_loss = F.cross_entropy(class_fake, class_truth)

    total_loss = box_weigth * box_loss + class_weigth * class_loss
    return total_loss.item()

