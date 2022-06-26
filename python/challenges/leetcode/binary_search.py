"""
Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to search target in nums. If target exists, then return its index. Otherwise, return -1.

You must write an algorithm with O(log n) runtime complexity.



Example 1:

Input: nums = [-1,0,3,5,9,12], target = 9
Output: 4
Explanation: 9 exists in nums and its index is 4

Example 2:

Input: nums = [-1,0,3,5,9,12], target = 2
Output: -1
Explanation: 2 does not exist in nums so return -1



Constraints:

    1 <= nums.length <= 104
    -104 < nums[i], target < 104
    All the integers in nums are unique.
    nums is sorted in ascending order.

"""

def search(nums, target):
    # keep track of current index, starting at middle
    index = len(nums) // 2
    # loop list
    while True:
        print(index)
        # if middle is target, return index
        if nums[index] == target:
            return index
        # if middle is greater than target, split lower, finding middle of lower hald
        elif nums[index] > target:
            index = index // 2
        # if middle is less than target, split upper, finding middle of upper half
        elif nums[index] < target:
            index = (len(nums) - index) // 2
        else:
            return -1


    # if current is greater than len of nums or lower than 0, return -1
    return -1

# naive solve
# def search(nums, target):
#     # loop to end of list
#     for i, num in enumerate(nums):
#         # if the num is found, return the index
#         if num == target:
#             return i

#     # return -1 if not found
#     return -1

