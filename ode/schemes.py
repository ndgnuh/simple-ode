import numpy as np
import sys
sys.path.append('/home/hung/Projects/simple-ode')
from misc import rprint
ex_euler = lambda f, xk, yk, h: yk + h*np.asarray(f(xk, yk))
im_euler = lambda f, xk, xk1, yk, yk1, h: np.asarray(yk) + h*np.asarray(f(xk1, yk1))
trape = lambda f, xk, xk1, yk, yk1, h: np.asarray(yk) + h/2*(np.asarray(f(xk1, yk1))+np.asarray(f(xk, yk)))
"""

"""
def explicit(f, xk, yk, x, stepnum, exf):
  """Dùng phương pháp hiện để giải, exf là công thức phương pháp hiện
  """
  h = (x-xk)/stepnum
  yks = np.array([yk])
  xks = np.array([[xk]])
  for i in range(0, stepnum):
    yk = exf(f, xk, yk, h)
    xk = xk + h
    yks = np.append(yks, [yk], axis=0)
    xks = np.append(xks, xk)
  return [xks, yks]



f = lambda x, y: y
g = lambda x, y: [y[0],y[1]]

def rk4(f, xk, yk, h):
  k1 = f(xk, yk)
  k2 = f(xk+h/2, yk+h*k1/2)
  k3 = f(xk+h/2, yk+h*k2/2)
  k4 = f(xk+h, yk+h*k3)
  return yk + h*(k1+2*k2+2*k3+k4)/6

def implicit(f, xk, yk, x, stepnum, imf, exf = ex_euler, correct_time = 50):
  h = (x-xk)/stepnum
  yks = np.array([yk])
  xks = np.array([[xk]])
  for i in range(0, stepnum):
    ykj = exf(f, xk, yk, h)
    xk1 = xk + h
    for j in range(0, correct_time):
      ykj = imf(f, xk, xk1, yk, ykj, h)
    xk = xk1
    yk = ykj
    yks = np.append(yks, [yk], axis=0)
    xks = np.append(xks, xk)
  return [xks, yks]
  return 0

[x, y] = explicit(f, 0, 1, 4, 4, ex_euler)
[x1, y1] = explicit(g, 0, [1,1], 4, 4, ex_euler)
from trapezoidal import trapezoidal

[x2, y2] = implicit(g, 0, [1,1], 4, 7, trape)
rprint.result(x2, y2)
[x3, y3] = trapezoidal(g, 0, [1,1], 4, 7)
rprint.result(x3, y3)