import numpy as np 
import ab as bashforth
import sys
sys.path.append("/home/hung/Projects/simple-ode")
from misc import rprint

def moulton_builder(s):
  def moulton(f, xks, yks, h):
    xks = xks[:s]; yks = yks[:s]
    return yks[-1]
  return moulton

def adams_moulton(f, xk, yk, x, stepnum, s = 4, correctors = 50):
  xks = [xk]; yks = [yk]
  h = (x - xk)/stepnum
  for i in range(0, s):
    ab = bashforth.ab_builder(i+1)
    am = moulton_builder(i+1)
    ykj = yk + ab(f, xks, yks, h)
    xk = xk + h
    yks.append(ykj); xks.append(xk)
    for j in range(0, correctors):
      ykj = yk + am(f, xks, yks, h)
    yks[-1] = ykj
  return [np.asarray(xks), np.asarray(yks)]


s = int(input("s = "))
f = lambda x,y: 1-y
[x, y] = adams_moulton(f, 0, 0,3,9, s)
rprint.result(x,y,12)