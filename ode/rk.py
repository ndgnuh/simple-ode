import numpy as np
from scipy.optimize import newton 

def erk4(f, xk, yk, h):
  k1 = np.asarray(f(xk, yk))
  k2 = np.asarray(f(xk+h/2, yk+h*k1/2))
  k3 = np.asarray(f(xk+h/2, yk+h*k2/2))
  k4 = np.asarray(f(xk+h, yk+h*k3))
  return np.asarray(yk) + h*(k1+2*k2+2*k3+k4)/6

def erk3(f, xk, yk, h):
  k1 = np.asarray(f(xk, yk))
  k2 = np.asarray(f(xk+h/2, yk+h*k1/2))
  k3 = np.asarray(f(xk+1, yk-h*k1+2*h*k2))
  return np.asarray(yk) + h*(k1/6+2*k2/3+k3/6)
  
def irk3(f, xk, yk, h, exf, iters):
  ykj_half = exf(f, xk, yk, h/2)
  xkj_half = xk + h/2
  for i in range(0, iters):
    ykj_half = np.asarray(yk) + h*np.asarray(f(xkj_half, ykj_half))/2
  ykj = exf(f, xk, yk, h)
  xkj = xk + h
  for i in range(0, iters):
    ykj = np.asarray(yk) + h*(np.asarray(f(xkj, ykj)) + np.asarray(f(xk,yk)) + 4*np.asarray(f(xkj_half, ykj_half)))/6
  return ykj

def irk3_sub(f, xk, yk, h):
  xk_half = xk + h/2
  yk_half = newton(lambda y: y - yk - h/2*f(xk_half, y), yk)
  return lambda y: y - yk - h*f(xk + h, y)
