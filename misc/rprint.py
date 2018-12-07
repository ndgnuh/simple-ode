from numpy import round, asarray

def result(xk, yk, dec=6):
  print("-"*30)
  if(type(yk[0]) == type([])):
    _system_result(xk, yk, dec)
    return 0
  if(type(yk[0]) == type(asarray([]))):
    _system_result(xk, yk, dec)
    return 0
  _scalar_result(xk, yk, dec)

def _system_result(xk, yk, dec):
  cols = len(yk[0])
  print("xk".ljust(dec+5), end="")
  for col in range(0, cols):
    print(("y"+ str(col) +"k").ljust(dec+5), end="", sep="")
  print("\n"+"-"*(cols+1)*(dec+5))
  for row in range(0, len(xk)):
    print(str(round(xk[row],dec)).ljust(dec+5), end="")
    for col in range(0, len(yk[0])):
      print(str(round(yk[row][col],dec)).ljust(dec+5), end="")
    print("")

def _scalar_result(xk, yk, dec=6):
  print("xk".ljust(10), "yk".ljust(10))
  print("-"*30)
  for i in range(0, len(xk)):
    print(str(round(xk[i],dec)).ljust(dec+5), end="")
    print(str(round(yk[i],dec)).ljust(dec+5))