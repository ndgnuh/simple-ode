def error_compare(y, xk, y1, y2):
  e1 = e2 = 0
  print("xk".ljust(10), "sai số (h = 1)".ljust(20), "sai số (h = 0.2)")
  for i in range(0, x1.size):
    x = x1[i]
    e1 += np.abs(y1[i] - y(x))
    e2 += np.abs(y2[i] - y(x))
    print(str(x.round(4)).ljust(10), end="| ")
    print(str((y1[i] - y(x)).round(4)).ljust(20), end="| ")
    print(str((y2[i] - y(x)).round(4)).ljust(20))
  print("e1:", e1, "e2:", e2)

