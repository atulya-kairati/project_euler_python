# The series, 1^1 + 2^2 + 3^3 + ... + 10^10 = 10405071317.

# Find the last ten digits of the series, 1^1 + 2^2 + 3^3 + ... + 1000^1000.

def main():
  limit = 1000
  s = sum([i**i for i in range(1, limit + 1)])
  print(s % 10**10)  # printing last 10 digits
  
  
if __name__ == '__main__':
  main()
