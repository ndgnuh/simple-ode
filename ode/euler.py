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
  print("y' =", inspect.getsource(f), end="\n")
  for i in range(0, stepnum):
    yk = yk + h * f(xk, yk)
    xk+= h
    i = i + 1
    xks.append(xk)
    yks.append(yk)
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
    print("y' =", inspect.getsource(f), end="\n")
    y  = Symbol("y") #y ~ y(k+1), symbolic for solving
    for i in range(0, stepnum):
      eulerEq = h * f(xk, y) + yk - y
      eulerEq = lambdify(y, eulerEq) 
      yk = newton(eulerEq, xk)
      xk = xk + h
      xks.append(xk)
      yks.append(yk)
    print("y(", xk, ") = ", yk)
    return [np.asarray(xks), np.asarray(yks)]
  except RuntimeError:
    print("Unable to solve, failed to converge")
    return [np.asarray(xks), np.asarray(yks)]

def explicit_syseq(f, xk, yk, x, stepnum):
  h = (x-xk)/stepnum
  if(h == 0):
    print("invalid stepsize")
    return 0
  xks = [xk]; yks=[yk]
  for i in range(0, stepnum):
    yk =np.asarray(yk) + h*np.asarray(f(xk,yk))
    xk += h; xks.append(xk); yks.append(yk)
  return [xks, yks]