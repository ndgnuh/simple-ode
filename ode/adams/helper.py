import numpy as np 

def gen_factarr(s):
  fact_arr = [1]
  for i in range(1, s+1):
    fact_arr.append(fact_arr[i-1]*i)
  return fact_arr

def fast_comb(k, n, fact_arr):
  return fact_arr[n] / fact_arr[n-k] / fact_arr[k]

def gen_comb_matrix(s, fact_arr):
  mat = np.array([[0]*s]*s)
  for i in range(0, s):
    sgn = 1 if (i % 2 == 0) else -1
    for j in range(0,i+1):
      mat[i][j] = sgn*fast_comb(j, i, fact_arr)
      sgn=-sgn
  return mat 

