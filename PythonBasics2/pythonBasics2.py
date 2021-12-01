# Python Activity
#
# Fill in the code for the functions below.
# The starter code for each function includes a 'return'
# which is just a placeholder for your code. Make sure to add what is going to be returned.


# Part A. count_threes
# Define a function count_threes(n) that takes an int and
# returns the number of multiples of 3 in the range from 0
# to n (including n).

def count_threes(n):
    # YOUR CODE HERE
    return int (n/3)


# Part B. longest_consecutive_repeating_char
# Define a function longest_consecutive_repeating_char(s) that takes
# a string s and returns the character that has the longest consecutive repeat.
def longest_consecutive_repeating_char(s):
  l = len(s)
  count = 1
  max = 1
  ch = s[0]
  for i in range(0, l -1):
    if s[i] == s[i + 1]:
      count += 1
    else:
      if count > max:
        max = count
        ch = s[i]
      count = 1
  if count > max:
    max = count
    ch = s[i]

  return ch


# Part C. is_palindrome
# Define a function is_palindrome(s) that takes a string s
# and returns whether or not that string is a palindrome.
# A palindrome is a string that reads the same backwards and
# forwards. Treat capital letters the same as lowercase ones
# and ignore spaces (i.e. case insensitive).
def is_palindrome(s):
  x = 0
  l = len(s) - 1
  while x <= l:
    if s[x] == '':
      x+=1
      continue
    if s[l] =='':
      l-=1
      continue
    if s[x].lower() != s[l].lower():
      return False
    x+=1
    l-=1
  return True


