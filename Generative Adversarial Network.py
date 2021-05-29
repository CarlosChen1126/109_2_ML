# -*- coding: utf-8 -*-
"""hw6_GAN.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1V9X92YePiOUa2hA3FLJv1cMhfu99ZmIG

# **Homework 6 - Generative Adversarial Network**

This is the example code of homework 6 of the machine learning course by Prof. Hung-yi Lee.


In this homework, you are required to build a generative adversarial  network for anime face generation.

## Set up the environment

### Packages Installation
"""

# You may replace the workspace directory if you want.
workspace_dir = '.'

# Training progress bar
!pip install -q qqdm

"""### Download the dataset
**Please use the link according to the last digit of your student ID first!**

If all download links fail, please follow [here](https://drive.google.com/drive/folders/13T0Pa_WGgQxNkqZk781qhc5T9-zfh19e).

* To open the file using your browser, use the link below (replace the id first!):
https://drive.google.com/file/d/REPLACE_WITH_ID
* e.g. https://drive.google.com/file/d/1IGrTr308mGAaCKotpkkm8wTKlWs9Jq-p
"""

!nvidia-smi

!gdown --id 1sc1sLsvlnHEgAPXmcKX8b-5GY_ZlvhDJ --output "./crypko_data.zip"

# Other download links
#   Please uncomment the line according to the last digit of your student ID first

# 0
# !gdown --id 131zPaVoi-U--XThvzgRfaxrumc3YSBd3 --output "{workspace_dir}/crypko_data.zip"

# 1
# !gdown --id 1kCuIj1Pf3T2O94H9bUBxjPBKb---WOmH --output "{workspace_dir}/crypko_data.zip"

# 2
# !gdown --id 1boEoiiqBJwoHVvjmI0xgoutE9G0Rv8CD --output "{workspace_dir}/crypko_data.zip"

# 3
# !gdown --id 1Ic0mktAQQvnNAnswrPHsg-u2OWGBXTWF --output "{workspace_dir}/crypko_data.zip"

# 4
# !gdown --id 1PFcc25r9tLE7OyQ-CDadtysNdWizk6Yg --output "{workspace_dir}/crypko_data.zip"

# 5
# !gdown --id 1wgkrYkTrhwDSMdWa5NwpXeE4-7JaUuX2 --output "{workspace_dir}/crypko_data.zip"

# 6
# !gdown --id 19gwNYWi9gN9xVL86jC3v8qqNtrXyq5Bf --output "{workspace_dir}/crypko_data.zip"

# 7 
# !gdown --id 1-KPZB6frRSRLRAtQfafKCVA7em0_NrJG --output "{workspace_dir}/crypko_data.zip"

# 8
# !gdown --id 1rNBfmn0YBzXuG5ub7CXbsGwduZqEs8hx --output "{workspace_dir}/crypko_data.zip"

# 9
# !gdown --id 113NEISX-2j6rBd1yyBx0c3_9nPIzSNz- --output "{workspace_dir}/crypko_data.zip"

"""###Unzip the downloaded file.
The unzipped tree structure is like 
```
faces/
├── 1.jpg
├── 2.jpg
├── 3.jpg
...
```
"""

!unzip -q "./crypko_data.zip" -d "./"

"""## Random seed
Set the random seed to a certain value for reproducibility.
"""

import random

import torch
import numpy as np


def same_seeds(seed):
    # Python built-in random module
    random.seed(seed)
    # Numpy
    np.random.seed(seed)
    # Torch
    torch.manual_seed(seed)
    if torch.cuda.is_available():
        torch.cuda.manual_seed(seed)
        torch.cuda.manual_seed_all(seed)
    torch.backends.cudnn.benchmark = False
    torch.backends.cudnn.deterministic = True

same_seeds(2021)

!pip install stylegan2_pytorch

!stylegan2_pytorch --data ./faces

"""## Import Packages
First, we need to import packages that will be used later.

Like hw3, we highly rely on **torchvision**, a library of PyTorch.
"""

import os
import glob

import torch.nn as nn
import torch.nn.functional as F
import torchvision
import torchvision.transforms as transforms
from torch import optim
from torch.autograd import Variable
from torch.utils.data import Dataset, DataLoader
import matplotlib.pyplot as plt
from qqdm.notebook import qqdm

"""## Dataset
1. Resize the images to (64, 64)
1. Linearly map the values from [0, 1] to  [-1, 1].

Please refer to [PyTorch official website](https://pytorch.org/vision/stable/transforms.html) for details about different transforms.

### Show some images
Note that the values are in the range of [-1, 1], we should shift them to the valid range, [0, 1], to display correctly.

## Model
Here, we use DCGAN as the model structure. Feel free to modify your own model structure.

Note that the `N` of the input/output shape stands for the batch size.

## Training

### Initialization
- hyperparameters
- model
- optimizer
- dataloader

### Training loop
We store some pictures regularly to monitor the current performance of the Generator, and regularly record checkpoints.

## Inference
Use the trained model to generate anime faces!

### Load model

### Generate and show some images.

### Compress the generated images using **tar**.
"""

import torch
from torchvision.utils import save_image
from stylegan2_pytorch import ModelLoader

os.makedirs('output', exist_ok=True)
loader = ModelLoader(
    base_dir = './',   # path to where you invoked the command line tool
    name = 'default'                   # the project name, defaults to 'default'
)

for i in range(1000):
  noise   = torch.randn(1, 512).cuda() # noise
  styles  = loader.noise_to_styles(noise, trunc_psi = 0.01)  # pass through mapping network
  images  = loader.styles_to_images(styles) # call the generator on intermediate style vectors
  images = torch.nn.functional.interpolate(images, size=64)
  save_image(images, f'output/{i+1}.jpg') # save your images, or do whatever you desire

# Commented out IPython magic to ensure Python compatibility.
# %cd output
!tar -zcf ../images.tgz *.jpg
# %cd ..

#delete ./output and images.tgz(if needed)
!rm -r ./output
!rm images.tgz