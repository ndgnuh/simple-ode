import numpy as np
import sympy as sp
from helper import *
import sys
sys.path.append("/home/hung/Projects/simple-ode")
from misc import rprint
import pprint

s = int(input("s = "))

def gen_dfi(s):
  zero_vec = np.array(0)
  pfi = np.asarray([1,0])
  delta_fi = np.asarray([1])
  nfact = 1
  for i in range(1, s):
    nfact *= i
    ipfi = np.polyint(pfi) # pfi = t(t-1)(t-2)...(t-s),
    delta_fi = np.append(delta_fi, (np.polyval(ipfi, s) - np.polyval(ipfi, s-1))/nfact)
    pfi = np.append(pfi, zero_vec) - i*np.append(zero_vec, pfi)
  return delta_fi

def ab_t(a, f, xks, yks):
  s = len(a)
  yks = yks.T[-s:]; xks = xks[-s:]
  yk = yks[-1]
  sum = 0
  
  return yk

def ab_builder(s):
  dfi = gen_dfi(s)
  fact_arr = gen_factarr(s)
  mat = gen_comb_matrix(s, fact_arr)
  ficoef = dfi.T.dot(mat)
  print("ficoef of s =", s, ":", ficoef)
  def adam(f, xks, yks, h):
    xks = xks[-s:]; yks = yks[-s:]
    dy = 0; yk = yks[-1]
    for i in range(0, len(ficoef)):
      dy = dy + ficoef[i]*f(xks[i], yks[i])
    return yk + h*dy
  return adam

def adam_bashforth(f, xk, yk, x, stepnum, s = 4):
  h = (x-xk)/stepnum
  xks = [xk]
  yks = [yk]
  for i in range(0, s):
    ab_formula = ab_builder(i+1)
    yk = ab_formula(f, xks, yks, h)
    xk = xk + h
    xks.append(xk); yks.append(yk)
  for i in range(s, stepnum):
    yk = ab_formula(f, xks, yks, h)
    xk = xk + h
    xks.append(xk); yks.append(yk)
  return [xks, yks]


f = lambda x,y: 1-y
[x, y] = adam_bashforth(f, 0, 0,3,9, s)
rprint.result(x,y,12)

f = lambda x,y: np.asarray([1-y[0],1-y[1]])
[x, y1] = adam_bashforth(f, 0,np.asarray([0, 0]),3,9, s)
rprint.result(x,y1,12)
print(x, y1[:,0] - y)
