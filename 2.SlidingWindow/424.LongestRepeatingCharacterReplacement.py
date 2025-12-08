#  You are given a string s and an integer k. You can choose any character of the string and change it to any other uppercase English character. You can perform this operation at most k times.

# Return the length of the longest substring containing the same letter you can get after performing the above operations.

 

# Example 1:

# Input: s = "ABAB", k = 2
# Output: 4
# Explanation: Replace the two 'A's with two 'B's or vice versa.
# Example 2:

# Input: s = "AABABBA", k = 1
# Output: 4
# Explanation: Replace the one 'A' in the middle with 'B' and form "AABBBBA".
# The substring "BBBB" has the longest repeating letters, which is 4.
# There may exists other ways to achieve this answer too.
 

# Constraints:

# 1 <= s.length <= 10^5
# s consists of only uppercase English letters.
# 0 <= k <= s.length


# pesudo first

# left=0
# win=[]
# max_len=0
# dic_win={A:0,B:0}
# for right in range len(s):
#     win加入s[right]
#     dic_win[s[right]]=get.dic_win(s[right],0)+1
#     用dic進行判斷
#     (A or B)的value值一定要有一個小於k
#     否則left+=1
#     取max_len=max(len(left,right),max_len)
        
        
# pesudo 修正
# left = 0
# max_len = 0
# dic_win = {}          # 紀錄每個字在 window 出現次數
# max_freq = 0          # 窗口裡出現次數最多的那個字的次數

# for right 從 0 到 len(s)-1:
#     ch = s[right]

#     # 更新當前字元的次數
#     dic_win[ch] = dic_win.get(ch, 0) + 1

#     # 更新目前 window 裡最多的字的次數
#     max_freq = max(max_freq, dic_win[ch])

#     # 算目前 window 大小
#     window_size = right - left + 1

#     # 檢查需不需要縮左邊
#     # 需要改的字數 = window_size - max_freq
#     while window_size - max_freq > k:
#         # 把 left 的字移出 window
#         left_ch = s[left]
#         dic_win[left_ch] -= 1
#         left += 1

#         window_size = right - left + 1

#     # 這裡代表 window 是合法的，可以更新答案
#     max_len = max(max_len, window_size)

# return max_len



class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """        
        left=0
        max_len=0
        dic_win={}
        max_freq=0
        for right in range(len(s)):
            ch=s[right]
            #更新當前字元的字數
            dic_win[ch]=dic_win.get(ch,0)+1

            #更新當前window中最多字的字數
            max_freq = max(max_freq,dic_win[ch])

            #算目前window大小
            window_size = right - left +1 

            #檢查需不需要左邊
            #需要改的字 = window_size - max_freq
            while(window_size-max_freq) > k:
                #則把left的字移出window
                left_ch=s[left]
                dic_win[left_ch] -= 1
                left += 1
                window_size = right - left + 1

            max_len= max(max_len,window_size)
        return max_len