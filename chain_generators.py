# Write a program to chain generators?

def count_up_to(max):
  count=1
  while count <=max:
    yield count
    count+=1

def squared_numbers(numbers):
  for number in number:
    yield number**2
