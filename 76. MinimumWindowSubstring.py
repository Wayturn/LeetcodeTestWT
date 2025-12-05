# Given two strings s and t of lengths m and n respectively, return the minimum window substring of s such that every character in t (including duplicates) is included in the window. If there is no such substring, return the empty string "".

# The testcases will be generated such that the answer is unique.

 

# Example 1:

# Input: s = "ADOBECODEBANC", t = "ABC"
# Output: "BANC"
# Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.
# Example 2:

# Input: s = "a", t = "a"
# Output: "a"
# Explanation: The entire string s is the minimum window.
# Example 3:

# Input: s = "a", t = "aa"
# Output: ""
# Explanation: Both 'a's from t must be included in the window.
# Since the largest window of s only has one 'a', return empty string.


# Constraints:

# m == s.length
# n == t.length
# 1 <= m, n <= 10^5
# s and t consist of uppercase and lowercase English letters.
 

# Follow up: Could you find an algorithm that runs in O(m + n) time?

#pseudo

# dic_={紀錄t內元素}
# left=0
# win=""
# ans=""
# list_win=[]
# for right in range(len(s)-1)
#     將s[right]加入win
#     用dic_t去檢查 win 內全部元素，若有符合項則將dic_t內該元素value值-1
#     判斷dic_t內是否全部key值的value值皆為0
#     若是則將win加入list_win

# ans= min(list_win)
# return ans

#修正pseudo
# 建立 need = {}  # 統計 t 內每個字需要幾個
# for 每個字 ch 在 t:
#     need[ch] = need.get(ch, 0) + 1

# window = {}      # 紀錄目前 window 內每個字有幾個
# left = 0
# valid = 0        # 有幾個字元已經達到 need 的數量要求
# start = 0        # 最佳答案的起點
# min_len = 無限大

# for right 從 0 到 len(s) - 1:
#     c = s[right]

#     # 右邊擴張 window，把 c 加進來
#     if c 在 need 裡:
#         window[c] = window.get(c, 0) + 1
#         如果 window[c] == need[c]:
#             valid += 1

#     # 當前 window 已經「包含 t 所有字元」時 → 盡量縮左邊
#     while valid == need 的 key 數量:
#         current_len = right - left + 1
#         如果 current_len < min_len:
#             min_len = current_len
#             start = left

#         # 準備移除最左邊的字
#         d = s[left]
#         left += 1

#         if d 在 need 裡:
#             window[d] -= 1
#             如果 window[d] < need[d]:
#                 valid -= 1   # 表示這個字又不達標了，window 不再合法

# 如果 min_len 還是無限大:
#     回傳 ""
# 否則:
#     回傳 s[start : start + min_len]

class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        need={}
        for ch in t:
            need[ch]=need.get(ch,0)+1
        window={} # 紀錄目前window內每個字有幾個          
        left=0       
        valid=0
        start=0
        min_len=float('inf')
        for right in range(len(s)):
            c=s[right]
            if c in need:
                window[c]=window.get(c,0)+1
                if window[c] == need[c]:
                    valid+=1
            while valid == len(need):
                current_len = right - left + 1
                if current_len < min_len:
                    min_len = current_len
                    start =left

                d=s[left]
                left+=1

                if d in need:
                    window[d] -= 1
                    if window[d] < need[d] :
                        valid -=1
        if min_len==float('inf'):
            return ""
        else:
            return s[start : start + min_len]