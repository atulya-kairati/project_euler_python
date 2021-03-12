# A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

# a^2 + b^2 = c^2
# For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

# There exists exactly one Pythagorean triplet for which  a + b + c = 1000.
# Find the product abc.


# -----------------------------------------------------

def check_pathagorean_triplets():
  for c in range(5, 1000):
    for b in range(1, c):
      a = 1000 - (c + b) # given a +b + c = 1000
      if a*a + b*b == c*c:
        return a * b * c
    
    
def main():
  print(check_pathagorean_triplets())
      
    
if __name__ == '__main__':
  main()