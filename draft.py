import numpy as np
import ode.euler as euler
from misc import rprint

f = lambda x,y: [
  y[0],
  y[1]
]
x0 = 0; y0 = [2, 1]; step = 1

[xk, yk] = euler.explicit_syseq(f, x0, y0, 3, 3)
rprint.result(xk, yk)

f = lambda x,y:y
[xk, yk] = euler.explicit(f, x0, 1, 3, 3)
rprint.result(xk, yk)