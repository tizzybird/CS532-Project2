# Download densenet model

import torch

model = torch.hub.load('pytorch/vision:v0.6.0', 'densenet121', pretrained=True)
model.eval()