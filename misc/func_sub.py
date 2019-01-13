def func_sub(f, x0):
  """f(x, y) -> f(x0, y)
  """
  return lambda y: f(x0, y)