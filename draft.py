import numpy as np
import ode.euler as euler
from misc import rprint

f = lambda x,y: [
  1-2*y[0],
  1-2*y[1]
]
x0 = 0; y0 = [1, 1]; step = 1

[xk, yk] = euler.implicit(f, x0, y0, 1, 10)
rprint.result(xk, yk, 10)

f = lambda x,y: 1-2*y
[xk, yk] = euler.implicit(f, x0, 1, 1, 10)
rprint.result(xk, yk)

