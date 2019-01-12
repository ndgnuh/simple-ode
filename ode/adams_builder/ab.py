import numpy as np
from ode.adams_builder import helper

def _gen_ai(s):
  dp = np.array([1])
  a = [1]
  for i in range(1, s):
    dp = np.polymul(dp, [1, i-1])/i
    a.append(np.polyval(np.polyint(dp), 1) - np.polyval(np.polyint(dp),0))
  return a

def _builder(s):
  a = _gen_ai(s)
  pc = helper._pascal_triangle(s)
  p = np.flip(np.array(a).dot(pc))
  # p[0] * f_0 + p[1] * f_1 + ...
  def adams(f, xks, yks, h):
    yk = yks[-1]
    xks = np.array(xks[-s:])
    yks = np.array(yks[-s:])
    # yks = [y(k-s), y(k-s+1), ... y(k)]
    dy = 0
    for i in range(0, len(p)):
      dy += p[i]*np.array(f(xks[i], yks[i]))
    return yk + h*dy
  return [adams, p] 

