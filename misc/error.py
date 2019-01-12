from numpy import average, array

def error_eval(xs, ys):
  """evaluate error 
  xs = [x1, x2, x3, ...] (list)
  ys = [y1, y2, y3, ...]
  """
  d = []; avg_err = [];
  n = len(xs)
  x_set = set(xs[0])

  if(n != len(ys)):
    print("Error: unmatch length")
    return False
  if(n < 2):
    print("Error: need more than 1 set of (x,y)")
    return False 

  for i in range(0, n):
    d.append(dict(zip(xs[i], ys[i])))
    x_set = x_set.intersection(set(xs[i]))
  for x in x_set:
    err = 0  #temporary error of each d1 dict
    for i in range(0, n):
      for j in range(i+1, n):
        err += (array(d[i][x]) - array(d[j][x]))
    avg_err.append(err/n)
  return [list(x_set), avg_err]