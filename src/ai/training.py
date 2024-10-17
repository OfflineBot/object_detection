
from detection import DetectionNN, object_detection_loss
from dataset.dataclass import DataClass
import torch.optim as optim

def train(num_classes: int, num_objects: int, iterations: int, lr: float, dataset: DataClass) -> DetectionNN:
    model = DetectionNN(num_classes=num_classes, num_objects=num_objects)
    optimizer = optim.Adam(model.parameters(), lr=lr)

    for epoch in range(iterations):
        running_loss = 0.0
        if dataset.length <= 1:
            raise RuntimeError("No objects exist in dataset")
        
        for obj in dataset.objects:
            optimizer.zero_grad()
            box_fake, class_fake = model(dataset.get_image_value(obj.image_path).flatten())
            loss = object_detection_loss(box_fake, obj.positions, class_fake, obj.label)

        print(f"Iteration: [{epoch+1}/{iterations}] | Loss: [{running_loss / dataset.length}]")

    return model


