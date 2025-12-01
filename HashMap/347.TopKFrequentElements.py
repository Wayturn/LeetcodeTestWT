# Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

 

# Example 1:

# Input: nums = [1,1,1,2,2,3], k = 2

# Output: [1,2]

# Example 2:

# Input: nums = [1], k = 1

# Output: [1]

# Example 3:

# Input: nums = [1,2,1,2,1,2,3,1,3,2], k = 2

# Output: [1,2]

 

# Constraints:

# 1 <= nums.length <= 105
# -104 <= nums[i] <= 104
# k is in the range [1, the number of unique elements in the array].
# It is guaranteed that the answer is unique.
 

# 解法1 HashMap + 排序  O(n log n)

# Follow up: Your algorithm's time complexity must be better than O(n log n), where n is the array's size.

# 建立一個 dic 用來記錄每個數字出現次數

# for num in nums:
#     dic[num] = dic.get(num, 0) + 1

# 把 dic 依照「次數由大到小」排序

# 從排序後的結果取前 k 個 key，放進 result list

# return result

class Solution:
    def topKFrequent(self, nums, k):
        dic = {}

        # 計數
        for num in nums:
            dic[num] = dic.get(num, 0) + 1

        # 排序：依照 value（次數）由大到小
        sorted_items = sorted(dic.items(), key=lambda x: x[1], reverse=True)

        # 取前 k 個 key
        result = [item[0] for item in sorted_items[:k]]

        return result


# 解法2 HashMap + Bucket Sort O(n)

# pseudo

# 建立一個dic用來儲存數字和該數字出現的次數
# for num in nums:
#     dic[num]=dic.get(num:0)+1
# 建立bucket長度為len(nums)+1
# 查dic將對應數字出現次數丟進bucket
# 將bucket從後查回來將前k大數字加入result
# 回傳result

class Solution:
    def topKFrequent(self, nums, k):
        # Step 1: 建立 dic 計每個數字出現次數
        dic = {}
        for num in nums:
            dic[num] = dic.get(num, 0) + 1   # 注意這裡是逗號，不是冒號

        # Step 2: 建立 bucket，索引是「出現次數」
        bucket = [[] for _ in range(len(nums) + 1)]

        # Step 3: 把數字丟進對應次數的 bucket
        for num, freq in dic.items():
            bucket[freq].append(num)

        # Step 4: 從高頻往低頻掃，收集前 k 個
        result = []
        for freq in range(len(bucket) - 1, 0, -1):  # 從最大頻率往下
            for num in bucket[freq]:
                result.append(num)
                if len(result) == k:
                    return result
