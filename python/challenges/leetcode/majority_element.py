def majority_element(nums):
  table = {}
  target = len(nums) / 2
  for num in nums:
    if num in table:
      table[num] += 1
    else:
      table[num] = 1

    if table[num] >= target:
      return num


nums = [3,2,3]

print('it should be', 3, majority_element(nums))

nums = [2,2,1,1,1,2,2]

print('it should be', 2, majority_element(nums))
