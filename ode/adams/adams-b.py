import numpy as np
import sympy as sp
from helper import *
import pprint

s = int(input("s = "))

def gen_dfi(s):
  zero_vec = np.array(0)
  pfi = np.asarray([1,0])
  delta_fi = np.asarray([1])
  nfact = 1
  for i in range(1, s):
    nfact *= i
    # pfi = t(t-1)(t-2)...(t-s)
    ipfi = np.polyint(pfi)
    delta_fi = np.append(delta_fi, (np.polyval(ipfi, s) - np.polyval(ipfi, s-1))/nfact)
    pfi = np.append(pfi, zero_vec) - i*np.append(zero_vec, pfi)
  return [pfi, delta_fi]

[p, dfi] = gen_dfi(s)



fact_arr = gen_factarr(s)
mat = gen_comb_matrix(s, fact_arr)
ficoef = dfi.T.dot(mat)

print("Công thức AB-", s, ". Các hệ số của fi (i từ 0 tới ", s-1,"):", sep="")
print(ficoef)


f = lambda x, y: y
x0 = 0; y0 = 1
tks = [y0]
fis = [f(x0, y0)]
yk = y0
xk = x0
stepnum = 20; x = 4
h = (x - xk)/stepnum 
for i in range(1, stepnum):
  yks = np.array([yk])
  xks = np.array([xk])
  if(i < s):
    [p, dfi] = gen_dfi(i)
    fact_arr = gen_factarr(i)
    mat = gen_comb_matrix(i, fact_arr)
    ficoef = dfi.T.dot(mat)
  # if(i > s):
  yk = yk + h*ficoef.T.dot(fis)
  xk = xk + h
  fis = np.append(fis, f(xk, yk))[-(s-1):]
  yks = np.append(yks, [yk])
  xks = np.append(xks, xk)

print(xks, yks)
print(ficoef)