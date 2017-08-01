""" 
    Given an array of integers, write a function that returns true 
    if there is a triplet (a, b, c) that satisfies a^2 + b^2 = c^2.
"""

def has_pythagorean_triplet1(arr):
  """ Solution using hashing.

      arr: a list of integers
      Returns True if the given array contains a triplet
  """

  arr = set([i**2 for i in arr])
  found = False
  
  for i in arr:
    for j in arr:
        if i != j:
            if i + j in arr:
                found = True
                break
    if found:
        break

  if found:
      print("Yes")
  else:
      print("No")


def has_pythagorean_triplet2(arr):
  """ Solution using sorting and meet in the middle algorithm.

      arr: a list of integers
      Returns True if the given array contains a triplet 
  """
  arr = [i**2 for i in arr]
  arr.sort()

  for i in range(len(arr) - 1, 1, -1):
    l = 0
    r = i - 1
    while l <= r:
      if arr[l] + arr[r] == arr[i]:
        return True
      elif arr[l] + arr[r] < arr[i]:
        l += 1
      else:
        r -= 1
  return False


arr = [3,2,4,6,5]
has_pythagorean_triplet1(arr)
has_pythagorean_triplet2(arr)