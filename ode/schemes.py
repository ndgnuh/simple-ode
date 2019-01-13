import numpy as np 
from ode.rk import erk4
from scipy.optimize import newton

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
  """
  Dùng phương pháp ẩn để giải (dự đooán hiệu chỉnh)
  """
  h = (x-xk)/stepnum
  yks = np.array([yk])
  xks = np.array([xk])
  for i in range(0, stepnum):
    yk = imf(f, xk, yk, h, exf, correct_time)
    xk = xk + h
    yks = np.append(yks, [yk], axis=0)
    xks = np.append(xks, xk)
  return [xks, yks]

def implicit_newton(f, xk, yk, x, stepnum, imsf):
  """
  Dùng phương pháp ẩn để giải với pp newton (dự đooán hiệu chỉnh)
  """
  h = (x-xk)/stepnum
  yks = np.array([yk])
  xks = np.array([xk])
  for i in range(0, stepnum):
    yk = newton(imsf(f, xk, yk, h), yk)
    xk = xk + h
    yks = np.append(yks, [yk], axis=0)
    xks = np.append(xks, xk)
  return [xks, yks]