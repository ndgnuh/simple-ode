import numpy as np 
import sympy as sp
from ode import euler, rk, trapezoidal

"""
  voi phuong phap hien dung numpy de tao ham f
"""

f = lambda x,y: np.sin(y)
x0 = 0; y0 = 1; x = 4; steps=10
[xk, yk] = euler.explicit(f, x0, y0, x, steps)
print("xk:", xk)
print("yk:", yk)


"""
  voi phuong phap hien an dung sympy de tao ham f
"""

f = lambda x,y: sp.sin(y)
x0 = 0; y0 = 1; x = 5; steps=2
[xk, yk] = euler.implicit(f, x0, y0, x, steps)