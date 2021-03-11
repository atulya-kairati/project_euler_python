# A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

# Find the largest palindrome made from the product of two 3-digit numbers.

from math import sqrt

def is_palindrome(num: int) -> bool:
  if str(num) == str(num)[::-1]:
    return True
  return False


def palindrome_gen():
  max_limit = 999**2
  min_limit = 100**2
  for i in range(max_limit, min_limit - 1, -1):
    if is_palindrome(i):
      yield i



pal_gen = palindrome_gen()
for p in pal_gen:
  for j in range(100, int(sqrt(p))):
    if p % j == 0 and len(str(p // j)) == 3:
      print(p)
      quit()