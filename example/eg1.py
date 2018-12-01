"""
  example 1: y' = 1 - 15y with y(0) = 0
"""
import sys
sys.path.append('/home/hung/Projects/tp25')
from ode import euler
import numpy as np
import matplotlib.pyplot as plt

# input 
y = lambda x: (1 - np.exp(-15*x))/15
f = lambda x,y: 1 - 15*y
x0 = 0; y0 = y(x0); x = 3
stepnum1 = (int)((x-x0)/0.25)
stepnum2 = (int)((x-x0)/0.1)


[x1,y1]= euler.explicit(f,x0,y0,x,stepnum1)
[x2,y2]= euler.explicit(f,x0,y0,x,stepnum2)

# plot
xx = np.linspace(x0, x, 100)
p1 = plt.subplot(121)
p2 = plt.subplot(122)
p11 = p1.plot(x1,y(x1) - y1,'-.x')
p12 = p1.plot(x2,y(x2) - y2,'-.o')
p21 = p2.plot(x1,y1, '-.x')
p22 = p2.plot(x2,y2, '-.o')
p23 = p2.plot(xx,y(xx),'-')
p1.legend(["h = 0.25","h = 0.1"])
p2.legend(["h = 0.25","h = 0.1", "y(x)"])
p1.set_title("Sai số")
p2.set_title("Nghiệm")

plt.show()