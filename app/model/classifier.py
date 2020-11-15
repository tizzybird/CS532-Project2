import torch
import torchvision.models as models
from torchvision import transforms
from PIL import Image

densenet = models.densenet161(pretrained=True)
densenet.eval()

transform = transforms.Compose([  # [1]
    transforms.Resize(256),  # [2]
    transforms.CenterCrop(224),  # [3]
    transforms.ToTensor(),  # [4]
    transforms.Normalize(  # [5]
        mean=[0.485, 0.456, 0.406],  # [6]
        std=[0.229, 0.224, 0.225]  # [7]
    )])

with open('labels.txt') as f:
  classes = [line.strip() for line in f.readlines()]


def classify(path):
    img = Image.open(path)
    img_t = transform(img)
    batch_t = torch.unsqueeze(img_t, 0)
    out = densenet(batch_t)

    maxval, index = torch.max(out, 1)
    percentage = torch.nn.functional.softmax(out, dim=1)[0] * 100
    return (classes[index[0]], percentage[index[0]].item())
