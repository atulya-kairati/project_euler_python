# def get_collatz_seq(number: int):
#   seq = [number]
#   while number > 1:
#     # print(number)
#     if number % 2 == 0:
#       number //= 2
#     else:
#       number = (3 * number + 1)
#     seq.append(number)
#   return seq

def get_collatz_seq_len(number: int):
  c = 1
  while number > 1:
    # print(number)
    if number % 2 == 0:
      number //= 2
    else:
      number = (3 * number + 1)
    c += 1
  return c


def main():
  max_seq_num = 2
  max_seq_len = 0
  for i in range(2, 1000000 + 1):
    seq_len = get_collatz_seq_len(i)
    if seq_len > max_seq_len:
      max_seq_len, max_seq_num = seq_len, i
  print(max_seq_num)
    
    
if __name__ == '__main__':
  main()