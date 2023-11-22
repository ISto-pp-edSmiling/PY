class Solution:
    def longestPalindrome(self, s: str) -> str:
        left,check = 0,[]
        while not left == len(s)-1:
            li=''
            for right in range(left, len(s)):
                if s[right] == s[left] and not right == left and s[left:right+1] == s[left:right+1][::-1]:
                    if not li: li = (s[left:right+1])
                    elif s[left:right+1] > li: li = (s[left:right+1])
            left+=1
            if li: check.append(li)
        return max(check, key=len) if check else s[0]
'''    
Example 1:

Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.

Example 2:

Input: s = "cbbd"
Output: "bb"
'''