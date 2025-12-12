# You are given an array of integers nums, there is a sliding window of size k which is moving from the very left of the array to the very right. You can only see the k numbers in the window. Each time the sliding window moves right by one position.

# Return the max sliding window.

 

# Example 1:

# Input: nums = [1,3,-1,-3,5,3,6,7], k = 3
# Output: [3,3,5,5,6,7]
# Explanation: 
# Window position                Max
# ---------------               -----
# [1  3  -1] -3  5  3  6  7       3
#  1 [3  -1  -3] 5  3  6  7       3
#  1  3 [-1  -3  5] 3  6  7       5
#  1  3  -1 [-3  5  3] 6  7       5
#  1  3  -1  -3 [5  3  6] 7       6
#  1  3  -1  -3  5 [3  6  7]      7
# Example 2:

# Input: nums = [1], k = 1
# Output: [1]
 

# Constraints:

# 1 <= nums.length <= 10^5
# -10^4 <= nums[i] <= 10^4
# 1 <= k <= nums.length


#pseudo

# result = []
# q = 空 deque  # 存 index，不是值

# for i from 0 到 len(nums)-1:

#     # 1. 把尾巴比較小的全部踢掉（維持遞減）
#     while q 不空 且 nums[i] >= nums[q[-1]]:
#         把 q 尾巴 pop 掉

#     # 2. 把當前 index 丟進去
#     q.append(i)

#     # 3. 如果最前面的 index 已經滑出 window，就踢掉
#     window_start = i - k + 1
#     if q[0] < window_start:
#         q.popleft()

#     # 4. 當 i >= k-1 時，每一步都可以記一個答案
#     if i >= k - 1:
#         result.append(nums[q[0]])

# return result


from collections import deque

class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        result = []
        q = deque()  # 存 index，且 nums[q] 由大到小

        for i in range(len(nums)):
            # 1) 維持遞減：把尾巴比 nums[i] 小的都踢掉
            while q and nums[i] >= nums[q[-1]]:
                q.pop()

            # 2) 加入當前 index
            q.append(i)

            # 3) 把滑出 window 的 index 踢掉
            window_start = i - k + 1
            while q and q[0] < window_start:
                q.popleft()

            # 4) i >= k-1 時，window 已成形，記錄最大值
            if i >= k - 1:
                result.append(nums[q[0]])

        return result