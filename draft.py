import numpy as np
from ode import euler, trapezoidal
from misc import rprint

f = lambda x,y: 1 - y
x0 = 0; y0 = 0; x = 1; step = 5;
[x1, y1] = trapezoidal.trapezoidal(f, x0, y0, 1, 5)
rprint.result(x1, y1, 11)
f = lambda x,y: [
  1 - y[0],
  1 - y[1]
]
x0 = 0; y0 = [0, 0];
[x1, y1] = euler.implicit(f, x0, y0, 1, 5)
rprint.result(x1, y1, 11)

