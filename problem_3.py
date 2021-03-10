# The prime factors of 13195 are 5, 7, 13 and 29.

# What is the largest prime factor of the number 600851475143 ?


factors = dict()
num = 600851475143
div = 2

while num > 1:
  while num % div == 0:
    factors[div] = factors.get(div, 0) + 1
    num /= div
  div += 1

print(max(factors.keys()))
# 6857