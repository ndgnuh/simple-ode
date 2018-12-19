import numpy as np 
from ode import schemes, euler, rk, trapezoidal

def ex_eval(f, x0, y0, x, stepnum, exf, div=4):
  cur_stepnum = stepnum
  x = []; y = []
  dy = np.array([])
  for i in range(0, div):
    [xk, yk] = schemes.explicit(f, x0, y0, x, stepnum, exf)
    cur_stepnum = cur_stepnum / 2
    x.append(xk); y.append(yk)
  print(y)
