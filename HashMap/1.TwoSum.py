# Given an array of integers nums and an integer target,
# return indices of the two numbers such that they add up to target.

# You may assume that each input would have exactly one solution,
# and you may not use the same element twice.

# You can return the answer in any order.

# Example 1:

# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].


# Example 2:

# Input: nums = [3,2,4], target = 6
# Output: [1,2]


# Example 3:

# Input: nums = [3,3], target = 6
# Output: [0,1]


# Constraints:

# 2 ≤ nums.length ≤ 10⁴

# −10⁹ ≤ nums[i] ≤ 10⁹

# −10⁹ ≤ target ≤ 10⁹

# Only one valid answer exists

# 建立一個 dict，用來記錄「我已經看過的數字 → 他的 index」

# for i, num in nums:
#     diff = target - num
#     如果 diff 在 dict 裡：
#         # 代表之前看過的「那個數字」 + 現在的 num = target
#         回傳 [dict[diff], i]

#     # 不然的話，記錄現在這個 num
#     dict[num] = i

class Solution:
    def twoSum(self, nums, target):
        dict = {}

        for i, num in enumerate(nums):
            diff = target - num

            if diff in dict:
                return [dict[diff], i]

            dict[num] = i
