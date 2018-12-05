import numpy as np
def trapezoidal(f, xk, yk, x, stepnum):
  print("\nTrapezoidal predictor-corrector method.")
  try:
    if(stepnum <= 0):
      print("invalid number of steps!")
      return 0
    h = (x - xk) / stepnum
    print("step h =",h)
    xks = [xk]
    yks = [yk]
    print("xk", "".ljust(5), "yk", "".ljust(25))
    for i in range(0, stepnum):
      # Predictor
      f0 = f(xk, yk)
      ybar = yk + h * f0 

      # Corrector
      xk = xk + h
      yk = yk + h/2*(f0 + f(xk, ybar))
      yks.append(yk)
      xks.append(xk)
      print(str(np.round(xk,3)).ljust(5) , " | ", str(yk).ljust(25))
    print(str(np.round(xk,3)).ljust(5) , " | ", str(yk).ljust(25))
    return [np.asarray(xks, dtype="complex"),np.asarray(yks, dtype="complex")]
  except RuntimeError:
    print("Unable to solve, failed to converge")
    return [np.asarray(xks, dtype="complex"),np.asarray(yks, dtype="complex")]
