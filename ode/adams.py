from ode.adams_builder import am, ab
import numpy as np
import sympy as sym
from scipy.optimize import newton

def bashforth(f, xk, yk, x, stepnum, s = 4):
  h = (x-xk)/stepnum
  xks = [xk]
  yks = [yk]
  for i in range(0, s):
    abf = ab._builder(i+1)[0]
    yk = abf(f, xks, yks, h)
    xk = xk + h
    xks.append(xk); yks.append(yk)
  for i in range(s, stepnum):
    yk = abf(f, xks, yks, h)
    xk = xk + h
    xks.append(xk); yks.append(yk)
  return [np.asarray(xks), np.asarray(yks)]

def moulton(f, xk, yk, x, stepnum, s = 4, iterations = 50):
  h = (x-xk)/stepnum
  yk = np.array(yk)
  xks = [xk]
  yks = [yk]
  for i in range(0, s):
    abf = ab._builder(i+1)[0]
    amf = am._builder(i+1)[0]
    xk = xk + h; xks.append(xk)
    ykj = abf(f, xks, yks, h)
    yks.append(ykj)
    for j in range(0, iterations):
      yks[-1] = yks[-2] + h*amf(f, xks, yks, h)
  for i in range(s, stepnum):
    xk = xk + h; xks.append(xk)
    ykj = abf(f, xks, yks, h)
    yks.append(ykj)
    for j in range(0, iterations):
      yks[-1] = yks[-2] + h*amf(f, xks, yks, h)
  return [np.asarray(xks), np.asarray(yks)]

def get_formula(s, type="ab"):
  """Lấy ra công thức hàm"""
  builder = ab._builder
  next_s = s
  if(type == "am"):
    builder = am._builder
    next_s = s-1
  fi_coef = builder(s)[1] 
  dy = 0
  ys = sym.Symbol(('y_' + str(next_s-1)), commutative=False)
  for i in range(0, s):
    dy = dy + sym.Symbol('f_' + str(i), commutative=False)*sym.nsimplify(fi_coef[i], tolerance=10e-6)
  h = sym.Symbol('h')
  eq = ys+h*dy 
  print("Terminal printing: ")
  sym.printing.pprint(eq)
  print("Latex printing (copy and paste this into adams.html): ")
  print("y_", next_s, "=", sym.latex(ys), "+", sym.latex(h*dy))
  
def moulton_newton(f, xk, yk, x, stepnum, s):
  h = (x-xk)/stepnum
  yk = np.array(yk)
  xks = [xk]
  yks = [yk]
  for i in range(0, s):
    amf = am._builder(i+1)[0]
    print(am._builder(i+1)[1])
    xk = xk + h; xks.append(xk)
    amg = lambda y: y - yk - h*amf(f, xks, np.append(yks, y), h)
    yk = newton(amg, yk, maxiter=200)
    yks.append(yk)
  for i in range(s, stepnum):
    xk = xk + h; xks.append(xk) 
    amg = lambda y: y - yk - h*amf(f, xks, np.append(yks, y), h)
    yk = newton(amg, yk, maxiter=200)
    yks.append(yk)
  return [np.asarray(xks), np.asarray(yks)] 