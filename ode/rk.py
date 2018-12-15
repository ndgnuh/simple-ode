import numpy as np

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
  
"""  
def rk4(f, xk, yk, x, stepnum):
  h = (x - xk)/stepnum
  yks = [yk]
  xks = [xk]
  print("xk", "".ljust(5), "yk", "".ljust(25))
  print(str(np.round(xk,3)).ljust(5) , " | ", str(yk).ljust(25))
  for i in range(0, stepnum):
    k1 = f(xk, yk)
    k2 = f(xk+h/2, yk+h*k1/2)
    k3 = f(xk+h/2, yk+h*k2/2)
    k4 = f(xk+h, yk+h*k3)
    yk = yk + h*(k1+2*k2+2*k3+k4)/6
    xk = xk+h
    print(str(np.round(xk,3)).ljust(5) , " | ", str(yk).ljust(25))
    xks.append(xk)
    yks.append(yk)
  return [np.asarray(xks), np.asarray(yks)]

def rk2(f, xk, yk, x, stepnum):
  h = (x - xk)/stepnum
  yks = [yk]
  xks = [xk]
  print("xk", "".ljust(5), "yk", "".ljust(25))
  print(str(np.round(xk,3)).ljust(5) , " | ", str(yk).ljust(25))
  for i in range(0, stepnum):
    k1 = f(xk, yk)
    k2 = f(xk+h/2, yk+h*k1/2)
    yk = yk + h*k2
    xk = xk+h
    print(str(np.round(xk,3)).ljust(5) , " | ", str(yk).ljust(25))
    xks.append(xk)
    yks.append(yk)
  return [np.asarray(xks), np.asarray(yks)]


def rk3(f, xk, yk, x, stepnum):
  h = (x - xk)/stepnum
  yks = [yk]
  xks = [xk]
  print("xk", "".ljust(5), "yk", "".ljust(25))
  print(str(np.round(xk,3)).ljust(5) , " | ", str(yk).ljust(25))
  for i in range(0, stepnum):
    k1 = f(xk, yk)
    k2 = f(xk+h/2, yk+h*k1/2)
    k3 = f(xk+1, yk-h*k1+2*h*k2)
    yk = yk + h*(k1/6+2*k2/3+k3/6)
    xk = xk+h
    print(str(np.round(xk,3)).ljust(5) , " | ", str(yk).ljust(25))
    xks.append(xk)
    yks.append(yk)
  return [np.asarray(xks), np.asarray(yks)]


def fehlberg(f, xk, yk, x, stepnum):
  h = (x - xk)/stepnum
  xks = [xk]
  yks = [yk]
  for i in range(0, stepnum):
    k1 = h*f(xk, yk)
    k2 = h*f(xk + h/4, yk+k1/4)
    k3 = h*f(xk + 3*h/8, yk+ 3*k1/32+9*k2/32)
    k4 = h*f(xk + 12*h/12, yk+1932*k1/2197-7200*k2/2197+7296*k3/2197)
    k5 = h*f(xk + h, yk+439*k1/216-8*k2+3680*k3/513-845*k4/4104)
    k6 = h*f(xk + h/2, yk-8*k1/27+2*k2-3544*k3/2565+1859*k4/4104-11*k5/40)
    yk = yk + 16*k1/135+6656*k3/12825+28561*k4/56430-9*k5/50+2*k6/55
    xk = xk + h
    xks.append(xk)
    yks.append(yk)
    print(str(np.round(xk,3)).ljust(5) , " | ", str(yk).ljust(25))
  return [np.asarray(xks), np.asarray(yks)]
"""