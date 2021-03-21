# Using names.txt a 46K text file containing over five-thousand first names, begin by sorting it into alphabetical order. Then working out the alphabetical value for each name, multiply this value by its alphabetical position in the list to obtain a name score.

# For example, when the list is sorted into alphabetical order, COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. So, COLIN would obtain a score of 938 × 53 = 49714.

# What is the total of all the name scores in the file?

import json


def word_sum(word: str):
  return sum(map(lambda c: ord(c) - 64, word))
  
  
def main():
  with open('names.txt') as file:
    name_list = json.loads('['+file.read()+']')
  
  name_list.sort()
  print(len(name_list))

  total_score = 0
  for index, name in enumerate(name_list):
    total_score += (index+1) * word_sum(name)
    
  print(total_score)


if __name__ == '__main__':
  main()
