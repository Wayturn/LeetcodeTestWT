# Given an array of integers nums and an integer k, return the total number of subarrays whose sum equals to k.

# A subarray is a contiguous non-empty sequence of elements within an array.

 

# Example 1:

# Input: nums = [1,1,1], k = 2
# Output: 2
# Example 2:

# Input: nums = [1,2,3], k = 3
# Output: 2
 

# Constraints:

# 1 <= nums.length <= 2 * 10**4
# -1000 <= nums[i] <= 1000
# (-10)**7 <= k <= 10**7

# 暴力解:O(n²)
      
# ans = 0
# for 每個起點 i:
#     sum = 0
#     for 每個終點 j 從 i 到尾巴:
#         sum += nums[j]
#         如果 sum == k:
#             ans += 1
# return ans

# prefix sum法 O(n)

# Hint:prefixSum 的差值 = 兩點之間的區間和

class Solution:
    def subarraySum(self, nums, k):
        curr_sum = 0
        ans = 0
        dic = {0: 1}

        for num in nums:
            curr_sum += num
            target = curr_sum - k

            # 以前有多少個 prefixSum = target，就有多少段 subarray 和 = k
            if target in dic:
                ans += dic[target]          # ✅ 不是 +1，是 + 出現次數

            # 把「現在這個 curr_sum」記錄起來
            dic[curr_sum] = dic.get(curr_sum, 0) + 1   # ✅ key 應該是 curr_sum

        return ans
