import os
os.environ['KMP_DUPLICATE_LIB_OK']='True'

from dataset_temp import custom_dataset
import albumentations as A
from albumentations.pytorch import ToTensorV2
from torch.utils.data import DataLoader
import torch
import hy_parameter
from torchvision import models

# device
# 윈도우 기반 그래픽 카드 엔비디아 사용하고 계신경우
# device = torch.device("cuda" if torch.cuda.is_available else "cpu")
# m1 m2 칩셋 사용하시는분
device = torch.device('mps:0' if torch.backends.mps.is_available() else 'cpu')

# train aug
train_transform = A.Compose([
    A.Resize(height=224, width=224),
    ToTensorV2()
])
# val aug
val_transform = A.Compose([
    A.Resize(height=224, width=224),
    ToTensorV2()
])

# dataset
train_dataset = custom_dataset("./data/train", transform=train_transform)
val_dataset = custom_dataset("./data/val", transform=val_transform)

# dataloader
train_loader = DataLoader(train_dataset, batch_size=hy_parameter.batch_size, shuffle=True)
val_loader = DataLoader(val_dataset, batch_size=hy_parameter.batch_size, shuffle=False)

# model call
train_loader = DataLoader(train_dataset, batch_size=24,)