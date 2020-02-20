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

  def _sigmoid(self, x):
    if not isinstance(x,np.ndarray): x = np.array(x)
    return 1/(1+np.exp(-x))

  def _deriv_sigmoid(self, sigm):
    return sigm*(1-sigm)

  def _weight_row(self, n):
    univec = np.random.uniform(0,1,n)
    return (univec/sum(univec))-(1/n)

  def forward(self):
    w1 = np.array([self._weight_row(self.X.shape[0]) for _ in range(self.X.shape[1])])    
    w2 = self._weight_row(self.y.shape[0]).reshape((self.y.shape[0],1))
    for c in range(10000):
      a1 = self._sigmoid(self.X @ w1)
      a2 = self._sigmoid(a1 @ w2)
      w1,w2,d1,d2 = self._backwards(w1, w2, a1, a2)
      if c%1000 == 0:
          print(self._calc_loss(a2))
          print(self._backwards_nv(w1, w2, a1, a2), d2)
    print(a2)
    
  def _backwards(self, w1, w2, a1, a2, n=1):
    # TODO: get a deeper understanding of backprop 
    # awesome resource: https://mattmazur.com/2015/03/17/a-step-by-step-backpropagation-example/
    l = self._deriv_loss(a2) * self._deriv_sigmoid(a2)
    d2 = a1 @ l #dE/dw2
    d1 = self.X.T @ ((l @ w2.T) * self._deriv_sigmoid(a1)) #dE/dw1
    uw2 = w2 - n * d2
    uw1 = w1 - n * d1
    return uw1,uw2,d1,d2

  def _backwards_nv(self, w1, w2, a1, a2, n=1):
      # backprop nonvector way
      dw2 = np.zeros(w2.shape)
      print(dw2.shape)
      for c,o in enumerate(a2):
          deda = self._deriv_loss(o)
          dadz = self._deriv_sigmoid(o)
          print(a1)
          for c1,o1 in enumerate(a1[c]):
              dw2[c,c1] = deda*dadz*o1
      print(dw2)
          

  def _calc_loss(self, o):
    return np.mean(np.sqrt((o-self.y)**2))

  def _deriv_loss(self, o):
    return 2*(o-self.y)

a = NN(X,y)
a.forward()
