def bubble_sort_1(unsorted_list):
    '''
      bubble_sort_1(li) -> li:\n
      accepts an unsorted list and sorts it in place -- returns the sorted list\n
      uses a while loop
    '''
    # flags for sort loop
    is_sorted = False
    made_swap = False

    while is_sorted is False:
        # interate in range of list length - 1 to avoid looking up indexes that are out of range
        for i in range(len(unsorted_list) - 1):
            # swap list elements if first element is greater than second element
            if unsorted_list[i] > unsorted_list[i + 1]:
                unsorted_list[i], unsorted_list[i +
                                                1] = unsorted_list[i + 1], unsorted_list[i]
                # set swap flag to true so the list is checked again
                made_swap = True

            # check if any swaps were made at the end of the for loop
            if i == len(unsorted_list) - 2:
                if made_swap is False:
                    is_sorted = True
                # break the while loop if no swaps were made
                else:
                    made_swap = False

    return unsorted_list


def bubble_sort_2(unsorted_list):
    '''
      bubble_sort_2(li) -> li:\n
      accepts an unsorted list and sorts it in place -- returns the sorted list\n
      uses a for loop
    '''
    # flag for sort loop
    made_swap = False
    # interate in range of list length - 1 to avoid looking up indexes that are out of range
    for i in range(len(unsorted_list) - 1):
        # swap list elements if first element is greater than second element
        if unsorted_list[i] > unsorted_list[i + 1]:
            unsorted_list[i], unsorted_list[i +
                                            1] = unsorted_list[i + 1], unsorted_list[i]
            # set swap flag to true so the list is checked again
            made_swap = True

    return unsorted_list

# takes a list and recursively sorts it


def bubble_sort_3(unsorted_list):
    '''
      bubble_sort_3(li) -> li:\n
      accepts an unsorted list and sorts it in place -- returns the sorted list\n
      uses a recursion
    '''
    return unsorted_list
