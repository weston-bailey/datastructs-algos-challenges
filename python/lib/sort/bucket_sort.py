import math
from .insertion_sort import insertion_sort

# accepts an unsorted list and the number of buckets to use (k)
# only works with positive vales
def bucket_sort(unsorted_list, num_buckets=2, sort_algorithm=insertion_sort):
  # make the buckets
  buckets = []
  for _ in range(num_buckets + 1): buckets.append([])

  # calculate the size of each bucket
  highest = max(unsorted_list)
  # find distance between highest and loweest value for negetive values
  # distance = abs(max(unsorted_list) - min(unsorted_list))

  # place elements in buckets
  for i in range(len(unsorted_list)):
    bucket_index = math.floor((num_buckets / highest) * unsorted_list[i])
    buckets[bucket_index].append(unsorted_list[i])
    
  # sort each bucket and add it to the sorted list
  unsorted_list.clear()
  for i in range(num_buckets): unsorted_list.extend(sort_algorithm(buckets[i]))
  unsorted_list.extend(buckets[-1])
  
  return unsorted_list
