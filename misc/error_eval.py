import numpy as np 
import sys 
sys.path.append("/home/hung/Projects/simple-ode/")
from ode import schemes, euler, rk, trapezoidal

def ex_eval(f, x0, y0, x, stepnum, exf, div=4):
  cur_stepnum = stepnum
  xx = []; yy = []
  er = []
  dy = np.array([])
  for i in range(0, div):
    [xk, yk] = schemes.explicit(f, x0, y0, x, cur_stepnum, exf)
    cur_stepnum = int(cur_stepnum * 2)
    xx.append(xk); yy.append(yk)
  for i in range(0, stepnum):
    for j in range(1, div):
      yy[j] = np.delete(yy[j], i)
      xx[j] = np.delete(xx[j], i)
  print(np.array(yy))

f = lambda x, y: 1 - y
x0 = 0; y0 = 0
x = 3; stepnum = 9
ex_eval(f, x0, y0, x, stepnum, rk.erk3)