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
from time import sleep

def search(nums, target):
    low = 0
    high = len(nums)
    mid = high // 2
    if nums[low] == target:
        return low
    if nums[high - 1] == target:
        return high - 1
    while True:
        # print('==================')
        # print(f'target: {target}')
        # print(f'nums: {nums}')
        # print(f'low: {low}, mid: {mid}, high: {high}')
        # print(f'current index: {nums[mid]}')
        # if mid is target
        if nums[mid] == target:
            return mid
        # if we are moving down
        elif nums[mid] > target:
            # move high down to current mid, recalc mid
            high = mid
            mid = high // 2
        # if we are moving up
        elif nums[mid] < target:
            # move low up to mid, recalc mid
            low = mid
            # need to know the difference between high and new low
            diff = high - low
            # find the mid point of the diff, add to low to get new mid
            mid = low + (diff // 2)
        else:
            # print(f'no case matched, low: {low}, mid: {mid}, high: {high}')

        # sleep(1)
        # if we are out of bounds
        if mid == low or mid == high:
            # print('mid out of bounds')
            # print(f'low: {low}, mid: {mid}, high: {high}')
            return -1
        if low >= high or high <= low:
            # print('low ord high out of bounds')
            # print(f'low: {low}, mid: {mid}, high: {high}')
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

