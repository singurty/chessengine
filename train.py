#!/usr/bin/env python3

from torch.utils.data import Dataset
import numpy as np
import torch.nn as nn
import torch.nn.functional as F

class ChessValueDataset(Dataset):
    def __init__(self):
        dat = np.load('processed/dataset_1M.npz')
        self.X = dat['arr_0']
        self.Y = dat['arr_1']
        print("loaded", self.X.shape, self.Y.shape)

    def __len__(self):
        return self.X.shape[0]

    def __getitem__(self, idx):
        return {'X': self.X[idx], 'Y': self.Y[idx]}

chess_dataset = ChessValueDataset()

class Net(nn.Module):
    def __init__(self):
        super(Net, self).__init__()

    def forward(self, x):
        x = F.relu(nn.Conv2d(5, 16, kernel_size=3))
        x = F.relu(nn.Conv2d(16, 16, kernel_size=3))
