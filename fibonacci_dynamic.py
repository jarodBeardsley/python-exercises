def fib(int n):
  if(n<=1):
    return n

  if(fib(n) != -1):
    return fib(n)

  int res = fib(n-1) + fib(n-2)

  fib(n) = res

  return res
