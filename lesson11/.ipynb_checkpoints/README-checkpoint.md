## Install
```bash

# INSIDED VSCODE
mkdir torch-tutorials
cd torch-tutorials

uv init --python 3.12
uv venv

source .venv/bin/activate 
# windows: .venv\Scripts\Activate.ps1

uv pip install torch=="2.2.0" torchvision torchaudio torch
uv add "numpy<2"

uv run python -c 'import torch; print(f"PyTorch version: {torch.__version__}")'


# INSIDE JUPYTER LAB/NOTEBOOK
%pip install torch torchvision torchaudio
%pip install "numpy<2"

import torch
import numpy as np

print("NumPy version:", np.__version__)
print("PyTorch version:", torch.__version__)
print("CUDA available:", torch.cuda.is_available())
print("CUDA available:", torch.mps.is_available())

# Create a tensor
x = torch.tensor([1, 2, 3, 4, 5])
print(x)

# Perform a calculation
print("Tensor multiplied by 2:", x * 2)

# Test conversion between PyTorch and NumPy
array = x.numpy()
print("NumPy array:", array)
```

## Introduction to PyTorch
 - What is PyTorch?
    - PyTorch is an open-source deep learning framework developed by Meta AI. It is widely used for:

- Machine Learning
- Deep Learning
- Computer Vision
- Natural Language Processing
- Research and Production AI Systems

### PyTorch is popular because it is:
- Easy to learn
- Pythonic
- Flexible
- Fast
- Great for experimentation

## Table of Contents
- Installing PyTorch
- Understanding Tensors
- Tensor Operations
- Working with GPU
- Autograd and Gradients
- Building Neural Networks
- Activation Functions
- Loss Functions
- Optimizers
- Training Loop
- Dataset and DataLoader
- Saving and Loading Models