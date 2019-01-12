import numpy as np 
from misc import rprint
from ode import schemes, rk, euler, trapezoidal
from inputs import *
from misc.error import error_eval

# from "tên thư mục" import "tên file"
# from "tên thư mục"."tên file" import "tên hàm/biến/..."
# import "tên" as "tên alias"

[xk, yk] = schemes.implicit(f, x0, y0, x, stepnum, rk.irk3, euler.ex_euler)
rprint.result(xk, yk, 12)

# error_eval.eval(f, x0, y0, x, 2*stepnum)
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
[xk, yk] = schemes.implicit(f, x0, y0, x, stepnum, rk.irk3, rk.erk3)
rprint.result(xk, yk) # in kq

# tinh tiep 1 lan nua voi so buoc nhay gap doi
[xk2, yk2] = schemes.implicit(f, x0, y0, x, stepnum*2, rk.irk3, rk.erk3)
[x_e, err] = error_eval([xk, xk2], [yk, yk2])
rprint.result(x_e, err) # in sai so
# y = lambda x: np.exp(-x/2)/3*(5*np.sqrt(3)*np.sin(x*np.sqrt(3)/2)+3*np.cos(np.sqrt(3)*x/2))
