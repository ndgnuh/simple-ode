from sympy import Symbol, lambdify
from scipy.optimize import newton 
import numpy as np

def trapezoidal(f, xk, yk, x, stepnum):
  try:
    print("\n\nTrapezoidal method:")
    if(np.abs(stepnum) < 1):
      print("invalid number of steps! Exiting...")
      return 1
    h = (x-xk) / stepnum
    y = Symbol("y")
    xks= [xk]
    yks= [yk]
    print("step h =", h)
    print("xk", "".ljust(5), "yk", "".ljust(25), "eq")
    for i in range(0, np.abs(stepnum)):
      g = yk + h*(f(xk,yk) + f(xk+h,y))/2 - y
      print(str(np.round(xk,3)).ljust(5) , " | ", str(yk).ljust(25), "|", g)
      g = lambdify(y,g)
      yk = newton(g, xk)
      xk = xk + h
      xks.append(xk)
      yks.append(yk)
  except RuntimeError:
    print("Unable to solve, failed to converge")
  return [np.asarray(xks), np.asarray(yks)]


def predictor_corrector(f, xk, yk, x, stepnum):
  print("\n\nTrapezoidal predictor-corrector scheme.")
  try:
    if(stepnum <= 0):
      print("invalid number of steps!")
      return 0
    h = (x - xk) / stepnum
    print("step h =",h)
    xks = [xk]
    yks = [yk]
    print("xk", "".ljust(5), "yk", "".ljust(25))
    for i in range(0, stepnum):
      # Predictor
      f0 = f(xk, yk)
      ybar = yk + h * f0 
      # Corrector
      xk = xk + h
      yk = yk + h/2*(f0 + f(xk, ybar))
      yks.append(yk)
      xks.append(xk)
      print(str(np.round(xk,3)).ljust(5) , " | ", str(yk).ljust(25))
    print(str(np.round(xk,3)).ljust(5) , " | ", str(yk).ljust(25))
    return [np.asarray(xks),np.asarray(yks)]
  except RuntimeError:
    print("Unable to solve, failed to converge")
    return [np.asarray(xks),np.asarray(yks)]
