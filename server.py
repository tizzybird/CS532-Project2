import torch
import torchvision.transforms as transforms

from flask import Flask, request, jsonify
from PIL import Image

import json, io

with open('config.json') as f:
    CONFIG = json.load(f)

# Used for mapping prediction to a corresponding class
imagenet_class_index = json.load(open('imagenet_class_index.json'))

model = torch.hub.load('pytorch/vision:v0.6.0', 'densenet121', pretrained=True)
model.eval()

app = Flask(__name__)

# Function for classifying the input image
# returns a class id and a name of animal
def predict(image_bytes):
    image = Image.open(io.BytesIO(image_bytes))
    transform_func = transforms.Compose([transforms.Resize(255),
                                        transforms.CenterCrop(224),
                                        transforms.ToTensor(),
                                        transforms.Normalize(
                                            [0.485, 0.456, 0.406],
                                            [0.229, 0.224, 0.225])])
    tensor = transform_func(image).unsqueeze(0)

    outputs = model.forward(tensor)
    _, y_hat = outputs.max(1)
    predicted_idx = str(y_hat.item())

    return imagenet_class_index[predicted_idx]

# Function for receiving HTTP requests
# if receiving a GET request, it returns 'no input image' message
# if receiving a POST request with an image appended in the 'image' field,
# it returns a class_id and a class_name including the name of the animal
# in the image
@app.route('/', methods=['POST', 'GET'])
def classify():
    print('Request is received!')
    res = {'message': 'no input image'}
    if request.method == 'POST':
        image = request.files['image']
        image_bytes = image.read()
        class_id, class_name = predict(image_bytes=image_bytes)
        res = {'class_id': class_id, 'class_name': class_name}
    
    return jsonify(res)


if __name__ == '__main__':
    app.run(host=CONFIG['addr'], port=CONFIG['port'])
