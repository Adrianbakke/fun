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
      w1,w2 = self._backwards(w1, w2, a1, a2)
      if c%1000 == 0: print("loss: ", self._calc_loss(a2))
    print("predictions: ", a2.T[0])
    
  def _backwards(self, w1, w2, a1, a2, n=1):
    # TODO: get a deeper understanding of backprop 
    # awesome resource: https://mattmazur.com/2015/03/17/a-step-by-step-backpropagation-example/
    l = self._deriv_loss(a2) * self._deriv_sigmoid(a2)
    d2 = a1.T @ l #dE/dw2
    d1 = self.X.T @ ((l @ w2.T) * self._deriv_sigmoid(a1)) #dE/dw1
    uw2 = w2 - n * d2
    uw1 = w1 - n * d1
    return uw1,uw2

  def _calc_loss(self, o):
    return np.mean(np.sqrt((o-self.y)**2))

  def _deriv_loss(self, o, c=None):
    if not c is None: return 2*(o-self.y[c][0])
    return 2*(o-self.y)

class NN2:
  def __init__(self, X, y):
    self.X = X
    self.y = y
  
  def _forward(self, x, ws):
    a = []
    for w in ws:
      x = self._sigmoid(w @ x)
      a.append(x)
    return a 

  def backpropagation(self):
    w1 = np.random.random((2,2))
    w2 = np.random.random(2)
    ws = [w1,w2]
    for c in range(10000):
      dedw2 = np.zeros(w2.shape)
      dedw1 = np.zeros(w1.shape)
      for sample_num,x in enumerate(self.X):
        a = self._forward(x.reshape(2,1),ws)
        delta = self._deriv_loss(a[-1][0], self.y[sample_num][0]) * self._deriv_sigmoid(a[-1][0])
        for i in range(len(ws[-1])): 
          dedw2[i] += delta * a[-2][i][0]
          delta2 = delta * ws[-1][i] * self._deriv_sigmoid(a[-2][i][0])
          for n in range(len(ws[-2])):
            dedw1[i][n] +=  delta2 * x[n]
      ws[-1] = ws[-1] - dedw2
      ws[-2] = ws[-2] - dedw1
      if c%1000==0: print("loss: ",self._loss(np.array([self._sigmoid(ws[-1]@(self._sigmoid(ws[-2]@self.X.T)))]).T))
    print("predictions:", self._sigmoid(ws[-1]@(self._sigmoid(ws[-2]@self.X.T))))

  def _sigmoid(self, x):
    return 1/(1+np.exp(-x))

  def _deriv_sigmoid(self, x):
    return x*(1-x)

  def _loss(self, o):
    return np.mean(np.sqrt((o-self.y)**2))

  def _deriv_loss(self, o, y):
    return 2*(o-y)
  
print("linalg way")
a = NN(X,y)
a.forward()
print()
print("loopy way")
a = NN2(X,y)
a.backpropagation()
