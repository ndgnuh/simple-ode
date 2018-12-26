import numpy as np 
from scipy.linalg import pascal

def _builder(s, _gen_ai):
  a = _gen_ai(s)
  pc = _pascal_triangle(s)
  p = np.array(a).dot(pc)
  def adams(f, xks, yks, h):
    xks = xks[-s:]; yks = yks[-s:]
    dy = 0; yk = yks[-1]
    for i in range(0, len(p)):
      dy = dy + p[i]*f(xks[i], yks[i])
    return yk + h*dy
  return [adams, p]

def _pascal_triangle(s):
  pc = np.array(pascal(s, kind='lower', exact= False))
  for i in range(0, s):
    if i % 2 != 0:
      pc [:,i] =- pc[:,i]
  return pc