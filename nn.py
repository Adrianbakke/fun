import numpy as np
import torch
import matplotlib.pyplot as plt

X = np.array([
    [0,0],
    [0,1],
    [1,0],
    [1,1]
    ])

y = np.array([0,1,1,0]).reshape((1,4)).T

class NN:
    def __init__(self):
        pass    

    def _relu(self, x, deriv=False):
        if not isinstance(x,np.ndarray): x = np.array(x)
        if deriv:
            x[x<=0] = 0
            x[x>0] = 1
        else: x[x<=0] = 0
        return x

    def _sigmoid(self, x, deriv=False):
        if not isinstance(x,np.ndarray): x = np.array(x)
        x = 1/(1+np.exp(-x))
        if deriv: x = x*(1-x)
        return x

    def _weight_row(self, n):
        univec = np.random.uniform(0,1,n)
        return (univec/sum(univec))-(1/n)

    def forward(self, X):
        fst_w = np.array([self._weight_row(X.shape[0]) for _ in range(X.shape[1])])     
        snd_w = _weight_row.reshape((1,4)).T
        for x in range(1000):
            fst = self._sigmoid(X@fst_w)
            snd = self._sigmoid(fst@snd_w)
            fst_w,snd_w = self._backwards
        
    def _backwards(self, w1, w2, res, ans):
        loss = self._calc_loss(res,ans)

    def _calc_loss(self, res, ans):
        return np.mean(np.sqrt((res-ans)**2))

