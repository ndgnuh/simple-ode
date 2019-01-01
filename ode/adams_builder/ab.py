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
  print("p", p)
  def adams(f, xks, yks, h):
    yk = yks[-1]
    xks = np.array(xks[-s:])
    yks = np.array(yks[-s:])
    print(yks)
    return yk + h*p.dot(np.array(f(xks, yks)))
  return [adams, p] 

