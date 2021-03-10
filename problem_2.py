# Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with 1 and 2, the first 10 terms will be:

# 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

# By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.

def gen_fibonacci():
  a, b = 1, 1
  while True:
    yield b
    a, b = b, a + b

sum_of_even_terms = 0    
for num in gen_fibonacci():
  if num > 4000000:
    break
  sum_of_even_terms += num if num % 2 == 0 else 0
  
print(sum_of_even_terms)
    
# 4613732