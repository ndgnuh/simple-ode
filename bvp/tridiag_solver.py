import numpy as np

def tridiag_solve(T, F, x0):
  # check if conditions are meet
  if(np.shape(T)[0] != np.size(F)):
    print("Dimension error.")
    return False
  
  # If ok proceed 
  n = np.size(F) 
  F = -np.array(F)
  
  # Find alphas, betas
  alpha = [T[0,1]/-T[0,0]]
  beta = [F[0]/-T[0,0]]
  for i in range(0, n-1):
    alpha.append(T[i, i+1]/(-T[i,i] - alpha[-1] * T[i,i-1]))
    beta.append((T[i,i-1]*beta[-1] + F[i])/(-T[i,i]-alpha[-1]*T[i,i-1]))

  # Find xn, x(n-1), x(n-2), ...
  X = []
  X.append((T[n-1, n-2]*beta[-1] + F[-1])/ (-T[n-1,n-1] - T[n-1,n-2]*alpha[-1]))
  for i in range(0, n-1):
    X.append(alpha[-i-1]*X[i] + beta[-i-1])
  return np.flip(X)
