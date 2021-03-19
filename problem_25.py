def gen_fib():
  a, b = 0, 1
  yield a
  while 1:
    yield b
    a, b = b, b + a
    
def main():
  fibs = gen_fib()
  i = 0
  while 1:
    f = next(fibs)
    if len(str(f)) == 1000:
      break
    i += 1
  print(i)
  
  
if __name__ == '__main__':
  main()