def selection_sort(li):
  # loop over list
  for index in range(len(li) - 1):
    # We first assume that the first element is the lowest
    min_index = index
    # loop through the remaining elements
    for cur_pos in range(index + 1, len(li)):
      # Update the min_index if the element at cur_pos is lower than it
      # update the min_index if a smaller value is found at the current position
      if li[cur_pos] < li[min_index]:
        min_index = cur_pos
    # After finding the lowest item of the unsorted regions, swap with the first unsorted item
    li[index], li[min_index] = li[min_index], li[index]
  return li