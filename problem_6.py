# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

n2_sum = sum_n = 0
for i in range (1, 101):
  n2_sum += i**2 
  sum_n += i
print(sum_n**2 - n2_sum)