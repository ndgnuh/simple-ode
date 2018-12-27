from ode.adams_builder import am, ab
import numpy as np

def bashforth(f, xk, yk, x, stepnum, s = 4):
  h = (x-xk)/stepnum
  xks = [xk]
  yks = [yk]
  for i in range(0, s):
    abf = ab._builder(i+1)[0]
    yk = abf(f, xks, yks, h)
    xk = xk + h
    xks.append(xk); yks.append(yk)
  for i in range(s, stepnum):
    yk = abf(f, xks, yks, h)
    xk = xk + h
    xks.append(xk); yks.append(yk)
  return [np.asarray(xks), np.asarray(yks)]

def moulton(f, xk, yk, x, stepnum, s = 4, iterations = 50):
  h = (x-xk)/stepnum
  xks = [xk]
  yks = [yk]
  for i in range(0, s):
    abf = ab._builder(i+1)[0]
    amf = am._builder(i+1)[0]
    xk = xk + h; xks.append(xk)
    ykj = abf(f, xks, yks, h)
    yks.append(ykj)
    for j in range(0, iterations):
      yks[-1] = amf(f, xks, yks, h)
  for i in range(s, stepnum):
    xk = xk + h; xks.append(xk)
    ykj = abf(f, xks, yks, h)
    yks.append(ykj)
    for j in range(0, iterations):
      yks[-1] = amf(f, xks, yks, h)
  return [np.asarray(xks), np.asarray(yks)]