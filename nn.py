# Let's solve the XOR problem with a simple neuralnet using SGD
# This can't be solved by "linear" means since there is no line 
# you can make which splits the F's and T's in two seperate groups
#
# keyword: breakingpoint
#
# T (0,1)     F (1,1) 
# -
# -
# F (0,0) - - T (0, 1)
#

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
  def __init__(self, X, y):
    self.X = X
    self.y = y

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

  def forward(self):
    fst_w = np.array([self._weight_row(self.X.shape[0]) for _ in range(self.X.shape[1])])     
    snd_w = self._weight_row(self.X.shape[0]).reshape((1,4)).T
    for c in range(1000):
      fst = self._sigmoid(self.X@fst_w)
      snd = self._sigmoid(fst@snd_w)
      fst_w,snd_w = self._backwards(fst_w, snd_w, snd)
      if c%100 == 0: print(self._calc_loss(snd))

  def _backwards(self, w1, w2, op, n=1e-3):
    d1 = self._deriv_loss(op) * self._sigmoid(w2, deriv=True)
    d2 = d1 * self._sigmoid(w1, deriv=True)
    neww1 = w1 - n * d1
    neww2 = w2 - n * d2
    return neww1,neww2

  def _calc_loss(self, res):
    return np.mean(np.sqrt((res-self.y)**2))

  def _deriv_loss(self, x):
    return 2*(x-self.y) 
 
a = NN(X,y)
a.forward()

