# The divisors of 12 are: 1,2,3,4,6 and 12.
# The largest divisor of 12 that does not exceed the square root of 12 is 3.
# We shall call the largest divisor of an integer n that does not exceed the square root of n the pseudo square root (PSR) of n.
# It can be seen that PSR(3102)=47.

# Let p be the product of the primes below 190.
# Find PSR(p) mod 10^16.
from math import sqrt, floor
from functools import reduce

def primality(num: int) -> bool:
  if num % 2 == 0:
    return False
  for i in range(3, int(sqrt(num))+1, 2):
    if num % i == 0:
      return False
  return True
    

def gen_prime(limit: int):
  yield 2 
  for i in range(3, limit, 2):
    if primality(i):
      yield i


def pseudo_sqrt(number):
  for i in range(floor(sqrt(number)), 1, -1):
    print(i)
    if number % i == 0:
      return i
    
      
def main():
  primeProduct = reduce(
    lambda a, b: a*b,
    [i for i in gen_prime(190)]
  )
  print((primeProduct)) 
  
  
if __name__ == '__main__':
  main()
