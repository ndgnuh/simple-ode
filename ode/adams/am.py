import numpy as np 
import sys
sys.path.append("/home/hung/Projects/simple-ode")
from scipy.linalg import pascal
from misc import rprint
from helper import fast_comb

def gen_comb_matrix(s, fact_arr):
  mat = np.array([[0]*s]*s)
  for i in range(0,s):
    sgn = 1 #if (i % 2 == 0) else -1
    for j in range(0,i+1):
      mat[i][j] = sgn*fast_comb(j, i, fact_arr)
      sgn=-sgn
  return mat 

# def moulton_builder(s):
#   def moulton(f, xks, yks, h):
#     xks = xks[:s]; yks = yks[:s]
#     return yks[-1]
#   return moulton

# def adams_moulton(f, xk, yk, x, stepnum, s = 4, correctors = 50):
#   xks = [xk]; yks = [yk]
#   h = (x - xk)/stepnum
#   for i in range(0, s):
#     ab = bashforth.ab_builder(i+1)
#     am = moulton_builder(i+1)
#     ykj = yk + ab(f, xks, yks, h)
#     xk = xk + h
#     yks.append(ykj); xks.append(xk)
#     for j in range(0, correctors):
#       ykj = yk + am(f, xks, yks, h)
#     yks[-1] = ykj
#   return [np.asarray(xks), np.asarray(yks)]




# s = int(input("s = "))
# f = lambda x,y: 1-y
# [x, y] = adams_moulton(f, 0, 0,3,9, s)
# rprint.result(x,y,12)
def gen_ai(s):
  dp = np.array([1])
  a = [1]
  for i in range(1, s):
    dp = np.polymul(dp, [1, i-2])/i
    a.append(np.polyval(np.polyint(dp), 1) - np.polyval(np.polyint(dp),0))
  return a

def pascal_triangle(s):
  pc = np.array(pascal(s, kind='lower', exact= False))
  for i in range(0, s):
    if i % 2 != 0:
      pc [:,i] =- pc[:,i]
  return pc

def ab_builder(s):
  a = gen_ai(s)
  pc = pascal_triangle(s)
  p = np.array(a).dot(pc)
  def adam(f, xks, yks, h):
    xks = xks[-s:]; yks = yks[-s:]
    dy = 0; yk = yks[-1]
    for i in range(0, len(d)):
      dy = dy + d[i]*f(xks[i], yks[i])
    return yk + h*dy
  return adam

# ab_builder(1)
# ab_builder(2)
ab_builder(3)
ab_builder(4)

# ab_builder(5)

# ab_builder(6)