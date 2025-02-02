# There are comments with the names of
# the required functions to build.
# Please paste your solution underneath
# the appropriate comment.

# factorial
def factorial(n):
    if n<0:
        raise ValueError("ValueError")
    if n==0:
        return 1
    return n * (factorial(n-1))


# reverse
def reverse(string):
  if len(string) <= 1:
    return string
  return reverse(string[1:]) + string[:1]


# bunny
def bunny(count):
    if count == 0:
        return 0
    return 2 + bunny(count-1)


# is_nested_parens
def is_nested_parens(parens, left_index = 0):
    right_index = len(parens) - 1 - left_index
    if len(parens) == 0:
        return True
    if left_index >= right_index:
        return True
    if parens[right_index] == ")" and parens[left_index] == "(":
        return is_nested_parens(parens, left_index + 1)
    else:
        return False
    

