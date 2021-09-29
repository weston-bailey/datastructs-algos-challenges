# return the list and the left and right indexes
def quick_sort(unsorted_list):
  length = len(unsorted_list)
  return sort(unsorted_list, 0, length - 1) 

def sort(unsorted_list, left_index, right_index):
  # base case
  if len(unsorted_list) == 1:
    return unsorted_list

  if left_index < right_index:
    par = partition(unsorted_list, left_index, right_index)
    sort(unsorted_list, left_index, par - 1),
    sort(unsorted_list, par + 1, right_index)
  
  return unsorted_list

def partition(unsorted_list, left_index, right_index):
  i = left_index  - 1
  for j in range(left_index, right_index):
    if unsorted_list[j] <= unsorted_list[right_index]:
      i += 1
      unsorted_list[i], unsorted_list[j] = unsorted_list[j], unsorted_list[i]

  unsorted_list[i + 1], unsorted_list[right_index] = unsorted_list[right_index], unsorted_list[i + 1]
  return i + 1