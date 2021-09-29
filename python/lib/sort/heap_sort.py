def heap_sort(unsorted_list):
  length = len(unsorted_list)

  build_heap(unsorted_list, length)

  for i in range(length - 1, 0, -1):
    unsorted_list[0], unsorted_list[i] = unsorted_list[i], unsorted_list[0]

    heapify(unsorted_list, i, 0)

  return unsorted_list
  

def build_heap(unsorted_list, length):
  for i in range(length // 2, -1, -1):
    heapify(unsorted_list, length, i)

def heapify(unsorted_list, size, root_index):
  largest = root_index
  left = 2 * root_index + 1
  right = 2 * root_index + 2

  if(left < size and unsorted_list[left] > unsorted_list[largest]):
    largest = left
  if(right < size and unsorted_list[right] > unsorted_list[largest]):
    largest = right
  
  if(root_index != largest):
    unsorted_list[largest], unsorted_list[root_index] = unsorted_list[root_index], unsorted_list[largest]
    heapify(unsorted_list, size, largest)