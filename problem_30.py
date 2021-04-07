# Find the sum of all the numbers that can be written as the sum of fifth powers of their digits.


def sum_nth_power(num: int, power: int):
  s = 0
  while num > 0:
    s += (num % 10)**power
    num //= 10
  return s


def main():
  p = 0
  s = 0
  power = 5
  while True:
    upper_limit = 10**(p + 1) - 1
    lower_limit = 10**p
    lower_limit = lower_limit if lower_limit != 1 else 2
    if sum_nth_power(upper_limit, power) < lower_limit:
      break
    for i in range(lower_limit, upper_limit + 1):
      if sum_nth_power(i, power) == i:
        print(i)
        s += i
    p += 1
  print(s)
  
  
if __name__ == '__main__':
  main()
