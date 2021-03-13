# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

# Find the sum of all the primes below two million.

from math import sqrt

def check_primality(number: int):
  if number == 2: return True
  if number % 2 == 0: return False
  for i in range(3, int(sqrt(number)) + 1, 2):
    if number % i == 0:
      return False
  return True

def sum_prime(limit: int):
  prime_sum = 2 # bcoz 2 is a prime num 
  for i in range(3, limit, 2):
    if check_primality(i):
      prime_sum += i
      print(i)
  print(prime_sum)
        
sum_prime(2000000)