from sympy import Symbol, lambdify
from scipy.optimize import newton 
import numpy as np

# def trapezoidal(f, xk, yk, x, stepnum):
#   try:
#     print("\n\nTrapezoidal method:")
#     if(np.abs(stepnum) < 1):
#       print("invalid number of steps! Exiting...")
#       return 1
#     h = (x-xk) / stepnum
#     y = Symbol("y")
#     xks= [xk]
#     yks= [yk]
#     print("step h =", h)
#     print("xk", "".ljust(5), "yk", "".ljust(25), "eq")
#     for i in range(0, np.abs(stepnum)):
#       g = yk + h*(f(xk,yk) + f(xk+h,y))/2 - y
#       print(str(np.round(xk,3)).ljust(5) , " | ", str(yk).ljust(25), "|", g)
#       g = lambdify(y,g)
#       yk = newton(g, xk)
#       xk = xk + h
#       xks.append(xk)
#       yks.append(yk)
#   except RuntimeError:
#     print("Unable to solve, failed to converge")
#   return [np.asarray(xks), np.asarray(yks)]


def _trapezoidal_single(f, xk, yk, x, stepnum, ite = 50):
  h = (x-xk) / stepnum
  xks= [xk]; yks= [yk]
  print("step h =", h)
  for i in range(0, stepnum):
    xknext = xk + h
    ybar = yk + h*f(xk,yk)
    for j in range(0, ite):
      ybar = yk  + h/2*(f(xk,yk) + f(xknext, ybar))
    xk = xknext; yk = ybar
    xks.append(xk); yks.append(yk)
  return [xks, yks]


def _trapezoidal_system(f, xk, yk, x, stepnum, ite = 50):
  h = (x-xk) / stepnum
  xks= [xk]; yks= [yk]
  print("step h =", h)
  for i in range(0, stepnum):
    xknext = xk + h
    ybar = np.asarray(yk) + h*np.asarray(f(xk,yk))
    for j in range(0, ite):
      ybar = np.asarray(yk)  + h/2*(np.asarray(f(xk,yk)) + np.asarray(f(xknext, ybar)))
    xk = xknext; yk = ybar
    xks.append(xk); yks.append(yk)
  return [xks, yks]


def trapezoidal(f,xk,yk,x,stepnum,ite=50):
  print("Trapezoidal method:")
  if(stepnum < 1):
    print("invalid number of steps! Exiting...")
    return 1
  if((type(yk) == type([])) or (type(yk) == type(np.asarray([])))):
    [xks, yks] = _trapezoidal_system(f, xk, yk, x, stepnum, ite)
  else:
    [xks, yks] =  _trapezoidal_single(f, xk, yk, x, stepnum, ite)
  return [np.asarray(xks), np.asarray(yks)]
