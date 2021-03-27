# 145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.

# Find the sum of all numbers which are equal to the sum of the factorial of their digits.

# Note: As 1! = 1 and 2! = 2 are not sums they are not included.

# ------------------------------------------

# 2 : 10-99 : 2-725760
# 3: 100-999: 3-1088640
# 4: 1000-9999: 4-1.45e6
# 5: 1e5-99999:
# 6: 100000-999999: .-2177280
# 7: 1000000-9999999: .-2540160


# no of digits can't succeed 7 ( 
# they b/w 6 and 7 (since sum of factorial digit 
# can't exceed 2540160)

def get_factorial(num: int) -> int:
  f = num
  for i in range (2, num):
    f *= i
  print(num, '->', f)
  return f


factorial = {
  '9': get_factorial(9),
  '8': get_factorial(8),
  '7': get_factorial(7),
  '6': get_factorial(6),
  '5': get_factorial(5),
  '4': get_factorial(4),
  '3': get_factorial(3),
  '2': get_factorial(2),
  '1': get_factorial(1),
  '0': 1,
}


def main():
  s = 0 
  for i in range(10, 2540160 + 1):
    str_i = str(i)
    fsum = sum(map(lambda x: factorial[x], str(i)))
    if i == fsum:
      s += i
    print(i)
  print('sum is: ', s)


if __name__ == '__main__':
  main()
# print(sum(map(lambda x: factorial[x], str(145))))