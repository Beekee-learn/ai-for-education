# Beekee AI Llama cpp & bitnet setup
A step-by-step guide to setting up **Llama.cpp** and **BitNet** on a Raspberry Pi 5 with 8GB RAM. This guide is designed to help you run AI models on a low-power, resource-constrained device, making it ideal for offline, edge applications.

## Table of Contents
- [Requirements](#requirements)
    - [Hardware](#hardware) 
- [Setup](#setup)
    - [Setup Llama.cpp](#install-llamacpp)
    - [Setup BitNet](#setup-bitnet)
- [Common Errors](#common-errors-and-troubleshooting)

## Requirements

We've used the follwing hardware components to run Llamacpp & Bitnet:
### Hardware
1. **Raspberry Pi 5 (8GB RAM)**  
   - This tutorial is designed for the Raspberry Pi 5 with 8GB of RAM to provide sufficient resources for model inference. Other versions of Raspberry Pi may experience limited performance or may not support the models.

2. **MicroSD Card (512GB or higher)**  
    - lower storage capacities can troubleshot the execution of AI models.

3. **Power Supply (USB-C, 5V 3A)**  

4. **Cooling Solution**  
   - Running AI models can be resource-intensive, which may cause the Raspberry Pi to heat up. A cooling fan or heatsink can help maintain optimal performance and avoid thermal throttling.

## Setup

### Setup Llama.cpp
1. **Install Raspberry Pi OS (64-bit Lite)**  
   Download and flash the Raspberry Pi OS (64-bit Lite) to your SD card.

2. **Connect via SSH**  
   Enable SSH to allow remote connection to your Raspberry Pi.

3. **Update System**  
   Run the following commands to update and upgrade your system:
   ```bash
   sudo apt-get update
   sudo apt-get upgrade

4. **Install packages needed**
    ```bash
    sudo apt-get install git git-lfs cmake clang
5. **Install llama cpp**
    ```bash
    git clone https://github.com/ggerganov/llama.cpp.git   

6. **Install models into /models folder**
    Download and place models in the /models directory. Ensure these are compatible with Llama.cpp (should be GGUF format).

### Setup BitNet (still some troubleshot running it)
1.  **Raspberry Pi OS (64-bit Lite)**
    Follow the steps above to install Raspberry Pi OS and connect via SSH.
2.  **System Update**
    Update your Raspberry Pi with:
    ```bash
    sudo apt-get update
    sudo apt-get upgrade
3.  **Install Required Packages for BitNet.**
    Install cmake and clang, as these are necessary for building BitNet:
    ```bash
    sudo apt-get install cmake clang
    sudo apt-get install libboost-all-dev libeigen3-dev
    sudo apt-get install python3 python3-pip
    pip3 install numpy
4.  **Build bitnet**
    ```bash
    mkdir build
    cd build
5.  **Complie using cmake**
    ```bash
    cmake ..
    make
6.  **Download pre-trained BitNet models and place them in a directory models/.**

## Common Errors and Troubleshooting

Setting up and running Llama.cpp and BitNet on a Raspberry Pi can involve various challenges. Here are some common errors and tips for troubleshooting:

1. `Out of Memory` Errors
- **Cause**: The Raspberry Pi may not have enough RAM to load large models.
- **Solution**: 
  - Try using a smaller, quantized version of the model (e.g., 4-bit or 8-bit quantized models).
  - Reduce the batch size or other resource-intensive parameters.
  - Monitor memory usage using `htop` or `free -h` to see if the system is hitting memory limits.

2. `Permission Denied` Errors
- **Cause**: This usually happens when attempting to execute commands without proper permissions.
- **Solution**: 
  - Use `sudo` before the command if it requires root privileges.
  - Ensure the directory or file permissions are set correctly. Use `chmod +x <filename>` to make files executable if needed.

3. `Command Not Found` Errors
- **Cause**: This can occur if a required package or tool is not installed, or if there’s a typo in the command.
- **Solution**:
  - Double-check that all necessary packages (`git`, `git-lfs`, `cmake`, `clang`, etc.) are installed.
  - Verify the command syntax.
  - Ensure the executable paths are correctly set, especially if you’re trying to run Llama.cpp or BitNet from a custom directory.

4. `Segmentation Fault` Errors
- **Cause**: A segmentation fault often occurs due to incorrect memory access, which can happen if the Raspberry Pi cannot handle the model’s size.
- **Solution**:
  - Ensure you’re using a model compatible with the Raspberry Pi’s ARM architecture.
  - Reduce model size by using quantized versions.
  - Restart the Raspberry Pi and free up memory by closing other applications before running the model.

5. `CMake Error: Could NOT find <library>` Errors
- **Cause**: This error can occur if certain libraries are missing or not correctly installed.
- **Solution**:
  - Ensure all dependencies are installed as listed in the requirements (`libboost-all-dev`, `libeigen3-dev`, etc.).
  - Run `sudo apt-get update` and `sudo apt-get upgrade` to ensure your package sources are up-to-date.
  - Double-check installation commands to verify that libraries are properly configured.

6. `git-lfs: command not found` Error
- **Cause**: Git LFS (Large File Storage) is required to download large model files but may not be installed by default.
- **Solution**:
  - Install Git LFS with `sudo apt-get install git-lfs` and not `git lfs install` first.
  - After installation, run `git lfs install` to initialize Git LFS for your environment.

7. `Unable to Load Model` or `File Not Found` Errors
- **Cause**: This often happens if the model file path is incorrect or if the model file did not download correctly.
- **Solution**:
  - Double-check the file path to ensure it matches the expected location.
  - Verify that the model file has been downloaded completely and is compatible with Llama.cpp or BitNet.
  - Ensure you’re using the correct model format (GGUF).

