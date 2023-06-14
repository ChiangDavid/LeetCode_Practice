#Using normal recursion
#O(2^n)

def fib(self, n: int) -> int:
  if n <= 1:
    return n
  return self.fib(n-1) + self.fib(n-2)
      
  
#Using memorization to store already seen result
def fib(self, n: int) -> int:
  dict = {}
  if n == 0:
    dict[n] = 0
   if n == 1:
    dict[n] = 1
   if n in dict:
    return dict[n]
   else:
      dict[n] = self.fib(n-1) + self.fib(n-2)
      return dict[n]
