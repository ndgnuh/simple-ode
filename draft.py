
import numpy as np
import sympy as sp
import scipy as scp
from ode import euler, trapezoidal
import matplotlib.pyplot as plt

l = -1
#y = lambda x:  -(np.sqrt(3) *np.exp(3*x))/np.sqrt(1 + np.exp(6*x))
#f = lambda x,y: 3*y-y**3
# y = lambda x: 1/(np.sqrt(2)*np.sqrt(1.1 - x))
# f = lambda x,y: y**3
y = lambda x: 1/15-np.exp(-15*x)/15
f = lambda x,y: 1-15*y
x0 = 0
y0 = y(x0)
print('y0 =',y0)
xn = 3
stpnum = np.abs((int)((xn - x0)/0.1))
[x1,y1]= euler.explicit(f,x0,y0,xn,stpnum)
# [x2,y2]= euler.implicit(f,x0,y0,xn,stpnum)
# [x3,y3]= trapezoidal.trapezoidal(f,x0,y0,xn,stpnum)

x = np.linspace(x0,xn)
p1 = plt.subplot(221)
p2 = plt.subplot(222)
p3 = plt.subplot(223)
p4 = plt.subplot(224)

p1.plot(x1, np.abs(y1-y(x1)), '-.x')
# p2.plot(x2, np.abs(y2-y(x2)), '-.s')
# p3.plot(x3, np.abs(y3-y(x3)), '-.o')
p4.plot(x1,y1, '-.x')
# p4.plot(x2,y2, '-.s')
# p4.plot(x3,y3, '-.o')
p4.plot(x,y(x), '-')
# p4.legend("explicit euler")
# p4.legend("implicit euler")
# p1.set_title("explicit euler error")
# p2.set_title("implicit euler error")
# p3.set_title("trapezoidial error")
p1.set_title("Nháp $\int_{x_0}^x$")

# plt.plot(x,y(x), '-.')

# plt.plot(x1,np.y1-y(x1), '-s')
# plt.plot(x2,y2-y(x2), '-x')
# plt.plot(x3,y3-y(x3), '-o')
# plt.plot(x,y(x), '-.')

plt.show()

 
"""
print("sai so")
print("xk".ljust(10),"yk".ljust(10),"error".ljust(5))
print("xk:", x2.real)
print("yk:", y2.real)
print("error:", np.abs(y(x2)-y2))
"""