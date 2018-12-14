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


print(p, dfi)

fact_arr = gen_factarr(s)
mat = gen_comb_matrix(s, fact_arr)
ficoef = dfi.T.dot(mat)

print("Công thức AB-", s, ". Các hệ số của fi (i từ 0 tới ", s-1,"):", sep="")
print(ficoef)

def test(x, y):
  return x*y

def gen_bashforth():
  return lambda x: test(x,x)

f = gen_bashforth()
print(f(3))