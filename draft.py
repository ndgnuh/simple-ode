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

"""
  test on y'' + y' + y = 0 or y'' = -y' - y with y(0) = y'(0) = 1
  systemize the problem:
    y1' = y2, y1(0) = 1
    y2' = -y2-y1, y2(0) = 1
"""

f = lambda x, y: [
  y[1],
  -y[1]-y[0]
]
x0 = 0
y0 = [1, 1]

[xk, yk] = euler.implicit(f, x0, y0, 1, 100)
rprint.result(xk, yk)


"""
  test on y'' - y' - y = 0 or y'' = y' + y with y(0) = y'(0) = 1
  systemize the problem:
    y1' = y2, y1(0) = 1
    y2' = y2+y1, y2(0) = 1 // unstable problem.
"""

f = lambda x, y: [
  y[1],
  y[1]+y[0]
]
x0 = 0
y0 = [1, 1]

[xk, yk] = euler.implicit(f, x0, y0, 10, 40)
rprint.result(xk, yk)
