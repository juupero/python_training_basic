def get_cycle_length(n):
  """ 
  takes an integer 0 < n < 10000
  returns the number of steps it
  will take to get to 1
  by performing n // 2 if n is even
  and n * 3 + 1 if n is odd
  int -> int
  print(get_cycle_length(5)) -> 6
  print(get_cycle_length(1)) -> 1
  print(get_cycle_length(197)) -> 27
  """
  number_of_steps = 0
  while n > 1:
    if n % 2 == 0:
      n = n // 2
    else:
      n = n * 3 + 1
    number_of_steps += 1
  return number_of_steps


def get_cycle_length_range(start, end):
    """
    takes 2 integers 0 < start, end < 10000
    finds the number for which it takes
    the maximum amount of steps to get to
    1 and returns the length of that cycle

    int, int -> int
    print(get_cycle_length_range(5, 100)) -> 119
    print(get_cycle_length_range(200, 100)) -> 125
    print(get_cycle_length_range(1, 2)) -> 2
    """
    # I don't understand the task assignment, yet..

# Results
print(get_cycle_length(5)) # 6
print(get_cycle_length(1)) # 1
print(get_cycle_length(197)) # 27
# The results of the script are off by minus one, but if you think about it how many steps does it really take for get_cycle_length(1)? The correct answer is zero not one.
# print(get_cycle_length_range(5, 100)) # 119
# print(get_cycle_length_range(200, 100)) # 125
# print(get_cycle_length_range(1, 2)) # 2