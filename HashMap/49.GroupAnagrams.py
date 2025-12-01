# Given an array of strings strs,
# group the anagrams together. You can return the answer in any order.

# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase,
# typically using all the original letters exactly once.

# Example 1:

# Input: strs = ["eat","tea","tan","ate","nat","bat"]
# Output: [["bat"],["nat","tan"],["ate","eat","tea"]]


# Example 2:

# Input: strs = [""]
# Output: [[""]]


# Example 3:

# Input: strs = ["a"]
# Output: [["a"]]


# Constraints:

# 1 ≤ strs.length ≤ 10⁴

# 0 ≤ strs[i].length ≤ 100


# pseudo

# strs[i] consists of lowercase English letters.

# 建立一個 dict，key = 排序後的字串，value = 裝同組的 list

# for 每個 word in strs:
#     c = 排序 word 得到的新字串

#     如果 c 不在 dict：
#         建一個空 list 當 dict[c]

#     把 word 加進 dict[c]

# 最後回傳 dict 裡所有 value 的集合（2D list）

class Solution:
    def groupAnagrams(self, strs):
        dict = {}

        for ch in strs:
            key = ''.join(sorted(ch))      # 排序後當 key

            if key not in dict:
                dict[key] = [ch]           # 建一個新 list
            else:
                dict[key].append(ch)       # 加進去

        return list(dict.values())
