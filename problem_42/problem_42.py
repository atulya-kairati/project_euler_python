# The nth term of the sequence of triangle numbers is given by, tn = ½n(n+1); so the first ten triangle numbers are:

# 1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

# By converting each letter in a word to a number corresponding to its alphabetical position and adding these values we form a word value. For example, the word value for SKY is 19 + 11 + 25 = 55 = t10. If the word value is a triangle number then we shall call the word a triangle word.

# Using words.txt, a 16K text file containing nearly two-thousand common English words, how many are triangle words?
from math import sqrt, floor
from json import loads
from string import ascii_uppercase


def get_char_pos(char):
  return ascii_uppercase.index(char) + 1
  

def get_word_num(word: str):
  return sum([get_char_pos(a) for a in word])


def check_trangularity(num: int) -> bool:
  index = floor(sqrt(2*num))
  if num == (index*(index+1))/2:
    return True
  return False

  
def main():
  with open('words.txt') as f:
    words = loads(f'[{f.read()}]')
    
  counter = 0
  for word in words:
    if check_trangularity(get_word_num(word)):
      counter += 1
  print(counter)
  
if __name__ == '__main__':
  main()
