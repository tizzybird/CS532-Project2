#!/bin/bash
# 1. build docker image
IMG_NAME="532_project2:v1"
CMD=docker.exe
echo "=================================================================="
echo "======================== Building Image =========================="
echo "=================================================================="
$CMD build -t $IMG_NAME . --no-cache
# 2. initialize server container
echo "=================================================================="
echo "=============== Initializing Server Container ===================="
echo "=================================================================="
$CMD run --net=host -itd $IMG_NAME python server.py