import numpy as np
from bvp.tridiag_solver import tridiag_solve

def finite_different(p, q, f, a, b, ua, ub, h):
  # x mesh
  n = int((b-a)/h)-1
  T = np.zeros(n*n).reshape(n,n)
  x = a + h

  # T = [t_ij]
  # t_00 and t_01
  T[0,0] = 2 + h**2 * q(x)
  T[0,1] = - 1 + h * p(x)/2
  F = [h**2*f(x) + ua + p(x)*h/2*ua]

  # t_ii, t_{i,i+1}, t_{i,i-1}
  for i in range(1, n-1):
    x = x + h
    T[i,i-1] = -1-p(x)*h/2
    T[i,i] = 2 + h**2 * q(x)
    T[i,i+1] = - 1 + h * p(x)/2
    F.append(h**2*f(x))

  # t_{n-1,n-1}, t_{n-1,n-2}
  i = n-1
  x = x + h
  T[i,i] = 2 + h**2 * q(x)
  T[i,i-1] = -1-p(x)*h/2
  F.append(h**2*f(x) + ub - ub*p(x)*h/2)
  
  # solve for U
  # U = tridiag_solve(T, np.asarray(F).reshape(n,1), 0)
  U = np.linalg.inv(T).dot(F)
  return U
    
