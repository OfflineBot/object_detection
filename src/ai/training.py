
from ai.detection import DetectionNN, object_detection_loss
from dataset.dataclass import DataClass
import torch
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
            input_data = dataset.get_image_value(obj.image_path)
            input_tensor = torch.tensor(input_data, dtype=torch.float32)
            input_tensor = input_tensor.permute(2, 0, 1).unsqueeze(0)
            print(input_tensor.shape)
            box_fake, class_fake = model(input_tensor)
            label_num = -1
            if obj.label == "none":
                label_num = 0
            elif obj.label == "circle":
                label_num = 1
            else: 
                label_num = 2

            obj_position_tensor = torch.tensor(obj.positions, dtype=torch.float32)
            obj_label_tensor = torch.tensor(label_num, dtype=torch.float32)
            
            print("box_fake: ", box_fake)
            loss: float = object_detection_loss(box_fake, obj_position_tensor, class_fake, obj_label_tensor)
            running_loss += loss

        print(f"Iteration: [{epoch+1}/{iterations}] | Loss: [{running_loss / dataset.length}]")

    return model
