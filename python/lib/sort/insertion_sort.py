def insertion_sort(li):
    # iterate through list and move elements down if they are less than the element to the left
    for index in range(len(li)):
        # current number for comaprisons
        current_number = li[index]
        # use while loop to go back down the list
        cur_pos = index - 1
        while cur_pos >= 0 and current_number < li[cur_pos]:
            # swap the values
            li[cur_pos], li[cur_pos + 1] = li[cur_pos + 1], li[cur_pos]
            # print(f'index: {index} current poition: {cur_pos} comparison: {current_number} < {li[cur_pos]} {li}', end='\r')
            # time.sleep(.5)
            cur_pos -= 1

    return li

# not working


def insertion_sort_2(unsorted_list):

    for i in range(len(unsorted_list)):
        sort_recursive(unsorted_list, i)

    return unsorted_list


def sort_recursive(unsorted_list, index):
    # base case
    if index <= 0:
        return unsorted_list
    if unsorted_list[index] < unsorted_list[index - 1]:
        unsorted_list[index -
                      1], unsorted_list[index] = unsorted_list[index], unsorted_list[index - 1]
        return sort_recursive(unsorted_list, index - 1)
