import math

def merge_sort(unsorted_list):
  # base case
  if len(unsorted_list) < 2:
    return unsorted_list

  # split the list in half
  middle = math.floor(len(unsorted_list) * .5)
  left = unsorted_list[:middle]
  right = unsorted_list[middle:]

  return merge(merge_sort(left), merge_sort(right))

def merge(left, right):
  left_index, right_index = 0, 0
  sorted_list =[]
  while left_index < len(left) and right_index < len(right):
    if left[left_index] <= right[right_index]:
      sorted_list.append(left[left_index])
      left_index += 1
    else:
      sorted_list.append(right[right_index])
      right_index += 1

  sorted_list += left[left_index:]
  sorted_list += right[right_index:]
  return sorted_list 
