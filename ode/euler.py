import numpy as np

ex_euler = lambda f, xk, yk, h: yk + h*np.asarray(f(xk, yk))
im_euler = lambda f, xk, xk1, yk, yk1, h: np.asarray(yk) + h*np.asarray(f(xk1, yk1))

"""
def _explicit_single(f,xk,yk,x,stepnum,epsilon=0):
  xks=[xk];  yks=[yk]; h = (x - xk)/stepnum
  for i in range(0, stepnum):
    yk = yk + h * f(xk, yk)
    xk+= h
    i = i + 1
    xks.append(xk)
    yks.append(yk)
  print("y(", xk,") = ", yk)
  return [xks, yks]

def _explicit_system(f, xk, yk, x, stepnum):
  print("(applying with system equations)")
  h = (x-xk)/stepnum
  if(h == 0):
    print("invalid stepsize")
    return 0
  print("step size h = ", h)
  xks = [xk]; yks=[yk]
  for i in range(0, stepnum):
    yk =np.asarray(yk) + h*np.asarray(f(xk,yk))
    xk += h; xks.append(xk); yks.append(yk)
  return [xks, yks]

def explicit(f, xk, yk, x, stepnum):
  print("Explicit Euler method:")
  if(stepnum == 0):
    print("Invalid step num")
    return 0
  if((type(yk) == type([])) or (type(yk) == type(np.asarray([])))):
    [xks, yks] = _explicit_system(f, xk, yk, x, stepnum)
  else:
    [xks, yks] = _explicit_single(f, xk, yk, x, stepnum)
  return [np.asarray(xks), np.asarray(yks)]


def implicit(f,xk,yk,x,stepnum,ite=50):
  print("Implicit Euler method:")
  if(stepnum == 0):
    print("Invalid step num")
    return 0
  if((type(yk) == type([])) or (type(yk) == type(np.asarray([])))):
    [xks, yks] = _implicit_system(f, xk, yk, x, stepnum, ite)
  else:
    [xks, yks] = _implicit_single(f, xk, yk, x, stepnum, ite)
  return [np.asarray(xks), np.asarray(yks)]


def _implicit_system(f,xk,yk,x,stepnum,ite=50):
  xks=[xk];  yks=[yk];  
  h = (x-xk)/stepnum;
  print("step h =", h)
  for i in range(0, stepnum):
    xk += h
    ybar = yk + h*np.asarray(f(xk, yk))
    for j in range(0, ite):
      ybar = yk + h*np.asarray(f(xk, ybar))
    yk = yk + h*np.asarray(f(xk, ybar))
    xks.append(xk); yks.append(yk)
  return [xks, yks]


def _implicit_single(f,xk,yk,x,stepnum, ite=50):
  xks=[xk];  yks=[yk];  
  h = (x-xk)/stepnum; 
  print("step h =", h)
  for i in range(0, stepnum):
    xk += h;
    ybar = yk + h*f(xk, yk)
    for j in range(0, ite):
      ybar = yk + h*f(xk, ybar)
    yk = yk + h*f(xk, ybar)
    xks.append(xk); yks.append(yk)
  print("y(", xk, ") = ", yk)
  return [xks, yks]
"""