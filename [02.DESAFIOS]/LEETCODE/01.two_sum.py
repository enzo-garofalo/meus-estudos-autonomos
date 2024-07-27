# Given an array of integers nums and an integer target, 
# return indices of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution, 
# and you may not use the same element twice.

# You can return the answer in any order.

nums = [3,2,4]
target = 6

def twoSum(nums, target):
    seen = {}
    for i_first, first in enumerate(nums):
        seen[i_first] = first
        for i_second, second in enumerate(nums):
            if (first + second) == target and i_second not in seen.keys():
                return[i_first, i_second]

print(twoSum(nums, target))