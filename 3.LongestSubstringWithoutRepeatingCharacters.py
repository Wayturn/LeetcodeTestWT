# Given a string s, find the length of the longest substring without duplicate characters.

 

# Example 1:

# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3. Note that "bca" and "cab" are also correct answers.
# Example 2:

# Input: s = "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.
# Example 3:

# Input: s = "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3.
# Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
 

# Constraints:

# 0 <= s.length <= 5 * 104
# s consists of English letters, digits, symbols and spaces.

# pseudo code
# 建立一個left=0
# 建立一個win=[](用來記錄當前window內的數字)
# 建立一個max_len=0(用來記錄當前最長的長度)
# for right in len(s)-1
#     判斷當前win內有無重複字母
#         若有則將left+1
#         更新win
    
#     將s[right]加入 win
#     max_len=max((right-left+1),max_len)

# return max_len


class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        left=0
        win=[]
        max_len=0
        for right in range(len(s)):
            chr = s[right]
            while chr in win:
                win.remove(s[left])
                left+=1
            win.append(chr)
            max_len=max((right-left+1),max_len)
        return max_len





