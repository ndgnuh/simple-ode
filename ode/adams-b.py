import numpy as np
import sympy as sp
import pprint
s = int(input("s = "))

def gen_fi(s):
  zero_vec = np.array(0)
  pfi = np.asarray([1,0])
  delta_fi = np.asarray([1])
  nfact = 1
  for i in range(1, s):
    nfact *= i
    ipfi = np.polyint(pfi)
    delta_fi = np.append(delta_fi, (np.polyval(ipfi, s) - np.polyval(ipfi, s-1))/nfact)
    pfi = np.append(pfi, zero_vec) - i*np.append(zero_vec, pfi)
  return [pfi, delta_fi]

[p, fi] = gen_fi(s)

fact_arr = [1]
for i in range(1, s+1):
  fact_arr.append(fact_arr[i-1]*i)
print(fact_arr)

def comb(k, n, fact_arr):
  return fact_arr[n] / fact_arr[n-k] / fact_arr[k]

def gen_comb_matrix(s, fact_arr):
  mat = np.array([[0]*s]*s)
  for i in range(0, s):
    sgn = 1 if (i % 2 == 0) else -1
    for j in range(0,i+1):
      mat[i][j] = sgn*comb(j, i, fact_arr)
      sgn=-sgn
  return mat 

mat = gen_comb_matrix(s, fact_arr)
ficoef = fi.T.dot(mat)

print("Công thức AB-", s, ". Các hệ số của fi (i từ 0 tới ", s,"):", sep="")
print(ficoef)
