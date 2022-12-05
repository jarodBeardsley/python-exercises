################
# Main Program #
################
if __name__ == '__main__':
  def fibonacci(n):
  """Implements Fibonacci calculation using dynamic programming for O(n) runtime"""
  a = 0
  b = 1
    if n < 0:
      print("Incorrect input")
    elif n == 0:
      return a
    elif n == 1:
      return b
    else:
      for i in range(2, n+1):
        c = a + b
        a = b
        b = c
      return b
     
