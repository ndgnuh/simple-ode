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
  maxlen = len(str(round(yk[0][0],dec)))
  for yik in yk:
    for y in yik:
      maxlen = maxlen if maxlen > len(str(round(y,dec))) else len(str((round(y,dec))))
  cols = len(yk[0])
  print("xk".ljust(7), end="")
  for col in range(0, cols):
    print(("y"+ str(col) +"k").ljust(maxlen+3), end="", sep="")
  print("\n"+"-"*(cols+1)*(maxlen+3))
  for row in range(0, len(xk)):
    print(str(round(xk[row],4)).ljust(7), end="")
    for col in range(0, len(yk[0])):
      print(str(round(yk[row][col],dec)).ljust(maxlen+3), end="")
    print("")

def _scalar_result(xk, yk, dec=6):
  maxlen = len(str(round(yk[0],dec)))
  print(maxlen)
  for y in yk:
    maxlen = maxlen if maxlen > len(str(round(y,dec))) else len(str((round(y,dec))))
  print("xk".ljust(7), "yk".ljust(maxlen+3))
  print("-"*(7+(maxlen+3)))
  for i in range(0, len(xk)):
    print(str(round(xk[i],4)).ljust(7), end="")
    print(str(round(yk[i],dec)).ljust(maxlen+3))

  