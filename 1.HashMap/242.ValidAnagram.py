# Given two strings s and t, return true if t is an anagram of s,
# and false otherwise.

# An Anagram is a word or phrase formed by rearranging the letters of another,
# using all the original letters exactly once.

# Example 1:

# Input: s = "anagram", t = "nagaram"
# Output: true


# Example 2:

# Input: s = "rat", t = "car"
# Output: false


# Constraints:

# 1 ≤ s.length, t.length ≤ 5×10⁴

# s and t consist of lowercase English letters.

# pseudo

# 先判斷兩個字串長度是否相等
# 若不相等則回傳false

# 建立一個dict

# for s 紀錄每個字母
#     dict[字母] 次數+1
# for t 裡每個字母
#     dict[字母] 次數-1
#     如果減完 有負數
#     則回傳false
# 檢查dict裡所有值是否為0
# 如果是回傳True
# 否則False

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        # 長度不一樣一定不是
        if len(s) != len(t):
            return False

        # 建立字典統計字頻
        count = {}

        # s 裡每個字加分
        for ch in s:
            count[ch] = count.get(ch, 0) + 1

        # t 裡每個字扣分
        for ch in t:
            if ch not in count:
                return False
            count[ch] -= 1
            if count[ch] < 0:
                return False

        # 最後檢查全部是不是歸零
        for v in count.values():
            if v != 0:
                return False

        return True
