# (2020 Fall) CS532 - Project 2

## Contents
**Source code**
- server.py: backend server code
- download_densenet.py: script for downloading Densenet-121
- imagenet_class_index.json: json file for mapping index to animal class

**Config files**
- config.json: server config file
- Dockerfile: file for building Docker image

**Script**
- run.sh

**Test files**
- data/: please upload your custom test images under this folder

**Documentation**
- Design Report.pdf
- README.md

----
## Setup instructions
Please make sure that below 3 variables in `run.sh` are properly set:
- **IMG_NAME**: the name of the Docker image. By default, it is "cs532_project2:v1"
- **CMD**: the path of Docker command. By default, it is "docker.exe" since my OS environment is Windows. You might need to change it to "docker" under Linux.
- **SERVER_ADDR**: the URL of the backend server (default: http://localhost:5000). Make sure that this address and port number are available and the same as the values in `config.json`.

In addition, if you are using "Docker Toolbox for Windows" for running docker service, you might need to set port forwarding rules on the default Docker virtual machine. Please follow the instructions in section **4. Running the program** of `Design Report.pdf`

The `run.sh` script contains 3 parts:
1. Building a Docker image according to `Dockerfile`
2. Initiating a Docker container based on the previously built Docker image.
3. Sending test requests by looping over all images under folder `data/`. If you want to use your custom pictures for test, please upload them under this folder.

You should be able to run the whole program by executing `./run.sh` command. If you want to skip some steps, simply comment out the corresponding lines.

You can also download built Docker image of this project by executing: `docker pull tizzybird/cs532_project2:v1`. (Notice that the backend server URL in this image is http://localhost:5000)