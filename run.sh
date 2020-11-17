#!/bin/bash
# 1. build docker image
IMG_NAME="532_project2:v1"
CMD=docker.exe
SERVER_ADDR=http://localhost:5000/
echo "=================================================================="
echo "================== 1. Building Docker Image ======================"
echo "=================================================================="
$CMD build -t $IMG_NAME . --no-cache
# 2. initialize server container
echo "=================================================================="
echo "=============== 2. Initializing Server Container ================="
echo "=================================================================="
$CMD run --net=host -itd $IMG_NAME python server.py
# 3. test
echo "=================================================================="
echo "=========================== 3. Test =============================="
echo "=================================================================="
for filename in data/*; do
    echo "Sending $filename to $SERVER_ADDR"
    curl -i -X POST -F "image=@$filename" $SERVER_ADDR
    echo "=================================================================="
done