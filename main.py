from custom_dataset import customDataset
import torch
import torchvision
import albumentations as A
from ana.pytorch.transforms import ToTensorV2
from torch.utils.data import DataLoader

device = torch.device('cuda' if (torch.cuda.is_available()) else 'cpu')

# Augmentation
train_transform = A.Compose([
    A.GaussianBlur(p=0.3),
    A.RandomShadow(p=0.5),
    A.RandomRain(p=0.3),
    A.RandomBrightnessContrast(p=0.5),
    A.Normalize(mean=(0.485, 0.456, 0.406), std=(0.229, 0.224, 0.225)),
    ToTensorV2()
])

val_transform = A.Compose([
    A.Normalize(mean=(0.485, 0.456, 0.406), std=(0.229, 0.224, 0.225)),
    ToTensorV2()
])

test_transform = A.Compose([
    A.Normalize(mean=(0.485, 0.456, 0.406), std=(0.229, 0.224, 0.225)),
    ToTensorV2()
])

# dataset
train_dataset = customDataset('./dataset/train', transfrom=train_transform)
val_dataset = customDataset('./dataset/val', transfrom=val_transform)
test_dataset = customDataset('./dataset/test', transfrom=test_transform)

# dataloader
train_loader = DataLoader(train_dataset, batch_size=64, shuffle=True)
val_loader = DataLoader(val_dataset, batch_size=64, shuffle=False)
test_loader = DataLoader(test_dataset, batch_size=1, shuffle=False)

# model call


'''
1. resnet50
2. vgg
3. mobile-net
4. swin_t
'''