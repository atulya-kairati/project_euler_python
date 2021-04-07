# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

# What is the 10 001st prime number?

def is_prime(num: int):
  if num < 2:
    return False
  elif num == 2:
    return True
  elif num % 2 == 0:
    return False
  else:
    for i in range(3, num, 2):
      if num % i == 0:
        return False
  return True

def gen_prime():
  i = 2
  while True:
    if is_prime(i):
      yield i
    i += 1
      
      
def main():
  primes = gen_prime()
  for _ in range(10000):
    print(next(primes))
  print(next(primes))
    
    
if __name__ == '__main__':
  main()