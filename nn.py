# Let's solve the XOR problem with a simple neuralnet using SGD
# This can't be solved by "linear" means since there is no line 
# you can make which splits the F's and T's in two seperate groups
#
# keyword: breakingpoint
#
# T (0,1)     F (1,1) 
# -
# -
# F (0,0) - - T (0,1)
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

  def _sigmoid(self, x):
    if not isinstance(x,np.ndarray): x = np.array(x)
    return 1/(1+np.exp(-x))

  def _deriv_sigmoid(self, sigm):
    return sigm*(1-sigm)

  def _weight_row(self, n):
    univec = np.random.uniform(0,1,n)
    return (univec/sum(univec))-(1/n)

  def forward(self):
    #X::4x2 w1::4x2 w2::1x4 a1::4x4 a2::1x4
    w1 = np.array([self._weight_row(self.X.shape[1]) for _ in range(self.X.shape[0])])     
    w2 = self._weight_row(self.X.shape[0]).reshape((1,4))
    for c in range(10000):
      a1 = self._sigmoid(w1 @ self.X.T)
      a2 = self._sigmoid(a1 @ w2.T) # this is really a2.T :: 4x1
      w1,w2 = self._backwards(w1, w2, a1, a2)
      if c%1000 == 0:
         print(self._calc_loss(a2))
    print(a2)
    
  def _backwards(self, w1, w2, a1, a2, n=1e-1):
    d2 = (a1.T @ (self._deriv_loss(a2) * self._deriv_sigmoid(a2))).T
    d1 = ((self._deriv_loss(a2) * self._deriv_sigmoid(a2)) @ w2) @ self.X
    neww2 = w2 - n * d2
    neww1 = w1 - n * d1
    return neww1,neww2

  def _calc_loss(self, o):
    return np.mean(np.sqrt((self.y-o)**2))

  def _deriv_loss(self, x):
    return 2*(x-self.y)

a = NN(X,y)
a.forward()
