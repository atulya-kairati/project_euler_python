# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

# -----------------------------------------------------
# Algorithm working
# save the prime factors of the limit then
# see if all the prime factor of limit-1 exist in 
# saved factors or not if not save the required 
# factors so that all the factors of limit - 1 exist 
# but not more, continue this to 1
# take product of all saved factors

def gen_prime_factor(number):
  factor = dict() # {number: exponent}
  div = 2
  while number > 1:
    while number % div == 0:
      factor[div] = factor.get(div, 0) + 1;
      number /= div
    div += 1
  return factor
  
def main():
  limit = 20
  multiple = {}
  for i in range(limit, 0, -1):
    for num, expo in gen_prime_factor(i).items():
      if multiple.get(num, 0) < expo:
        multiple[num] = expo
  result = 1
  for num, expo in multiple.items():
    result *= num**expo
  print(result)
  
if __name__ == '__main__':
  main()

# 232792560