from numpy import round, asarray

def result(xk, yk):
  print("-"*30)
  if(type(yk[0]) == type([])):
    _system_result(xk, yk)
    return 0
  if(type(yk[0]) == type(asarray([]))):
    _system_result(xk, yk)
    return 0
  _scalar_result(xk, yk)

def _system_result(xk, yk):
  cols = len(yk[0])
  print("xk".ljust(10), end="")
  for col in range(0, cols):
    print(("y"+ str(col) +"k").ljust(10), end="", sep="")
  print("\n"+"-"*(cols+1)*10)
  for row in range(0, len(xk)):
    print(str(round(xk[row],4)).ljust(10), end="")
    for col in range(0, len(yk[0])):
      print(str(round(yk[row][col],4)).ljust(10), end="")
    print("")

def _scalar_result(xk, yk):
  print("xk".ljust(10), "yk".ljust(10))
  print("-"*30)
  for i in range(0, len(xk)):
    print(str(round(xk[i],4)).ljust(10), end="")
    print(str(round(yk[i],4)).ljust(10))