import numpy as np 
from misc import rprint
from ode import schemes, rk, euler, trapezoidal
from inputs import *
# from "tên thư mục" import "tên file"
# from "tên thư mục"."tên file" import "tên hàm/biến/..."
# import "tên" as "tên alias"
x = 2
stepnum = 4
[xk, yk] = schemes.implicit(f, x0, y0, x, stepnum, euler.im_euler, rk.erk4, 40)
rprint.result(xk, yk, 12)


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
x0 = 0; x = 2.5; stepnum = 5;
[xk, yk] = schemes.implicit(f, x0, y0, x, stepnum, euler.im_euler, rk.erk3)
# rprint.result(xk, yk)

y = lambda x: np.exp(-x/2)/3*(5*np.sqrt(3)*np.sin(x*np.sqrt(3)/2)+3*np.cos(np.sqrt(3)*x/2))

