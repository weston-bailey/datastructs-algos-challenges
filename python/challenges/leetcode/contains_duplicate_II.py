# Given an integer array nums and an integer k, return true if there are two distinct indices i and j in the array such that nums[i] == nums[j] and abs(i - j) <= k.

def dupe(nums, k):
    table = {}
    for i, num in enumerate(nums):
        if num not in table:
            table[num] = i
        else:
            print(abs(i - table[num]) <= k)
            if abs(i - table[num]) <= k:
                return True

            table[num] = i
    return False


nums = [1, 2, 3, 1]
k = 3

print('should be', True, dupe(nums, k))

nums = [1, 2, 3, 1, 2, 3]
k = 2

print('should be', False, dupe(nums, k))

nums = [1, 0, 1, 1]
k = 1

print('should be', True, dupe(nums, k))
