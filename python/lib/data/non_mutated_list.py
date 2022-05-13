def non_mutated_list(li, callback, *args, **kwargs):
    '''
      non_mutated_list([list], <function>) -> [list]:\n
      instead of sorting in place, non_mutated_list() returns a new sorted list without changing the unsorted one
    '''
    new_list = li.copy()
    return callback(new_list, *args, **kwargs)
