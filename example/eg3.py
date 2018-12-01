
"""
  example 2: y' = 1 - y with y(0) = 0 solving by implicit euler
"""
import sys
sys.path.append('/home/hung/Projects/tp25')
from ode import trapezoidal, euler
import numpy as np
import sympy as sp
import matplotlib.pyplot as plt


y = lambda x: 1-np.exp(-x)
f = lambda x,y: 1-y
x0 = 0; y0 = y(x0); x = 6
stepnum2 = (int)((x-x0)/0.75)

[x1,y1]= trapezoidal.trapezoidal(f,x0,y0,x,stepnum2)
[x2,y2]= euler.implicit(f,x0,y0,x,stepnum2)
p1 = plt.subplot(121)
p2 = plt.subplot(122)

xx = np.linspace(x0, x)
p1.plot(np.abs(y(x1) - y1), '-.s')
p1.plot(np.abs(y(x2) - y2), '-.o')
p2.plot(x1,y1,'-.s')
p2.plot(x2,y2,'-.o')
p2.plot(xx,y(xx), '-')
p2.set_title("Nghiệm với h = 0.75")
p1.set_title("Sai số với h = 0.75")
p1.legend(["hình thang", "Euler ẩn"])
p2.legend(["hình thang", "Euler ẩn", "y(x)"])
plt.show()