def majority_element(nums):
    table = {}
    target = len(nums) / 3
    found = []
    for num in nums:
        if num in table:
            table[num] += 1
        else:
            table[num] = 1

        if table[num] > target:
            if num not in found:
                found.append(num)
    return found


nums = [3, 2, 3]

print('should be', [3], majority_element(nums))

nums = [1]

print('should be', [1], majority_element(nums))

nums = [1, 2]

print('should be', [1, 2], majority_element(nums))
