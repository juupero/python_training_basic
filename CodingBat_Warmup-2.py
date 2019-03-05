# string_times
# Given a string and a non-negative int n, return a larger string that is n copies of the original string.

def string_times(str, n):
  print(str * n)

string_times('Hi', 2)
string_times('Hi', 3)
string_times('Hi', 1)

# string_bits
# Given a string, return a new string made of every other char starting with the first, so "Hello" yields "Hlo".

def string_bits(str):
  string_bits_string = ""
  for x in range(len(str)):
    if x % 2 == 0:
      string_bits_string += str[x]
  print(string_bits_string)

string_bits('Hello') # 'Hlo'
string_bits('Hi') # 'H'
string_bits('Heeololeo') # 'Hello'

# string_splosion
# Given a non-empty string like "Code" return a string like "CCoCodCode".

def string_splosion(str):
  string_splosion_string = ""
  number_of_rounds = 0
  while number_of_rounds <= len(str):
    for x in range(number_of_rounds):
      string_splosion_string += str[x]
    number_of_rounds += 1
  print(string_splosion_string)

string_splosion('Code') # 'CCoCodCode'
string_splosion('abc') # 'aababc'
string_splosion('ab') # 'aab'

# last2
# Given a string, return the count of the number of times that a substring length 2 appears in the string and also as the last 2 chars of the string, so "hixxxhi" yields 1 (we won't count the end substring).

# # I don't understand the task.. maybe later.

# # last2('hixxhi') # 1
# # last2('xaxxaxaxx') # 1
# # last2('axxxaaxx') # 2

# array_count9
# Given an array of ints, return the number of 9's in the array.

def array_count9(nums):
  nines = 0
  for num in nums:
    if num == 9:
      nines += 1
  print(nines)

array_count9([1, 2, 9]) # 1
array_count9([1, 9, 9]) # 2
array_count9([1, 9, 9, 3, 9]) # 3

# array_front9
# Given an array of ints, return True if one of the first 4 elements in the array is a 9. The array length may be less than 4.

def array_front9(nums):
  rounds = 0
  array_length = len(nums)
  if array_length > 4:
    array_length = 4

  while rounds < array_length:
    if nums[rounds] == 9:
      return True
    rounds += 1
  return False

array_front9([1, 2, 9, 3, 4]) # True
array_front9([1, 2, 3, 4, 9]) # False
array_front9([1, 2, 3, 4, 5]) # False

# array123
# Given an array of ints, return True if the sequence of numbers 1, 2, 3 appears in the array somewhere.

def array123(nums):
  sequence_of_numbers = [1, 2, 3]
  for num in range(len(nums) - 2):
    if [nums[num], nums[num + 1], nums[num + 2]] == sequence_of_numbers:
      return True
  return False

array123([1, 1, 2, 3, 1]) # True
array123([1, 1, 2, 4, 1]) # False
array123([1, 1, 2, 1, 2, 3]) # True