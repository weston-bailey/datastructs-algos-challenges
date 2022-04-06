# Given an integer array nums and two integers k and t, return true if there are two distinct indices i and j in the array such that abs(nums[i] - nums[j]) <= t and abs(i - j) <= k.
def dupe(nums, k, t):
  table = {}
  for i, num in enumerate(nums):
    if num not in table:
      table[num] = i
    else:
      if abs(nums[i] - nums[table[num]]) <= t and abs(i - table[num]) <= k:
        return True
        
      table[num] = i
    print('is', i - table[num], 'less than or equalt to', k, i)
    print('is', nums[i] - nums[table[num]], 'less than or equalt to', t)
    print(abs(nums[i] - nums[table[num]]) <= t and abs(i - table[num]) <= k)
  return False

nums = [1,2,3,1]
k = 3
t = 0

print('should be', True, dupe(nums, k, t))

nums = [1,0,1,1]
k = 1
t =2

print('should be', True, dupe(nums, k, t))

nums = [1,5,9,1,5,9]
k = 2
t = 3

print('should be', False, dupe(nums, k, t))

nums = [8,7,15,1,6,1,9,15]
k = 1
t = 3

print('should be', True, dupe(nums, k, t))