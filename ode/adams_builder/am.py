import numpy as np 
from ode.adams_builder import helper, ab

def _gen_ai(s):
  dp = np.array([1])
  a = [1]
  for i in range(1, s):
    dp = np.polymul(dp, [1, i-2])/i
    a.append(np.polyval(np.polyint(dp), 1) - np.polyval(np.polyint(dp),0))
  return a

def _builder(s):
  a = _gen_ai(s)
  pc = helper._pascal_triangle(s)
  p = np.array(a).dot(pc)
  def adams(f, xks, yks, ykj, h):
    xks = xks[-(s-1):]; yks = yks[-(s-1):]
    xks.append(xks[-1]+h)
    yks.append(ykj)
    dy = 0; yk = yks[-1]
    for i in range(0, s):
      dy = dy + p[s-i-1]*f(xks[i], yks[i])
    return yk + h*dy
  return [adams, p]

def solve(f, xk, yk, x, stepnum, s = 4):
  h = (x-xk)/stepnum
  xks = [xk]; yks = [yk]
  for i in range(0, s):
    am = _builder(s)[0]
    yk = ab(f, xks, yks, h)
    xk = xk + h
    xks.append(xk); yks.append(yk)
  for i in range(s, stepnum):
    yk = ab(f, xks, yks, h)
    xk = xk + h
    xks.append(xk); yks.append(yk)
  return [np.asarray(xks), np.asarray(yks)]
