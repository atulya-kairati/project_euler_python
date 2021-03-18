def factorial(num: int):
  f = 1
  for i in range(1, num + 1):
    f *= i
  return f
  
print(sum(map(int, list(str(factorial(100))))))