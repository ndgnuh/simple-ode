import numpy as np 
import inspect
import matplotlib.pyplot as plt
from sympy import Symbol, lambdify
from scipy.optimize import newton

def explicit(f,xk,yk,x,stepnum,epsilon=0):
  print("\n\nExplicit Euler method:")
  if(stepnum == 0):
    print("Invalid number of steps. Exiting...")
    return 1
  h = (x-xk)/stepnum
  i = 0
  xks=[xk]
  yks=[yk]
  print("step size h = ", h)
  print("y' =", inspect.getsource(f))

  print("xk", "".ljust(5), "yk", "".ljust(25))
  for i in range(0, stepnum):
    print(str(np.round(xk,3)).ljust(5) , " | ", str(yk).ljust(25))
    yk = yk + h * f(xk, yk)
    xk+= h
    i = i + 1
    xks.append(xk)
    yks.append(yk)
  print(str(np.round(xk,3)).ljust(5) , " | ", str(yk).ljust(25))
  print("y(", xk,") = ", yk)
  return [np.asarray(xks),np.asarray(yks)]

def implicit(f,xk,yk,x,stepnum,epsilon=0):
  try:
    print("\n\nImplicit Euler method:")
    if(stepnum == 0):
      print("Invalid number of steps. Exiting...")
      return 1
    xks=[xk]
    yks=[yk]
    h = (x-xk)/stepnum
    print("step h =", h)
    print("xk", "".ljust(5), "yk", "".ljust(25), "eq")
    y  = Symbol("y") #y ~ y(k+1), symbolic for solving
    for i in range(0, stepnum):
      eulerEq = h * f(xk, y) + yk - y
      print(str(np.round(xk,3)).ljust(5) , " | ", str(yk).ljust(25), "|", eulerEq)
      eulerEq = lambdify(y, eulerEq) 
      yk = newton(eulerEq, xk)
      xk = xk + h
      xks.append(xk)
      yks.append(yk)
    print(str(np.round(xk,3)).ljust(5) , str(yk).ljust(25))
    print("y(", xk, ") = ", yk)
    return [np.asarray(xks), np.asarray(yks)]
  except RuntimeError:
    print("Unable to solve, failed to converge")
    return [np.asarray(xks), np.asarray(yks)]