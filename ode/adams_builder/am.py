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
  p = np.flip(np.array(a).dot(pc))
  # dy / h = p[0] * f_0 + p[1] * f_1 + ...
  def adams(f, xks, yks, h):
    yk = yks[-2]
    xks = np.array(xks[-s:])
    yks = np.array(yks[-s:])
    dy = 0
    for i in range(0, len(p)):
      dy += p[i]*np.asarray(f(xks[i], yks[i]))
    # return yk + h*p.dot(f(xks, yks))
    return yk + dy*h
  return [adams, p]
