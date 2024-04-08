from functools import reduce
from operator import __add__
from torch import device, flatten
from torch.cuda import is_available as is_cuda_available
from torch.backends.mps import is_available as is_mps_available
from torch.nn import (Sequential, Conv2d, LazyLinear, MaxPool2d, LazyBatchNorm1d,
                      LazyBatchNorm2d, LazyBatchNorm3d, LazyConv2d, Dropout,
                      ReLU, Softmax, Module)

CLASSES = ('plane', 'car', 'bird', 'cat', 'deer', 'dog', 'frog', 'horse', 'ship', 'truck')
N_CLASS = len(CLASSES)

class AlgaeCNN(Module):
    # Input
    def __init__(self):
        super(AlgaeCNN, self).__init__()
        
        self.device = device("mps" if is_mps_available() else "cuda" if is_cuda_available() else "cpu")
        
        self.conv1 = self.conv_layer(in_channels = 3,
                                     out_channels = 64,
                                     conv_padding = 0,
                                     pool_stride = 2,
                                     first = True)
        
        self.conv2 = self.conv_layer(out_channels = 64,
                                     conv_padding = 2,
                                     pool_stride = 1)

        self.conv3 = self.conv_layer(out_channels = 128,
                                     conv_padding = 2,
                                     pool_stride = 1)
        
        self.drop = Dropout(0.1)

        self.den1 = self.dense_layer(out_features = 1024)
        self.den2 = self.dense_layer(out_features = 1024)
        self.den3 = self.dense_layer(out_features = N_CLASS)
        
    def batch_norm(self, momentum, epsilon, dim):
        if dim == 1: return LazyBatchNorm1d(momentum = momentum, device = self.device, eps = epsilon)
        elif dim == 2: return LazyBatchNorm2d(momentum = momentum, device = self.device, eps = epsilon)
        else: return LazyBatchNorm3d(momentum = momentum, device = self.device, eps = epsilon)

    def pooling(self, stride, pool_padding, pool_size):
        return MaxPool2d(kernel_size = pool_size, stride = stride, padding = pool_padding)

    def padding(self, kernel_sizes):
        conv_padding = reduce(__add__, 
            [(k // 2 + (k - 2 * (k // 2)) - 1, k // 2) for k in kernel_sizes[::-1]])
        # pad = ZeroPad2d(conv_padding)
        return conv_padding

    def conv_layer(self,
                   out_channels,
                   conv_padding,
                   pool_stride,
                   conv_stride = 2,
                   pool_padding = 1,
                   pool_size = 3,
                   kernel_size = 5,
                   momentum = 0.9,
                   epsilon = 0.001,
                   first = False,
                   **kwargs):
        if first: conv = Conv2d(out_channels = out_channels,
                                kernel_size = kernel_size,
                                stride = conv_stride,
                                padding = conv_padding,
                                device = self.device,
                                **kwargs)

        else: conv = LazyConv2d(out_channels = out_channels,
                                kernel_size = kernel_size,
                                padding = conv_padding,
                                stride = conv_stride,
                                device = self.device,
                                **kwargs)
    
        return Sequential(conv,
                          ReLU(inplace = True),
                          
                          self.pooling(pool_padding = pool_padding, stride = pool_stride, pool_size = pool_size),
                          
                          self.batch_norm(momentum = momentum, epsilon = epsilon, dim = 2))

    def dense_layer(self,
                    out_features,
                    momentum = 0.9,
                    epsilon = 0.001,
                    last = False):
        initial = Sequential(LazyLinear(out_features = out_features, device = self.device),
                             Softmax(dim = 1) if last else ReLU(inplace = True))

        # TODO Fix (used to be batch_norm2d)
        if last: return initial
        
        return Sequential(initial, self.batch_norm(momentum = momentum, epsilon = epsilon, dim = 1))

    def features(self, x):
        x = self.conv1(x)
        x = self.conv2(x)
        x = self.conv3(x)
        
        x = self.drop(x)
        return x

    def classifier(self, x):
        x = self.den1(x)
        x = self.den2(x)
        x = self.den3(x)
        return x
    
    def forward(self, x):
        x = self.features(x)
        
        # Pytorch rep: (Batch, Channel, Height, Width) for conv
        # (Batch, # feats) for linear/dense
        # TODO Fix
        x = flatten(x, 1) # flatten all dimensions except batch

        x = self.classifier(x)
        return x