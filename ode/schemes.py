import numpy as np 
from ode.rk import erk4

def explicit(f, xk, yk, x, stepnum, exf):
  """Dùng phương pháp hiện để giải, exf là công thức phương pháp hiện
  """
  h = (x-xk)/stepnum
  yks = np.array([yk])
  xks = np.array([xk])
  for i in range(0, stepnum):
    yk = exf(f, xk, yk, h)
    xk = xk + h
    yks = np.append(yks, [yk], axis=0)
    xks = np.append(xks, xk)
  return [xks, yks]

def implicit(f, xk, yk, x, stepnum, imf, exf = erk4, correct_time = 50):
  h = (x-xk)/stepnum
  yks = np.array([yk])
  xks = np.array([xk])
  for i in range(0, stepnum):
    yk = exf(f, xk, yk, h)
    xk = xk + h
    yks = np.append(yks, [yk], axis=0)
    xks = np.append(xks, xk)
    for j in range(0, correct_time):
      yks[-1] = imf(f, xks, yks, h)
  print(yks)
  return [xks, yks]
