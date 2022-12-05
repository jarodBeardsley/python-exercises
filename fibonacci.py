################
# Main Program #
################
def fibonacci(n):
  """Implements Fibonacci calculation using dynamic programming for O(n) runtime"""
  a = 0
  b = 1
  if n < 0:
    print("Invalid input: input must be greater than -1")
  elif n <= 1:
    return n
  else:
    for i in range(2, n+1):
      c = a + b
      a = b
      b = c
  return b
     
