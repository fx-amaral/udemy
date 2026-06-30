iterable = [1 , 5 , 7 , 8 , 'casa']
iterator = iter(iterable)  # tem __iter__ e __next__

# try:
#   while True:
#     print(next(iterator))

# except:
#   StopIteration

for n in iterator:
  print(n)  


# generator = (n for n in range(50))
# for n in generator:
#   print(n)  

def generator(n=0):
  yield 1
  return 'Acabou'

gen = generator(n=0)
print(gen)