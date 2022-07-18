'''
https://leetcode.com/problems/find-pivot-index/
724. Find Pivot Index
Easy

Given an array of integers nums, calculate the pivot index of this array.

The pivot index is the index where the sum of all the numbers strictly to the left of the index is equal to the sum of all the numbers strictly to the index's right.

If the index is on the left edge of the array, then the left sum is 0 because there are no elements to the left. This also applies to the right edge of the array.

Return the leftmost pivot index. If no such index exists, return -1.



Example 1:

Input: nums = [1,7,3,6,5,6]
Output: 3
Explanation:
The pivot index is 3.
Left sum = nums[0] + nums[1] + nums[2] = 1 + 7 + 3 = 11
Right sum = nums[4] + nums[5] = 5 + 6 = 11

Example 2:

Input: nums = [1,2,3]
Output: -1
Explanation:
There is no index that satisfies the conditions in the problem statement.

Example 3:

Input: nums = [2,1,-1]
Output: 0
Explanation:
The pivot index is 0.
Left sum = 0 (no elements to the left of index 0)
Right sum = nums[1] + nums[2] = 1 + -1 = 0



Constraints:

    1 <= nums.length <= 104
    -1000 <= nums[i] <= 1000



Note: This question is the same as 1991: https://leetcode.com/problems/find-the-middle-index-in-array/
'''

def pivot_index(nums):
    # to keep track of nums to the left of it
    left = 0
    for i in range(len(nums)):
        # for every num, loop to end of nums and find the sum to the right
        right = sum(nums[i + 1:])
        # compare left and right sum 
        # if the are equal, return the current index
        if right == left:
            return i
        # keep track left sum for next iteration
        left += nums[i]

    # if we reach the end of the nums, return -1, condition not satisfied
    return -1

def main():
    nums = [1,7,3,6,5,6]
    print(pivot_index(nums)) # 3
    nums = [1,2,3]
    print(pivot_index(nums)) # -1
    nums = [2,1,-1]
    print(pivot_index(nums)) # 0
    nums = [-1,-1,-1,-1,-1,-1]
    print(pivot_index(nums)) # -1

if __name__ == '__main__':
    main()
