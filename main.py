import numpy as np 
from ode import euler, rk, trapezoidal
from misc import rprint
# from "tên thư mục" import "tên file"
# from "tên thư mục"."tên file" import "tên hàm/biến/..."
# import "tên" as "tên alias"
"""
  f = sin(y), y(0) = 1; tinh y(4), voi 10 buoc nhay
"""

f = lambda x,y: np.sin(y)
x0 = 0; y0 = 1; x = 4; steps=10
[xk, yk] = euler.explicit(f, x0, y0, x, steps)
rprint.result(xk, yk)

"""
  - giai he pt, hoac pt vi phan bac cao, vd: y'' + y' + y = 0,  y(0) = 1, y'(0) = 2
  - dat y1 = y, y2 = y1' --> he pt:
    + y1' = y2; y1(0) = 2
    + y2' = -y2-y1; y2(0) = 2
  - f(x, y) = (y2, -y2-y1)
  - y0 = (y1(0), y2(0))
"""
f = lambda x, y: [
  y[1], 
  -y[1]-y[0]
]
y0 = [1, 2]
x0 = 0; x = 10; stepnum = 40;
[xk, yk] = trapezoidal.trapezoidal(f, x0, y0, x, stepnum)
rprint.result(xk, yk)

y = lambda x: np.exp(-x/2)/3*(5*np.sqrt(3)*np.sin(x*np.sqrt(3)/2)+3*np.cos(np.sqrt(3)*x/2))

