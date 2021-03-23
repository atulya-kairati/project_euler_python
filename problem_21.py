# Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
# If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and each of a and b are called amicable numbers.

# For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

# Evaluate the sum of all the amicable numbers under 10000.


def prime_factors(num: int):
  factors = {}
  div = 2
  while num > 1:
    while num % div == 0:
      factors[div] = factors.get(div, 0) + 1
      num //= div
    div += 1
  return factors
  
  
def get_helper_array(factors: dict):
  arr = []
  for num, exp in factors.items():
    arr.append([num**i for i in range(exp+1)])
  return arr
  

def get_combination(lst1, lst2):
  return [i*j for i in lst1 for j in lst2]
  

def get_all_divisors(num: int):
  pfactors = prime_factors(num)
  print(pfactors)
  helper_array = get_helper_array(pfactors)
  print(helper_array)
  accumulator = helper_array[0]
  helper_array = helper_array[1:]
  for arr in helper_array:
    print(accumulator)
    accumulator = get_combination(arr, accumulator)
  
  return accumulator
  
  
def main():
  # print(get_all_divisors(5397346292805549782720214077673687806275517530364350655459511599582614290))
  print(get_all_divisors(539782666556665556672))
  # print(get_combination([1,2,3], [4,5,6]))
  # print(get_all_divisors(100))

if __name__ == '__main__':
  main()
