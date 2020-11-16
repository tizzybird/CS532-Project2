FROM python:3.7.9-buster
COPY server.py /
COPY imagenet_class_index.json /
COPY download_densenet.py /
RUN pip install flask
RUN pip install torch==1.7.0+cpu torchvision==0.8.1+cpu torchaudio==0.7.0 -f https://download.pytorch.org/whl/torch_stable.html
RUN python download_densenet.py