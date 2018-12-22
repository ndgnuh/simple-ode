import numpy as np 
# import ab as bashforth
import sys
sys.path.append("/home/hung/Projects/simple-ode")
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


def ab_builder(s):
  dfi_coef_1 = np.array([1, 0])
  dfi_coef_2 = [1]; fact_arr = [1]
  sgn = -1
  for i in range(1, s):
    fact_arr.append(fact_arr[i-1] * i)
    int_dfi_coef_1 = np.polyint(dfi_coef_1)
    dfi_coef_2.append(sgn*(np.polyval(int_dfi_coef_1, 1) - np.polyval(int_dfi_coef_1, 0))/fact_arr[i-1])
    dfi_coef_1 = np.polymul(dfi_coef_1, [1, i])
    sgn = -sgn
  dfi_coef_2 = np.asarray(dfi_coef_2)
  mat = gen_comb_matrix(s, fact_arr)
  for i in range(0, s):
    mat[i] = np.flip(mat[i])
  ficoef = dfi_coef_2.T.dot(mat)
  print("ficoef of s =", s, ":", ficoef)
  def adam(f, xks, yks, h):
    xks = xks[-s:]; yks = yks[-s:]
    dy = 0; yk = yks[-1]
    for i in range(0, len(ficoef)):
      dy = dy + ficoef[i]*f(xks[i], yks[i])
    return yk + h*dy
  return adam

s = int(input("s = "))

for i in range(0, s):
  ab_builder(i+1)