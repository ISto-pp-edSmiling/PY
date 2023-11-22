class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left, right, count= 0, 1, 1
        while right <= len(s)-1:
            li = [s[left]]
            while right <= len(s)-1 and (s[right] != s[left]):
                if s[right] in li: break
                else: li.append(s[right])
                right+=1
            count=max(count,len(li))
            left+=1
            right=left+1
        return count if s else 0
    
# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.
# better code below

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_set = set()
        left = 0
        max_length = 0

        for right in range(len(s)):
            while s[right] in char_set:
                char_set.remove(s[left])
                left += 1

            char_set.add(s[right])
            max_length = max(max_length, right - left + 1)

        return max_length