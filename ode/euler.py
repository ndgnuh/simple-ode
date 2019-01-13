import numpy as np

def ex_euler(f, xk, yk, h):
  return np.asarray(yk) + h*np.asarray(f(xk, yk))

def im_euler(f, xk, yk, h, exf, iters):
  ykj = exf(f, xk, yk, h)
  xknext = xk + h
  for j in range(0, iters):
    ykj = np.asarray(yk) + h*np.asarray(f(xknext, ykj))
  return ykj

def im_euler_sub(f, xk, yk, h):
  return lambda y: y - h*f(xk+h, y) - yk